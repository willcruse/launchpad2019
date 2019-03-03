# Imports
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Reviews.models import Review
from django.core import serializers
from recognition import SpeechRecognition
import json
from APIs import weather, destination, flight
from datetime import date

# Create your views here.


def addReviewPage(request):
    """ Adds the addReview web page """
    context = {}
    return render(request, 'Reviews/addReview.html', context)

def displayReviews(request):
    """ Prints off all of the reviews recieved from the search """
    context = {}
    return render(request, 'Reviews/getReview.html', context)


@csrf_exempt
def incrementUpvote(request):
    """ Upvotes the review, increasing it's value by 1 """
    if request.is_ajax() and request.method == 'POST':
        r = Review.objects.get(pk=request.POST['idd'])
        r.upvotes = r.upvotes+1
        r.save()
        return HttpResponse("hello")

@csrf_exempt
def submitReview(request):
    if request.is_ajax() and request.method == "POST":
        f = Review(source=request.POST["source"],duration=request.POST["duration"],
        budget=request.POST["budget"],noOfPeople=request.POST["noOfPeople"],
        skillLevel=request.POST["skillLevel"],windSpeed=request.POST["windSpeed"],
        windDirection=request.POST["windDirection"],temperature=request.POST["temperature"])
        f.save()
        return HttpResponse("")
    else:
        raise Http404

def getAudio(request):
    """ Runs the speech recognition algorithm, returning the JSON file """
    speech = SpeechRecognition(3,48000)
    speech.takeMicInput()
    speech.convertAudioFile()
    jsonFile = speech.recogniseVoice()
    return HttpResponse(jsonFile, content_type='application/json')

def getDestinations(i):
    destinations = [
          destination([16.538799, -23.041800], "Cape Verde", "SID"),
          destination([-6.135730, 39.362122], "Zanzibar", "ZNZ"),
          destination([-3.682650, -38.737560], "Cumbuco, Brazil", "FOR"),
          destination([-28.016666, 153.399994], "Gold Coast, Australia", "OOL")
    ]
    return destinations[i]


def getWeatherInfo(dest):
    dates = date.today()
    info = weather()
    info.pullWeather(dates, dest)
    return info


def getFlights(i):
    flights = [
      flight(150, 1000, 1200, "SID", "LGW", "Tap Air Portugal", "2019-04-23"),
      flight(160, 800, 1600, "ZNZ", "LHR", "British Airways", "2019-04-23"),
      flight(170, 900, 1500, "FOR", "STN", "KLM", "2019-04-23"),
      flight(180, 1700, 2100, "OOL", "LHR", "British Airways", "2019-04-23"),
      flight(150, 1000, 1200, "LGW", "SID", "Tap Air Portugal", "2019-04-23"),
      flight(160, 800, 1600, "LHR", "ZNZ", "British Airways", "2019-04-23"),
      flight(170, 900, 1500, "STN", "FOR", "KLM", "2019-04-23"),
      flight(180, 1700, 2100, "LHR", "OOL", "British Airways", "2019-04-23")
      ]
    return flights[i]


def getReviews(request):
    validStuff = []
    for i in range(4):
        dest = getDestinations(i)
        w = getWeatherInfo(dest)
        if min(w.windspeed) >= 4.5:
            validStuff.append({
                "name": dest.name,
                "airport": dest.airport,
                "windspeed": min(w.windspeed),
                "temp": min(w.temp)
                })
    return JsonResponse(validStuff,safe=False)
