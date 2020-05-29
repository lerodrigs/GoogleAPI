$(document).ready(function() {
    $("#geoLocate").click(function() {
        var searchReq = $.get("/getGeolocate");
        searchReq.done(function(data) {
            $("#image").html(data);
        });
    });
  });