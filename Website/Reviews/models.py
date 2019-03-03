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
class Review(models.Model):
    source = models.TextField(default="1")
    duration = models.IntegerField(default=2)
    budget = models.IntegerField(default=500)
    noOfPeople = models.IntegerField(default=1)
    skillLevel = models.CharField(choices=skillSelection,max_length=1,default='B')
    windSpeed = models.IntegerField(default=10)
    windDirection = models.CharField(choices=windSelection,max_length=2,default="N")
    temperature = models.IntegerField(default=10)
    # Wind speed, wind direction, temp
