$(document).ready(function() {
        $('#addButton').click(function() {
          var source = $('#source').val();
          var duration = $('#duration').val();
          var budget = $('#budget').val();
          var noOfPeople = $('#noOfPeople').val();
          var skillLevel = $('#skillLevel').val();
          var windSpeed = $('#windSpeed').val();
          var windDirection = $('#windDirection').val();
          var temperature = $('#temperature').val();
          var array = windDirection.split(" ");
          var i;
          var windDirection = "";
          for (i = 0; i < 2; i++) {
              var windDirection = windDirection.concat(array[i].charAt(0)).toUpperCase();
          }
          console.log(windDirection);
          $.ajax({
            type: 'POST',
            url: 'submitReview/',
            dataType: 'json',
            data: {'source': source, 'duration': duration, 'budget':budget,
             'noOfPeople':noOfPeople, 'skillLevel':skillLevel.charAt(0).toUpperCase(),
              'windSpeed':windSpeed, 'windDirection':windDirection,
               'temperature':temperature},
          });
        });
});
