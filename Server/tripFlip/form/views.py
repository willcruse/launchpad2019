from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template import loader


from .models import TravelForm
# Create your views here.
def form(request):
        template = loader.get_template('form/index.html')
        return HttpResponse(template.render())

@csrf_exempt
def submitForm(request):
    if request.is_ajax() and request.method == "POST":
        f = Form(source=request.POST["source"],duration=request.POST["duration"],
        budget=request.POST["budget"],noOfPeople=request.POST["noOfPeople"],
        skillLevel=request.POST["skillLevel"],windSpeed=request.POST["windSpeed"],
        windDirection=request.POST["windDirection"],temperature=request.POST["temperature"])
        f.save()
        return HttpResponse("Submitted")
    else:
        raise Http404
