# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CongressionalDistrict',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('permanent_identifier', models.CharField(max_length=40, null=True, blank=True)),
                ('source_featureid', models.CharField(max_length=40, null=True, blank=True)),
                ('source_datasetid', models.CharField(max_length=40, null=True, blank=True)),
                ('source_datadesc', models.CharField(max_length=100, null=True, blank=True)),
                ('source_originator', models.CharField(max_length=130, null=True, blank=True)),
                ('data_security', models.IntegerField(blank=True, null=True, choices=[(0, b'Unknown'), (1, b'Top Secret'), (2, b'Secret'), (3, b'Confidential'), (4, b'Restricted'), (5, b'Unclassified'), (6, b'Sensitive')])),
                ('distribution_policy', models.CharField(blank=True, max_length=4, null=True, choices=[(b'A1', b'Emergency Service Provider - Internal Use Only'), (b'A2', b'Emergency Service Provider - Bitmap Display Via Web'), (b'A3', b'Emergency Service Provider - Free Distribution to Third Parties'), (b'A4', b'Emergency Service Provider - Free Distribution to Third Parties Via Internet'), (b'B1', b'Government Agencies or Their Delegated Agents - Internal Use Only'), (b'B2', b'Government Agencies or Their Delegated Agents - Bitmap Display Via Web'), (b'B3', b'Government Agencies or Their Delegated Agents - Free Distribution to Third Parties'), (b'B4', b'Government Agencies or Their Delegated Agents - Free Distribution to Third Parties Via Internet'), (b'C1', b'Other Public or Educational Institutions - Internal Use Only'), (b'C2', b'Other Public or Educational Institutions - Bitmap Display Via Web'), (b'C3', b'Other Public or Educational Institutions - Free Distribution to Third Parties'), (b'C4', b'Other Public or Educational Institutions - Free Distribution to Third Parties Via Internet'), (b'D1', b'Data Contributors - Internal Use Only'), (b'D2', b'Data Contributors - Bitmap Display Via Web'), (b'D3', b'Data Contributors - Free Distribution to Third Parties'), (b'D4', b'Data Contributors - Free Distribution to Third Parties Via Internet'), (b'E1', b'Public Domain - Internal Use Only'), (b'E2', b'Public Domain - Bitmap Display Via Web'), (b'E3', b'Public Domain - Free Distribution to Third Parties'), (b'E4', b'Public Domain - Free Distribution to Third Parties Via Internet')])),
                ('loaddate', models.DateTimeField(null=True, blank=True)),
                ('ftype', models.CharField(max_length=50, null=True, blank=True)),
                ('gnis_id', models.CharField(max_length=10, null=True, blank=True)),
                ('globalid', models.CharField(max_length=38, null=True, blank=True)),
                ('objectid', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=120, null=True, blank=True)),
                ('fcode', models.IntegerField(blank=True, null=True, choices=[(62200, 'Fire District')])),
                ('designation', models.CharField(max_length=60, null=True, blank=True)),
                ('state_fipscode', models.CharField(max_length=2, null=True, blank=True)),
                ('state_name', models.CharField(max_length=120, null=True, blank=True)),
                ('admintype', models.IntegerField(blank=True, null=True, choices=[(0, 'Unknown'), (1, 'Federal'), (2, 'Tribal'), (3, 'State'), (4, 'Regional'), (5, 'County'), (6, 'Municipal'), (7, 'Private')])),
                ('ownerormanagingagency', models.IntegerField(blank=True, null=True, choices=[(1, 'Army Corps of Engineers'), (15, 'Bureau of Census'), (2, 'Bureau of Indian Affairs'), (3, 'Bureau of Land Management'), (4, 'Bureau of Reclamation'), (5, 'Department of Defense'), (6, 'Department of Energy'), (7, 'Department of Homeland Security'), (8, 'Department of Transportation'), (9, 'Department of Veteran Affairs'), (10, 'Fish and Wildlife Service'), (11, 'Forest Service'), (12, 'National Oceanic and Atmospheric Administration'), (13, 'National Park Service'), (14, 'Tennessee Valley Authority'), (99, 'Not Applicable')])),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CountyorEquivalent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('permanent_identifier', models.CharField(max_length=40, null=True, blank=True)),
                ('source_featureid', models.CharField(max_length=40, null=True, blank=True)),
                ('source_datasetid', models.CharField(max_length=40, null=True, blank=True)),
                ('source_datadesc', models.CharField(max_length=100, null=True, blank=True)),
                ('source_originator', models.CharField(max_length=130, null=True, blank=True)),
                ('data_security', models.IntegerField(blank=True, null=True, choices=[(0, b'Unknown'), (1, b'Top Secret'), (2, b'Secret'), (3, b'Confidential'), (4, b'Restricted'), (5, b'Unclassified'), (6, b'Sensitive')])),
                ('distribution_policy', models.CharField(blank=True, max_length=4, null=True, choices=[(b'A1', b'Emergency Service Provider - Internal Use Only'), (b'A2', b'Emergency Service Provider - Bitmap Display Via Web'), (b'A3', b'Emergency Service Provider - Free Distribution to Third Parties'), (b'A4', b'Emergency Service Provider - Free Distribution to Third Parties Via Internet'), (b'B1', b'Government Agencies or Their Delegated Agents - Internal Use Only'), (b'B2', b'Government Agencies or Their Delegated Agents - Bitmap Display Via Web'), (b'B3', b'Government Agencies or Their Delegated Agents - Free Distribution to Third Parties'), (b'B4', b'Government Agencies or Their Delegated Agents - Free Distribution to Third Parties Via Internet'), (b'C1', b'Other Public or Educational Institutions - Internal Use Only'), (b'C2', b'Other Public or Educational Institutions - Bitmap Display Via Web'), (b'C3', b'Other Public or Educational Institutions - Free Distribution to Third Parties'), (b'C4', b'Other Public or Educational Institutions - Free Distribution to Third Parties Via Internet'), (b'D1', b'Data Contributors - Internal Use Only'), (b'D2', b'Data Contributors - Bitmap Display Via Web'), (b'D3', b'Data Contributors - Free Distribution to Third Parties'), (b'D4', b'Data Contributors - Free Distribution to Third Parties Via Internet'), (b'E1', b'Public Domain - Internal Use Only'), (b'E2', b'Public Domain - Bitmap Display Via Web'), (b'E3', b'Public Domain - Free Distribution to Third Parties'), (b'E4', b'Public Domain - Free Distribution to Third Parties Via Internet')])),
                ('loaddate', models.DateTimeField(null=True, blank=True)),
                ('ftype', models.CharField(max_length=50, null=True, blank=True)),
                ('gnis_id', models.CharField(max_length=10, null=True, blank=True)),
                ('globalid', models.CharField(max_length=38, null=True, blank=True)),
                ('objectid', models.IntegerField(unique=True, null=True, blank=True)),
                ('fcode', models.IntegerField(blank=True, null=True, choices=[(61200, 'County'), (61201, 'Borough'), (61210, 'City and Borough'), (61202, 'District'), (61203, 'Independent City'), (61204, 'Island'), (61205, 'Judicial Division'), (61206, 'Municipality'), (61207, 'Municipio'), (61208, 'Parish'), (61299, 'Other County Equivalent Area')])),
                ('state_fipscode', models.CharField(max_length=2, null=True, blank=True)),
                ('state_name', models.CharField(max_length=120, null=True, blank=True)),
                ('county_fipscode', models.CharField(max_length=3, null=True, blank=True)),
                ('county_name', models.CharField(max_length=120, null=True, blank=True)),
                ('stco_fipscode', models.CharField(max_length=5, null=True, blank=True)),
                ('population', models.IntegerField(null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            options={
                'verbose_name': 'County (or Equivalent)',
            },
        ),
        migrations.CreateModel(
            name='GovUnits',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('objectid', models.IntegerField(unique=True, null=True, blank=True)),
                ('permanent_identifier', models.CharField(max_length=40, null=True, blank=True)),
                ('source_featureid', models.CharField(max_length=40, null=True, blank=True)),
                ('source_datasetid', models.CharField(max_length=40, null=True, blank=True)),
                ('source_datadesc', models.CharField(max_length=100, null=True, blank=True)),
                ('source_originator', models.CharField(max_length=130, null=True, blank=True)),
                ('data_security', models.IntegerField(blank=True, null=True, choices=[(0, b'Unknown'), (1, b'Top Secret'), (2, b'Secret'), (3, b'Confidential'), (4, b'Restricted'), (5, b'Unclassified'), (6, b'Sensitive')])),
                ('distribution_policy', models.CharField(blank=True, max_length=4, null=True, choices=[(b'A1', b'Emergency Service Provider - Internal Use Only'), (b'A2', b'Emergency Service Provider - Bitmap Display Via Web'), (b'A3', b'Emergency Service Provider - Free Distribution to Third Parties'), (b'A4', b'Emergency Service Provider - Free Distribution to Third Parties Via Internet'), (b'B1', b'Government Agencies or Their Delegated Agents - Internal Use Only'), (b'B2', b'Government Agencies or Their Delegated Agents - Bitmap Display Via Web'), (b'B3', b'Government Agencies or Their Delegated Agents - Free Distribution to Third Parties'), (b'B4', b'Government Agencies or Their Delegated Agents - Free Distribution to Third Parties Via Internet'), (b'C1', b'Other Public or Educational Institutions - Internal Use Only'), (b'C2', b'Other Public or Educational Institutions - Bitmap Display Via Web'), (b'C3', b'Other Public or Educational Institutions - Free Distribution to Third Parties'), (b'C4', b'Other Public or Educational Institutions - Free Distribution to Third Parties Via Internet'), (b'D1', b'Data Contributors - Internal Use Only'), (b'D2', b'Data Contributors - Bitmap Display Via Web'), (b'D3', b'Data Contributors - Free Distribution to Third Parties'), (b'D4', b'Data Contributors - Free Distribution to Third Parties Via Internet'), (b'E1', b'Public Domain - Internal Use Only'), (b'E2', b'Public Domain - Bitmap Display Via Web'), (b'E3', b'Public Domain - Free Distribution to Third Parties'), (b'E4', b'Public Domain - Free Distribution to Third Parties Via Internet')])),
                ('loaddate', models.DateTimeField(null=True, blank=True)),
                ('ftype', models.CharField(max_length=50, null=True, blank=True)),
                ('fcode', models.IntegerField(blank=True, null=True, choices=[(61200, b'County'), (61201, b'Borough'), (61210, b'City and Borough'), (61202, b'District'), (61203, b'Independent City'), (61204, b'Island'), (61205, b'Judicial Division'), (61206, b'Municipality'), (61207, b'Municipio'), (61208, b'Parish'), (61299, b'Other County Equivalent Area')])),
                ('state_fipscode', models.CharField(max_length=2, null=True, blank=True)),
                ('state_name', models.CharField(max_length=120, null=True, blank=True)),
                ('county_fipscode', models.CharField(max_length=3, null=True, blank=True)),
                ('county_name', models.CharField(max_length=120, null=True, blank=True)),
                ('population', models.IntegerField(null=True, blank=True)),
                ('gnis_id', models.CharField(max_length=10, null=True, blank=True)),
                ('fips', models.CharField(max_length=10, null=True, blank=True)),
                ('globalid', models.CharField(max_length=38, null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            options={
                'ordering': ('state_name', 'county_name'),
                'verbose_name': 'Government Unit',
                'verbose_name_plural': 'Government Units',
            },
        ),
        migrations.CreateModel(
            name='IncorporatedPlace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('permanent_identifier', models.CharField(max_length=40, null=True, blank=True)),
                ('source_featureid', models.CharField(max_length=40, null=True, blank=True)),
                ('source_datasetid', models.CharField(max_length=40, null=True, blank=True)),
                ('source_datadesc', models.CharField(max_length=100, null=True, blank=True)),
                ('source_originator', models.CharField(max_length=130, null=True, blank=True)),
                ('data_security', models.IntegerField(blank=True, null=True, choices=[(0, b'Unknown'), (1, b'Top Secret'), (2, b'Secret'), (3, b'Confidential'), (4, b'Restricted'), (5, b'Unclassified'), (6, b'Sensitive')])),
                ('distribution_policy', models.CharField(blank=True, max_length=4, null=True, choices=[(b'A1', b'Emergency Service Provider - Internal Use Only'), (b'A2', b'Emergency Service Provider - Bitmap Display Via Web'), (b'A3', b'Emergency Service Provider - Free Distribution to Third Parties'), (b'A4', b'Emergency Service Provider - Free Distribution to Third Parties Via Internet'), (b'B1', b'Government Agencies or Their Delegated Agents - Internal Use Only'), (b'B2', b'Government Agencies or Their Delegated Agents - Bitmap Display Via Web'), (b'B3', b'Government Agencies or Their Delegated Agents - Free Distribution to Third Parties'), (b'B4', b'Government Agencies or Their Delegated Agents - Free Distribution to Third Parties Via Internet'), (b'C1', b'Other Public or Educational Institutions - Internal Use Only'), (b'C2', b'Other Public or Educational Institutions - Bitmap Display Via Web'), (b'C3', b'Other Public or Educational Institutions - Free Distribution to Third Parties'), (b'C4', b'Other Public or Educational Institutions - Free Distribution to Third Parties Via Internet'), (b'D1', b'Data Contributors - Internal Use Only'), (b'D2', b'Data Contributors - Bitmap Display Via Web'), (b'D3', b'Data Contributors - Free Distribution to Third Parties'), (b'D4', b'Data Contributors - Free Distribution to Third Parties Via Internet'), (b'E1', b'Public Domain - Internal Use Only'), (b'E2', b'Public Domain - Bitmap Display Via Web'), (b'E3', b'Public Domain - Free Distribution to Third Parties'), (b'E4', b'Public Domain - Free Distribution to Third Parties Via Internet')])),
                ('loaddate', models.DateTimeField(null=True, blank=True)),
                ('ftype', models.CharField(max_length=50, null=True, blank=True)),
                ('gnis_id', models.CharField(max_length=10, null=True, blank=True)),
                ('globalid', models.CharField(max_length=38, null=True, blank=True)),
                ('objectid', models.IntegerField(unique=True, null=True, blank=True)),
                ('fcode', models.IntegerField(blank=True, null=True, choices=[(61400, 'Incorporated Place'), (61401, 'Borough'), (61403, 'City'), (61404, 'City and Borough'), (61405, 'Communidad'), (61407, 'Consolidated City'), (61410, 'Independent City'), (61412, 'Municipality'), (61414, 'Town'), (61415, 'Village'), (61416, 'Zona Urbana')])),
                ('state_name', models.CharField(max_length=120, null=True, blank=True)),
                ('place_fipscode', models.CharField(max_length=5, null=True, verbose_name=b'FIPS Code', blank=True)),
                ('place_name', models.CharField(max_length=120, null=True, blank=True)),
                ('population', models.IntegerField(null=True, blank=True)),
                ('iscapitalcity', models.IntegerField(blank=True, null=True, choices=[(1, 'Yes'), (2, 'No'), (0, 'Unknown')])),
                ('iscountyseat', models.IntegerField(blank=True, null=True, choices=[(1, 'Yes'), (2, 'No'), (0, 'Unknown')])),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            options={
                'ordering': ('state_name', 'place_name'),
            },
        ),
        migrations.CreateModel(
            name='MinorCivilDivision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('permanent_identifier', models.CharField(max_length=40, null=True, blank=True)),
                ('source_featureid', models.CharField(max_length=40, null=True, blank=True)),
                ('source_datasetid', models.CharField(max_length=40, null=True, blank=True)),
                ('source_datadesc', models.CharField(max_length=100, null=True, blank=True)),
                ('source_originator', models.CharField(max_length=130, null=True, blank=True)),
                ('data_security', models.IntegerField(blank=True, null=True, choices=[(0, b'Unknown'), (1, b'Top Secret'), (2, b'Secret'), (3, b'Confidential'), (4, b'Restricted'), (5, b'Unclassified'), (6, b'Sensitive')])),
                ('distribution_policy', models.CharField(blank=True, max_length=4, null=True, choices=[(b'A1', b'Emergency Service Provider - Internal Use Only'), (b'A2', b'Emergency Service Provider - Bitmap Display Via Web'), (b'A3', b'Emergency Service Provider - Free Distribution to Third Parties'), (b'A4', b'Emergency Service Provider - Free Distribution to Third Parties Via Internet'), (b'B1', b'Government Agencies or Their Delegated Agents - Internal Use Only'), (b'B2', b'Government Agencies or Their Delegated Agents - Bitmap Display Via Web'), (b'B3', b'Government Agencies or Their Delegated Agents - Free Distribution to Third Parties'), (b'B4', b'Government Agencies or Their Delegated Agents - Free Distribution to Third Parties Via Internet'), (b'C1', b'Other Public or Educational Institutions - Internal Use Only'), (b'C2', b'Other Public or Educational Institutions - Bitmap Display Via Web'), (b'C3', b'Other Public or Educational Institutions - Free Distribution to Third Parties'), (b'C4', b'Other Public or Educational Institutions - Free Distribution to Third Parties Via Internet'), (b'D1', b'Data Contributors - Internal Use Only'), (b'D2', b'Data Contributors - Bitmap Display Via Web'), (b'D3', b'Data Contributors - Free Distribution to Third Parties'), (b'D4', b'Data Contributors - Free Distribution to Third Parties Via Internet'), (b'E1', b'Public Domain - Internal Use Only'), (b'E2', b'Public Domain - Bitmap Display Via Web'), (b'E3', b'Public Domain - Free Distribution to Third Parties'), (b'E4', b'Public Domain - Free Distribution to Third Parties Via Internet')])),
                ('loaddate', models.DateTimeField(null=True, blank=True)),
                ('ftype', models.CharField(max_length=50, null=True, blank=True)),
                ('gnis_id', models.CharField(max_length=10, null=True, blank=True)),
                ('globalid', models.CharField(max_length=38, null=True, blank=True)),
                ('objectid', models.IntegerField(unique=True, null=True, blank=True)),
                ('fcode', models.IntegerField(blank=True, null=True, choices=[(61300, 'Minor Civil Division'), (61302, 'Barrio'), (61304, 'Barrio - Pueblo'), (61306, 'Borough'), (61308, 'Census County Division'), (61310, 'Census Sub Area'), (61312, 'Census Sub District'), (61314, 'Charter Township'), (61316, 'City'), (61318, 'County'), (61320, 'District'), (61322, 'Gore'), (61324, 'Grant'), (61326, 'Incorporated Town'), (61328, 'Independent City'), (61330, 'Island'), (61332, 'Location'), (61334, 'Municipality'), (61336, 'Plantation'), (61338, 'Precinct'), (61340, 'Purchase'), (61342, 'Reservation'), (61344, 'Subbarrio'), (61346, 'Town'), (61348, 'Township'), (61350, 'Unorganized Territory'), (61352, 'Village')])),
                ('state_name', models.CharField(max_length=120, null=True, blank=True)),
                ('minorcivildivision_fipscode', models.CharField(max_length=10, null=True, blank=True)),
                ('minorcivildivision_name', models.CharField(max_length=120, null=True, blank=True)),
                ('population', models.IntegerField(null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NativeAmericanArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('permanent_identifier', models.CharField(max_length=40, null=True, blank=True)),
                ('source_featureid', models.CharField(max_length=40, null=True, blank=True)),
                ('source_datasetid', models.CharField(max_length=40, null=True, blank=True)),
                ('source_datadesc', models.CharField(max_length=100, null=True, blank=True)),
                ('source_originator', models.CharField(max_length=130, null=True, blank=True)),
                ('data_security', models.IntegerField(blank=True, null=True, choices=[(0, b'Unknown'), (1, b'Top Secret'), (2, b'Secret'), (3, b'Confidential'), (4, b'Restricted'), (5, b'Unclassified'), (6, b'Sensitive')])),
                ('distribution_policy', models.CharField(blank=True, max_length=4, null=True, choices=[(b'A1', b'Emergency Service Provider - Internal Use Only'), (b'A2', b'Emergency Service Provider - Bitmap Display Via Web'), (b'A3', b'Emergency Service Provider - Free Distribution to Third Parties'), (b'A4', b'Emergency Service Provider - Free Distribution to Third Parties Via Internet'), (b'B1', b'Government Agencies or Their Delegated Agents - Internal Use Only'), (b'B2', b'Government Agencies or Their Delegated Agents - Bitmap Display Via Web'), (b'B3', b'Government Agencies or Their Delegated Agents - Free Distribution to Third Parties'), (b'B4', b'Government Agencies or Their Delegated Agents - Free Distribution to Third Parties Via Internet'), (b'C1', b'Other Public or Educational Institutions - Internal Use Only'), (b'C2', b'Other Public or Educational Institutions - Bitmap Display Via Web'), (b'C3', b'Other Public or Educational Institutions - Free Distribution to Third Parties'), (b'C4', b'Other Public or Educational Institutions - Free Distribution to Third Parties Via Internet'), (b'D1', b'Data Contributors - Internal Use Only'), (b'D2', b'Data Contributors - Bitmap Display Via Web'), (b'D3', b'Data Contributors - Free Distribution to Third Parties'), (b'D4', b'Data Contributors - Free Distribution to Third Parties Via Internet'), (b'E1', b'Public Domain - Internal Use Only'), (b'E2', b'Public Domain - Bitmap Display Via Web'), (b'E3', b'Public Domain - Free Distribution to Third Parties'), (b'E4', b'Public Domain - Free Distribution to Third Parties Via Internet')])),
                ('loaddate', models.DateTimeField(null=True, blank=True)),
                ('ftype', models.CharField(max_length=50, null=True, blank=True)),
                ('gnis_id', models.CharField(max_length=10, null=True, blank=True)),
                ('globalid', models.CharField(max_length=38, null=True, blank=True)),
                ('objectid', models.IntegerField(unique=True, null=True, blank=True)),
                ('name', models.CharField(max_length=120, null=True, blank=True)),
                ('fcode', models.IntegerField(blank=True, null=True, choices=[(64000, 'Native American Reservation'), (64080, 'Tribal Designated Statistic Area'), (64081, 'Colony'), (64082, 'Community'), (64083, 'Joint Use Area'), (64084, 'Pueblo'), (64085, 'Rancheria'), (64086, 'Reservation'), (64087, 'Reserve'), (64088, 'Oklahoma Tribal Statistical Area'), (64089, 'American Indian Trust Land'), (64090, 'Joint Use Oklahoma Tribal Statistical Area'), (64091, 'Ranch'), (64092, 'State Designated American Indian Statistical Area'), (64093, 'Indian Village'), (64095, 'Indian Community'), (64096, 'American Indian Off-Reservation Trust Land')])),
                ('nativeamericanarea_fipscode', models.CharField(max_length=5, null=True, blank=True)),
                ('admintype', models.IntegerField(blank=True, null=True, choices=[(0, 'Unknown'), (1, 'Federal'), (2, 'Tribal'), (3, 'State'), (4, 'Regional'), (5, 'County'), (6, 'Municipal'), (7, 'Private')])),
                ('population', models.IntegerField(null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('permanent_identifier', models.CharField(max_length=40, null=True, blank=True)),
                ('source_featureid', models.CharField(max_length=40, null=True, blank=True)),
                ('source_datasetid', models.CharField(max_length=40, null=True, blank=True)),
                ('source_datadesc', models.CharField(max_length=100, null=True, blank=True)),
                ('source_originator', models.CharField(max_length=130, null=True, blank=True)),
                ('data_security', models.IntegerField(blank=True, null=True, choices=[(0, b'Unknown'), (1, b'Top Secret'), (2, b'Secret'), (3, b'Confidential'), (4, b'Restricted'), (5, b'Unclassified'), (6, b'Sensitive')])),
                ('distribution_policy', models.CharField(blank=True, max_length=4, null=True, choices=[(b'A1', b'Emergency Service Provider - Internal Use Only'), (b'A2', b'Emergency Service Provider - Bitmap Display Via Web'), (b'A3', b'Emergency Service Provider - Free Distribution to Third Parties'), (b'A4', b'Emergency Service Provider - Free Distribution to Third Parties Via Internet'), (b'B1', b'Government Agencies or Their Delegated Agents - Internal Use Only'), (b'B2', b'Government Agencies or Their Delegated Agents - Bitmap Display Via Web'), (b'B3', b'Government Agencies or Their Delegated Agents - Free Distribution to Third Parties'), (b'B4', b'Government Agencies or Their Delegated Agents - Free Distribution to Third Parties Via Internet'), (b'C1', b'Other Public or Educational Institutions - Internal Use Only'), (b'C2', b'Other Public or Educational Institutions - Bitmap Display Via Web'), (b'C3', b'Other Public or Educational Institutions - Free Distribution to Third Parties'), (b'C4', b'Other Public or Educational Institutions - Free Distribution to Third Parties Via Internet'), (b'D1', b'Data Contributors - Internal Use Only'), (b'D2', b'Data Contributors - Bitmap Display Via Web'), (b'D3', b'Data Contributors - Free Distribution to Third Parties'), (b'D4', b'Data Contributors - Free Distribution to Third Parties Via Internet'), (b'E1', b'Public Domain - Internal Use Only'), (b'E2', b'Public Domain - Bitmap Display Via Web'), (b'E3', b'Public Domain - Free Distribution to Third Parties'), (b'E4', b'Public Domain - Free Distribution to Third Parties Via Internet')])),
                ('loaddate', models.DateTimeField(null=True, blank=True)),
                ('ftype', models.CharField(max_length=50, null=True, blank=True)),
                ('gnis_id', models.CharField(max_length=10, null=True, blank=True)),
                ('globalid', models.CharField(max_length=38, null=True, blank=True)),
                ('objectid', models.IntegerField(unique=True, null=True, blank=True)),
                ('name', models.CharField(max_length=120, null=True, blank=True)),
                ('fcode', models.IntegerField(blank=True, null=True, choices=[(67500, 'Wilderness')])),
                ('admintype', models.IntegerField(blank=True, null=True, choices=[(0, 'Unknown'), (1, 'Federal'), (2, 'Tribal'), (3, 'State'), (4, 'Regional'), (5, 'County'), (6, 'Municipal'), (7, 'Private')])),
                ('ownerormanagingagency', models.IntegerField(blank=True, null=True, choices=[(1, 'Army Corps of Engineers'), (15, 'Bureau of Census'), (2, 'Bureau of Indian Affairs'), (3, 'Bureau of Land Management'), (4, 'Bureau of Reclamation'), (5, 'Department of Defense'), (6, 'Department of Energy'), (7, 'Department of Homeland Security'), (8, 'Department of Transportation'), (9, 'Department of Veteran Affairs'), (10, 'Fish and Wildlife Service'), (11, 'Forest Service'), (12, 'National Oceanic and Atmospheric Administration'), (13, 'National Park Service'), (14, 'Tennessee Valley Authority'), (99, 'Not Applicable')])),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StateorTerritoryHigh',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('permanent_identifier', models.CharField(max_length=40, null=True, blank=True)),
                ('source_featureid', models.CharField(max_length=40, null=True, blank=True)),
                ('source_datasetid', models.CharField(max_length=40, null=True, blank=True)),
                ('source_datadesc', models.CharField(max_length=100, null=True, blank=True)),
                ('source_originator', models.CharField(max_length=130, null=True, blank=True)),
                ('data_security', models.IntegerField(blank=True, null=True, choices=[(0, b'Unknown'), (1, b'Top Secret'), (2, b'Secret'), (3, b'Confidential'), (4, b'Restricted'), (5, b'Unclassified'), (6, b'Sensitive')])),
                ('distribution_policy', models.CharField(blank=True, max_length=4, null=True, choices=[(b'A1', b'Emergency Service Provider - Internal Use Only'), (b'A2', b'Emergency Service Provider - Bitmap Display Via Web'), (b'A3', b'Emergency Service Provider - Free Distribution to Third Parties'), (b'A4', b'Emergency Service Provider - Free Distribution to Third Parties Via Internet'), (b'B1', b'Government Agencies or Their Delegated Agents - Internal Use Only'), (b'B2', b'Government Agencies or Their Delegated Agents - Bitmap Display Via Web'), (b'B3', b'Government Agencies or Their Delegated Agents - Free Distribution to Third Parties'), (b'B4', b'Government Agencies or Their Delegated Agents - Free Distribution to Third Parties Via Internet'), (b'C1', b'Other Public or Educational Institutions - Internal Use Only'), (b'C2', b'Other Public or Educational Institutions - Bitmap Display Via Web'), (b'C3', b'Other Public or Educational Institutions - Free Distribution to Third Parties'), (b'C4', b'Other Public or Educational Institutions - Free Distribution to Third Parties Via Internet'), (b'D1', b'Data Contributors - Internal Use Only'), (b'D2', b'Data Contributors - Bitmap Display Via Web'), (b'D3', b'Data Contributors - Free Distribution to Third Parties'), (b'D4', b'Data Contributors - Free Distribution to Third Parties Via Internet'), (b'E1', b'Public Domain - Internal Use Only'), (b'E2', b'Public Domain - Bitmap Display Via Web'), (b'E3', b'Public Domain - Free Distribution to Third Parties'), (b'E4', b'Public Domain - Free Distribution to Third Parties Via Internet')])),
                ('loaddate', models.DateTimeField(null=True, blank=True)),
                ('ftype', models.CharField(max_length=50, null=True, blank=True)),
                ('gnis_id', models.CharField(max_length=10, null=True, blank=True)),
                ('globalid', models.CharField(max_length=38, null=True, blank=True)),
                ('objectid', models.IntegerField(unique=True, null=True, blank=True)),
                ('fcode', models.IntegerField(blank=True, null=True, choices=[(61100, 'State'), (61101, 'Territory'), (61102, 'Province')])),
                ('state_fipscode', models.CharField(max_length=2, null=True, blank=True)),
                ('state_name', models.CharField(max_length=120, null=True, blank=True)),
                ('population', models.IntegerField(null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UnincorporatedPlace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('permanent_identifier', models.CharField(max_length=40, null=True, blank=True)),
                ('source_featureid', models.CharField(max_length=40, null=True, blank=True)),
                ('source_datasetid', models.CharField(max_length=40, null=True, blank=True)),
                ('source_datadesc', models.CharField(max_length=100, null=True, blank=True)),
                ('source_originator', models.CharField(max_length=130, null=True, blank=True)),
                ('data_security', models.IntegerField(blank=True, null=True, choices=[(0, b'Unknown'), (1, b'Top Secret'), (2, b'Secret'), (3, b'Confidential'), (4, b'Restricted'), (5, b'Unclassified'), (6, b'Sensitive')])),
                ('distribution_policy', models.CharField(blank=True, max_length=4, null=True, choices=[(b'A1', b'Emergency Service Provider - Internal Use Only'), (b'A2', b'Emergency Service Provider - Bitmap Display Via Web'), (b'A3', b'Emergency Service Provider - Free Distribution to Third Parties'), (b'A4', b'Emergency Service Provider - Free Distribution to Third Parties Via Internet'), (b'B1', b'Government Agencies or Their Delegated Agents - Internal Use Only'), (b'B2', b'Government Agencies or Their Delegated Agents - Bitmap Display Via Web'), (b'B3', b'Government Agencies or Their Delegated Agents - Free Distribution to Third Parties'), (b'B4', b'Government Agencies or Their Delegated Agents - Free Distribution to Third Parties Via Internet'), (b'C1', b'Other Public or Educational Institutions - Internal Use Only'), (b'C2', b'Other Public or Educational Institutions - Bitmap Display Via Web'), (b'C3', b'Other Public or Educational Institutions - Free Distribution to Third Parties'), (b'C4', b'Other Public or Educational Institutions - Free Distribution to Third Parties Via Internet'), (b'D1', b'Data Contributors - Internal Use Only'), (b'D2', b'Data Contributors - Bitmap Display Via Web'), (b'D3', b'Data Contributors - Free Distribution to Third Parties'), (b'D4', b'Data Contributors - Free Distribution to Third Parties Via Internet'), (b'E1', b'Public Domain - Internal Use Only'), (b'E2', b'Public Domain - Bitmap Display Via Web'), (b'E3', b'Public Domain - Free Distribution to Third Parties'), (b'E4', b'Public Domain - Free Distribution to Third Parties Via Internet')])),
                ('loaddate', models.DateTimeField(null=True, blank=True)),
                ('ftype', models.CharField(max_length=50, null=True, blank=True)),
                ('gnis_id', models.CharField(max_length=10, null=True, blank=True)),
                ('globalid', models.CharField(max_length=38, null=True, blank=True)),
                ('objectid', models.IntegerField(unique=True, null=True, blank=True)),
                ('fcode', models.IntegerField(blank=True, null=True, choices=[(61500, 'Unincorporated Place'), (61501, 'Census Designated Place'), (61502, 'Community / Town / Village'), (61503, 'Neighborhood'), (61504, 'Subdivision'), (61505, 'Communidad'), (61506, 'Zona Urbana')])),
                ('state_name', models.CharField(max_length=120, null=True, blank=True)),
                ('place_fipscode', models.CharField(max_length=5, null=True, blank=True)),
                ('place_name', models.CharField(max_length=120, null=True, blank=True)),
                ('population', models.IntegerField(null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
