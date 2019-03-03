$(document).ready(function() {
        $.ajax({
            type: 'GET',
            url: "/reviews/getReviews/",
            dataType: 'json',
            success: async function (data) {
                document.getElementById("description1").innerHTML = "Location: "+data[0]['name']+" , Airport: "+data[0]['airport']+" , Wind Speed: "+data[0]['windspeed']+" m/s , Temperature: "+(Math.round(data[0]['temp']-273))+" C"; /*edit the description here*/
                document.getElementById("description2").innerHTML =  "Location: "+data[1]['name']+" , Airport: "+data[1]['airport']+" , Wind Speed: "+data[1]['windspeed']+" m/s , Temperature: "+(Math.round(data[1]['temp']-273))+" C";
                $('#resultsDiv').html("");
                if(data.return == "No Data"){
                    responsiveVoice.speak("Sorry, no reviews were found for this location. please try again.")
                    setTimeout(function(){
                        location.reload();
                    }, 5000);
                }
            }
        });
    });

function getData(){
    var file = xhttp.open("GET", "/getreviews", true);
    console.log(file);
 /*edit the description here*/
}



function share(){
  window.location.replace("https://www.facebook.com/");
  /*You can implement this shit if you want*/
}
