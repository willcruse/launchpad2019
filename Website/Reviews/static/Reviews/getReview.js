$(document).ready(function() {
    responsiveVoice.speak("What location would you like reviews for?");
    setTimeout(function() {
        console.log("finished sleeping");
        askSearch();
    }, 2500);

    function askSearch() {
        console.log("Request incomming")
        $.ajax({
            type: 'GET',
            url: "/reviews/getAudio/",
            dataType: 'json',
            success: function(data) {
                console.log(data);
                getReviews(data.message)
            }
        })
    }

    function getReviews(message) {
        var search = message;
        $.ajax({
            type: 'GET',
            url: "/reviews/getReviews/" + search.toLowerCase() + "/",
            dataType: 'json',
            success: async function (data) {
                console.log(data);
                $('#resultsDiv').html("");
                if(data.return == "No Data"){
                    responsiveVoice.speak("Sorry, no reviews were found for this location. please try again.")
                    setTimeout(function(){
                        location.reload();
                    }, 5000);

                }
                else{
                    getReviews2(data);
                }
            }
        });
    }

    function getReviews2(data){
        if (data.length == 0) return;
        var element = data[0];
        data.shift();


        var loc = element.fields.location;
        var auth = element.fields.author;
        var up = element.fields.upvotes;
        var dt = element.fields.datePosted;

        var text = auth + " has written: " +
                   element.fields.reviewText + "."
                   + " this review was upvoted "
                   + up + " times.";

        var id=element.pk;
        $('#resultsDiv').append(
            "<p><strong>Review: </strong> "+element.fields.reviewText+"</p>" +
            "<p><strong>Location: </strong> "+loc+"</p>" +
            "<p><strong>Author: </strong> "+auth+"</p>" +
            "<p><strong>Up-votes: </strong> "+up+"</p>" +
            "<p>"+dt+"</p>"+
            "<hr>");

        responsiveVoice.speak(text);
        setTimeout(function(){
            askUpVoteFunc(id,data);

        },9000);

    }

        function askUpVoteFunc(review,data1) {
            responsiveVoice.speak("was this helpful?");

            setTimeout(function() {
                console.log("Request incomming");
                $.ajax({
                    type: 'GET',
                    url: "/reviews/getAudio/",
                    dataType: 'json',
                    success: function(data) {upVote(review, data.message,data1);}
                });
            },1750);
        }

        function upVote(review, message,data){
            responsiveVoice.speak("thank you for your feedback.")
            setTimeout(function() {
                if(message.includes("yes") || message.includes("helpful") || message.includes("helpful")){
                    $.ajax({
                        type: 'POST',
                        url: '/reviews/incrementupvote/',
                        dataType: 'json',
                        data: {'idd': review},
                        success: function(data) {}
                    });
                }
                getReviews2(data);
            },1500);
        }

        function askForMore() {
            console.log("Request incomming");
            return $.ajax({
                type: 'GET',
                url: "/reviews/getAudio/",
                dataType: 'json',
                success: function(data) {
                    console.log(data.message);
                    if(data.message.includes("yes") || data.message.includes("helpful")){
                        console.log("continuing ...")
                        return true;
                    }
                    return false;
                }
            })
        }
    });
