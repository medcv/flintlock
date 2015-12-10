import hashlib

from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.bundle import Bundle
from tastypie.resources import Resource
from brpy import init_brpy

import os
import tempfile

from tastypie.serializers import Serializer

from vida.fileservice.helpers import get_fileservice_files, get_filename_absolute
from vida.firestation.api import PrettyJSONSerializer
from vida.vida.models import Person


class FaceSearch(object):
    name = ''


class FaceSearchResource(Resource):
    name = fields.CharField(attribute='name')
    br = init_brpy()

    class Meta:
        resource_name = 'facesearchservice'
        object_class = FaceSearch
        fields = ['name']
        include_resource_uri = False
        allowed_methods = ['post']
        always_return_data = True
        authentication = BasicAuthentication()
        authorization = Authorization()

    def determine_format(self, request):
        return 'application/json'

    def deserialize(self, request, data, format=None):
        if not format:
            format = request.META.get('CONTENT_TYPE', 'application/json')

        if format == 'application/x-www-form-urlencoded':
            return request.POST

        if format.startswith('multipart'):
            data = request.POST.copy()
            data.update(request.FILES)
            return data

        return super(Resource, self).deserialize(request, data, format)

    def detail_uri_kwargs(self, bundle_or_obj):
        if isinstance(bundle_or_obj, Bundle):
            return {'name': bundle_or_obj.obj.name}
        else:
            return {'name': bundle_or_obj.name}

    def obj_create(self, bundle, request=None, **kwargs):
        # TODO: Need a one-time init somewhere
        self.br.br_initialize_default()
        self.br.br_set_property('algorithm', 'FaceRecognition')
        self.br.br_set_property('enrollAll', 'true')

        # create a new File
        bundle.obj = FaceSearch()
        # full_hydrate does the heavy lifting mapping the
        # POST-ed payload key/values to object attribute/values
        bundle = self.full_hydrate(bundle)
        file_data = bundle.data[u'file'].read()

        # write the file data to a temporary file
        filename_name, file_extension = os.path.splitext(bundle.data[u'file'].name)
        destination_file = tempfile.NamedTemporaryFile(suffix=file_extension)
        destination_file.write(file_data)
        # dest_img = destination_file.read()

        # OpenBR shizzy
        facetmpl = self.br.br_load_img(file_data, len(file_data))
        query = self.br.br_enroll_template(facetmpl)
        nqueries = self.br.br_num_templates(query)

        # More OpenBR shizzy
        scores = []
        for imgpath in get_fileservice_files():
            # load and enroll image from URL
            _name, _extension = os.path.splitext(imgpath)
            img = open(get_filename_absolute(imgpath), 'rb').read()
            tmpl = self.br.br_load_img(img, len(img))
            targets = self.br.br_enroll_template(tmpl)
            ntargets = self.br.br_num_templates(targets)

            # compare and collect scores
            scoresmat = self.br.br_compare_template_lists(targets, query)
            for r in range(ntargets):
                for c in range(nqueries):
                    percent_match = self.br.br_get_matrix_output_at(scoresmat, r, c)
                    # percentage match threshold > 50% likelihood
                    if percent_match > 0.5:
                        scores.append(('{}{}'.format(hashlib.sha1(img).hexdigest(), _extension), percent_match))

            # clean up - no memory leaks
            self.br.br_free_template(tmpl)
            self.br.br_free_template_list(targets)

        destination_file.close()

        # TODO: Ensure this is a one-time event along with br_initialize_default()
        self.br.br_finalize()

        peeps = Person.objects.filter(pic_filename__in=dict(scores).keys()).values()

        sorted_peeps = []

        scores.sort(key=lambda s: s[1])
        for s in scores:
            sorted_peeps.append(filter(lambda p: p['pic_filename'] == s[0], peeps)[0])

        # bundle the search results
        bundle.obj.name = bundle.data[u'file'].name
        bundle.data.pop(u'file', None)
        bundle.data['meta'] = {
            "limit": len(peeps),
            "next": None,
            "offset": 0,
            "previous": None,
            "total_count": len(peeps)
        }

        bundle.data['objects'] = sorted_peeps.reverse()
        bundle.data['scores'] = scores.reverse()
        return bundle