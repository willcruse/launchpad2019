function getData(){
  var file = xhttp.open("GET", "/getreviews", true);
  console.log(file);
  document.getElementById("description1").innerHTML = ""; /*edit the description here*/
  document.getElementById("description2").innerHTML = ""; /*edit the description here*/
}

function expand1(){
  document.getElementById("holiday1").id = "holiday1expanded";
  console.log("shazam");
}

function expand2(){
  document.getElementById("holiday2").id = "holiday2expanded";
}

function share(){
  /*You can implement this shit if you want*/
}
