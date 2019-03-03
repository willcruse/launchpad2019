# Imports
from django.shortcuts import render
from django.http import HttpResponse
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

def getReviews(request, l):
    """ Returns a JSON file of all of the relevant reviews, returning them
        If none are found in the intial search, then each word is searched individually
        If still nothing is found, then "No Data" is returned"""
    if request.is_ajax():
        found = False
        results = Review.objects.filter(location=l).order_by('-upvotes','-datePosted')
        if len(results) == 0:
            wordsInSearch = l.split(" ")
            for word in wordsInSearch:
                results = Review.objects.filter(location=word).order_by('-upvotes','-datePosted')
                if len(results) > 0:
                    found = True
                    break
        else:
            found = True
        if found:
            data = serializers.serialize("json", results)
        else:
            data = {'return':"No Data"}
            data = json.dumps(data)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404

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
    pullWeather(dates, dest)


def getFlights():
    pass
