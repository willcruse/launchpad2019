from django.db import models

skillSelection = (('B', "Beginner"),
                  ('I', "Intermediate"),
                  ('A', "Advanced"))

windSelection = (("N","North"),
                 ("NE", "North East"),
                 ("E", "East"),
                 ("SE", "South East"),
                 ("S", "South"),
                 ("SW","South West"),
                 ("W","West"),
                 ("NW","North West"))


# Create your models here.
class TravelForm(models.Model):
    source = models.TextField()
    duration = models.IntegerField(default=2)
    budget = models.IntegerField(default=500)
    noOfPeople = models.IntegerField(default=1)
    skillLevel = models.CharField(choices=skillSelection,max_length=1)
    windSpeed = models.IntegerField()
    windDirection = models.CharField(choices=windSelection,max_length=2)
    temperature = models.IntegerField()
    # Wind speed, wind direction, temp
