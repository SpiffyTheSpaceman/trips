from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Activity(models.Model):
   activity = models.CharField(default='', max_length=100)
   

   def __str__(self):
      return f'{self.activity}'

   # Add this method. This will redirect to the named 'detail' url and input in the self.id as the trip_id param.
   # The reverse function builds a path string. The above will return the correct path for the detail named route. However, since that route requires a trip_id route parameter, its value must provided as a shown above.
   def get_absolute_url(self):
      return reverse('activities_detail', kwargs={'pk': self.id})


class Trip(models.Model):
   country = models.CharField(default='', max_length=100)
   start_date = models.DateField(default=date.today)
   end_date = models.DateField(default=date.today)
   activities = models.ManyToManyField(Activity)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   

   def __str__(self):
      return f'{self.city} {self.id}'

   # Add this method. This will redirect to the named 'detail' url and input in the self.id as the trip_id param.
   # The reverse function builds a path string. The above will return the correct path for the detail named route. However, since that route requires a trip_id route parameter, its value must provided as a shown above.
   def get_absolute_url(self):
      return reverse('detail', kwargs={'trip_id': self.id})



class City(models.Model):
   city = models.CharField(default='', max_length=100)
   attractions = models.TextField(default='', max_length=500)
   foods = models.TextField(default='', max_length=500)
   trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

   def __str__(self):
      return f"{self.city}"

  # change the default sort
   class Meta:
      ordering = ['-city']

