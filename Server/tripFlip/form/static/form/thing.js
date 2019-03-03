$(document).ready(function() {
        console.log("hello")
        $('#nextButton').click(function() {
          var source = $('#source').val();
          var duration = $('#duration').val();
          var budget = $('#budget').val();
          var noOfPeople = $('#noOfPeople').val();
          var skillLevel = $('#skillLevel').val();
          var windSpeed = $('#windSpeed').val();
          var windDirection = $('#windDirection').val();
          var temperature = $('#temperature').val();
          $.ajax({
            type: 'POST',
            url: 'submitForm/',
            dataType: 'json',
            data: {'source': source, 'duration': duration, 'budget':budget,
             'noOfPeople':noOfPeople, 'skillLevel':skillLevel,
              'windSpeed':windSpeed, 'windDirection':windDirection,
               'temperature':temperature},
          });
          console.log("Done")
        });
});
