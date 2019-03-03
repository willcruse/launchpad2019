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
