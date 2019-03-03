$(document).ready(function() {
        responsiveVoice.speak("What location would you like reviews for?");
        $('#addButton').click(function() {
          var author = $('#author').val();
          var location = $('#location').val();
          var review = $('#review').val();
          $.ajax({
            type: 'POST',
            url: 'submitReview/',
            dataType: 'json',
            data: {'author': author.toLowerCase(), 'location': location.toLowerCase(), 'review': review.toLowerCase()},
          });

        });
      });
