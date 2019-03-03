# Imports
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Reviews.models import Review
from django.core import serializers
import json

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
        HttpResponseNotFound('<h1>Page not found</h1>')

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
    """ Submits the review to the database as a POST request """
    if request.is_ajax() and request.method == 'POST':
        r = Review(author=request.POST['author'],location=request.POST['location'],reviewText=request.POST['review'])#,datePosted=datetime.date.today())
        r.save()
        return HttpResponse("")
    else:
        raise Http404
