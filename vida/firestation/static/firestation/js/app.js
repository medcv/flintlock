'use strict';

(function() {
  angular.module('fireStation', [
      'ngResource',
      'ngTable',
      'ui.bootstrap',
      'fireStation.factories',
      'fireStation.homeController',
      'fireStation.departmentDetailController',
      'fireStation.performanceScoreController',
      'fireStation.mapService',
      'fireStation.shelterService',
      'fireStation.formService',
      'fireStation.reportService',
      'fireStation.gauge',
      'fireStation.search',
      'fireStation.graphs',
      'fireStation.forms',
      'fireStation.report',
      'fireStation.reportList'
  ])

  .config(function($interpolateProvider, $httpProvider, $resourceProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $resourceProvider.defaults.stripTrailingSlashes = false;
  })

})();

