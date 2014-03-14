var mudahale = angular.module('mudahale', ['ngSanitize']);

mudahale.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.useXDomain = true;
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
}]);

mudahale.controller('mainController', ['$scope', '$http', '$window', '$timeout', function ($scope, $http, $window, $timeout) {
    $scope.stream = [];

    $scope.toUnixTime = function(stringDate) {
        return Date.parse(stringDate);
    }

    function getInitial() {
        console.log('requesting');
        $http({method: 'GET', url: 'http://www.mudahalebasladimi.com:8080/api'}).
            success(function(data, status, headers, config) {
                $scope.stream = data.result.reverse();
                $scope.pollingTask = $window.setInterval(pollData, 60000*3);
            }).
            error(function(data, status, headers, config) {
                $timeout(function() {
                    getInitial();
                }, 1000);
            });
    }

    function pollData() {
        var sinceId = $scope.stream[0].id;
        $http({method: 'GET', url: 'http://www.mudahalebasladimi.com:8080/api/search/since/' + sinceId}).
            success(function(data, status, headers, config) {
                $scope.stream = data.result.reverse().concat($scope.stream);
            }).
            error(function(data, status, headers, config) {

            });
    }

    getInitial();


}]);
