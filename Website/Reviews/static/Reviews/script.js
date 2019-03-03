var source = "";
var duration = 0;
var budget = 0;
var peopleCount = 0;
var skillLevel = "";
var windSpeed = 0;
var windDirection = "";
var temperature = 0;

function step1to2(){
  source = document.getElementById('airport').value;
  document.getElementById('questionContainerAppear').id = "questionContainerDisappear";
  document.getElementById('questionContainer2').id = "questionContainerAppear";
  document.getElementById('progress1').id = "progress2";
  document.getElementById('point2').id = "point2Filled";
}

function step2to3(){
  duration = document.getElementById('duration').value;
  document.getElementById('questionContainerAppear').id = "questionContainerDisappear";
  document.getElementById('questionContainer3').id = "questionContainerAppear";
  document.getElementById('progress2').id = "progress3";
  document.getElementById('point3').id = "point3Filled";
}

function step3to4(){
  budget = document.getElementById('budget').value;
  document.getElementById('questionContainerAppear').id = "questionContainerDisappear";
  document.getElementById('questionContainer4').id = "questionContainerAppear";
  document.getElementById('progress3').id = "progress4";
  document.getElementById('point4').id = "point4Filled";
}

function step4to5(){
  peopleCount = document.getElementById('people').value;
  document.getElementById('questionContainerAppear').id = "questionContainerDisappear";
  document.getElementById('questionContainer5').id = "questionContainerAppear";
  document.getElementById('progress4').id = "progress5";
  document.getElementById('point5').id = "point5Filled";
}

function step5toEnd(){
  if(document.getElementById('skillLevel1').checked){
    skillLevel = document.getElementById('skillLevel1').value
  }
  if(document.getElementById('skillLevel2').checked){
    skillLevel = document.getElementById('skillLevel2').value
  }
  if(document.getElementById('skillLevel3').checked){
    skillLevel = document.getElementById('skillLevel3').value
  }
  document.getElementById('summary1').innerHTML = "Airport : " + source;
  document.getElementById('summary2').innerHTML = "Destination : " + duration;
  document.getElementById('summary3').innerHTML = "Budget : " + budget;
  document.getElementById('summary4').innerHTML = "Number of People : " + peopleCount;
  document.getElementById('summary5').innerHTML = "Skill Level : " + skillLevel;

  document.getElementById('questionContainerAppear').id = "questionContainerDisappear";
  document.getElementById('questionContainer6').id = "questionContainerAppear";
}

$(document).ready(function() {
  $('#submitFinal').click(function() {
    $.ajax({
      type: 'POST',
      url: 'submitReview/',
      dataType: 'json',
      data: {'source': source, 'duration': duration, 'budget':budget,
      'noOfPeople': peopleCount, 'skillLevel': skillLevel,
      'windSpeed': windSpeed, 'windDirection': windDirection,
      'temperature': temperature}
    });
  });
});
