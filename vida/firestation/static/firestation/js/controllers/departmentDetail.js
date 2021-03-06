'use strict';

(function() {
    angular.module('fireStation.departmentDetailController', [])

    .controller('jurisdictionController', function($scope, $http, CurrentUser, LatestTracks, Report, map, $interval, reportService, formService, Form) {
          var departmentMap = map.initMap('map', {scrollWheelZoom: false});
          var timeFormat = 'MMMM Do YYYY, hh:mm:ss';
          var fitBoundsOptions = {};
          var queryDict = {};
          var tracksLayer, stop;

          $scope.tracks = [];
          $scope.lastUpdated = moment().format(timeFormat);

          CurrentUser.query().$promise.then(function(data) {
            reportService.setCurrentUser(data);
          }, function(error) {
            console.log('Error retrieving current user: ', error);
          });

          location.search.substr(1).split("&").forEach(function(item) {queryDict[item.split("=")[0]] = item.split("=")[1]});

          function setUpdateTime() {
                $scope.lastUpdated = moment().format(timeFormat);
            }

          function updateTracks() {
            LatestTracks.query().$promise.then(function(data) {
                 $scope.tracks = data.objects;

                  var tracksMarkers = [];
                  var numTracks = $scope.tracks.length;
                  for (var i = 0; i < numTracks; i++) {
                      var track = $scope.tracks[i];
                      var markerRadius = 3;
                      var markerConfig = {fillOpacity: .5, color: track.force_color};
                      var user = track.user ? track.user.username : 'Not Specified';
                      var shouldAnimate = true;
                      if (moment.now() - moment(new Date(track.timestamp)) > 1000 * 300 /* 300 seconds */) {
                        shouldAnimate = false;
                      }

                      var popupText = '<b>User: </b>' + user + '<br/> <b>Time:</b> ' + moment(new Date(track.timestamp)).format(timeFormat);

                      markerConfig.icon = L.icon.pulse({
                        iconSize: track.mayday ? [20,20] : [10,10],
                        color: track.force_color,
                        pulseColor: track.mayday ? '#FF851B' : track.force_color,
                        heartbeat: track.mayday ? 0.4 : 1,
                        animate: shouldAnimate,
                        border: track.mayday ? '3px solid #FF851B' : '0'
                      });

                      if (track.mayday === true) {
                        popupText = '<b>Mayday!</b><br/>' + popupText;
                      }

                      var marker = L.marker(track.geom.coordinates.reverse(), markerConfig);

                      marker.bindPopup(popupText);
                      tracksMarkers.push(marker);
                  }

				 if (numTracks > 0) {
                    if (angular.isDefined(tracksLayer) === true) {
                        departmentMap.removeLayer(tracksLayer);
                        map.layerControl.removeLayer(tracksLayer);
                    }
                    tracksLayer = L.featureGroup(tracksMarkers);
                    tracksLayer.addTo(departmentMap);
                    map.layerControl.addOverlay(tracksLayer, 'GPS Tracks');
			     }
                 setUpdateTime();
              });
          };

          var stopPolling = function() {
              if (angular.isDefined(stop)) {
                $interval.cancel(stop);
                stop = undefined;
              }
          };

          var startPolling = function() {
              stop = $interval(function() {
                updateTracks()
              }, 30000);
          };

          updateTracks();
          startPolling();

           $scope.zoomToTracksLayer = function () {
               departmentMap.fitBounds(tracksLayer.getBounds(), fitBoundsOptions);
           };

           if (queryDict.hasOwnProperty('showReport') === true) {
              Report.query({id: queryDict.showReport}).$promise.then(function(data) {
                  var re = /^\/api\/v1\/form\/(\d+)\/$/;

                  Form.query({id: data.form.match(re)[1]}).$promise.then(function(form){
                      formService.processForm(form)
                      reportService.updateReport(data, true);
                      reportService.viewReport(data, true);
                  });
              });
           };

          /*
          if (config.centroid != null) {
           var headquarters = L.marker(config.centroid, {icon: headquartersIcon,zIndexOffset:1000});
           headquarters.addTo(departmentMap);
           layersControl.addOverlay(headquarters, 'Headquarters Location');
          };

          if (config.geom != null) {
           var countyBoundary = L.geoJson(config.geom, {
                                  style: function (feature) {
                                      return {color: '#0074D9', fillOpacity: .05, opacity:.8, weight:2};
                                  }
                              }).addTo(departmentMap);
            layersControl.addOverlay(countyBoundary, 'Jurisdiction Boundary');
            departmentMap.fitBounds(countyBoundary.getBounds(), fitBoundsOptions);
          } else {
              departmentMap.setView(config.centroid, 13);
          }
          */
          $scope.toggleFullScreenMap = function() {
              departmentMap.toggleFullscreen();
          };

      })

      .controller('personController', function($scope, $rootScope, $http, shelterServ) {
        $scope.shelterList = [];
        $scope.current_shelter = {};

        $scope.getShelterByUUID = function(id) {
          var shelter = shelterServ.getShelterByUUID(id);
          if (shelter) {
            document.getElementById("shelterID").innerHTML = '<div class="ct-u-displayTableCell">' +
              '<span class="ct-fw-600">Current Shelter</span></div>' +
              '<div class="ct-u-displayTableCell text-right">' +
              '<span>' + shelter.name + '   </span>' +
              '<a style="display: inline-block;"' +
              'class="fa fa-chevron-right trigger" href="/shelters/' + shelter.id + '\/" ></a></div> </div>';
            return shelter;
          } else
            return undefined;
        };

        $scope.getAllShelters = function() {
          shelterServ.getAllShelters(function() {});
        };

        $scope.getAllShelters();
      })
})();
