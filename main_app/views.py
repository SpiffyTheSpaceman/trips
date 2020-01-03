from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Trip, City, Activity
from .forms import CityForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Define views here
def home(request):
  return render(request, 'home.html')

def about(request):
   return render(request, 'about.html')

# def trips_index(request):
#    trips = Trip.objects.all()
#    return render(request, 'trips/index.html', { 'trips': trips })
# Class Based view below:
# This will look for a view of main_app/trip_list by default (nameofmodel_list). It can be reassigned here.
class TripList(LoginRequiredMixin, ListView):
   model = Trip

@login_required
def trips_detail(request, trip_id):
   trip = Trip.objects.get(id=trip_id)
   activities_trip_doesnt_have = Activity.objects.exclude(id__in = trip.activities.all().values_list('id'))
   city_form = CityForm()
   return render(request, 'trips/detail.html', { 
      'trip': trip,
      'city_form': city_form,
      'activities': activities_trip_doesnt_have
      })

@login_required
def assoc_activity(request, trip_id, activity_id):
   Trip.objects.get(id=trip_id).activities.add(activity_id)
   return redirect('detail', trip_id=trip_id)

@login_required
def unassoc_activity(request, trip_id, activity_id):
  Trip.objects.get(id=trip_id).activities.remove(activity_id)
  return redirect('detail', trip_id=trip_id)

# This will look for a view of main_app/trip_form by default
class TripCreate(CreateView):
   model = Trip
   fields = ['country', 'start_date', 'end_date']
   def form_valid(self, form):
      # Assign the logged in user (self.request.user)
      form.instance.user = self.request.user  # form.instance is the cat
      # Let the CreateView do its job as usual
      return super().form_valid(form)

# Note: for update and trip we don't have to pass in the id/pk because the class will already know to input that in.
# The CBVs that work with a single model instance automatically pass as part of the context two attributes that are assigned the model instance. The attributes are named object and, in this case, trip (the lowercase name of the Model).
class TripUpdate(LoginRequiredMixin, UpdateView):
  model = Trip
  fields = '__all__'

class TripDelete(LoginRequiredMixin, DeleteView):
  model = Trip
  success_url = '/trips'

def add_city(request, trip_id):
	# create the ModelForm using the data in request.POST
  form = CityForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_city= form.save(commit=False)
    # Note: in the models, we only defined a trip property, not a trip_id property, but django inherently creates a trip_id property for reference key properties that you can use and it will understand.
    new_city.trip_id = trip_id
    new_city.save()
  return redirect('detail', trip_id=trip_id)


def delete_city(request, city_id):
   city = City.objects.get(id=city_id)
   city.delete()
   return redirect('detail', city.trip_id)


class ActivityList(LoginRequiredMixin, ListView):
   model = Activity

class ActivityDetail(LoginRequiredMixin, DetailView):
   model = Activity

class ActivityCreate(LoginRequiredMixin, CreateView):
   model = Activity
   fields = '__all__'

class ActivityUpdate(LoginRequiredMixin, UpdateView):
  model = Activity
  fields = '__all__'

class ActivityDelete(LoginRequiredMixin, DeleteView):
  model = Activity
  success_url = '/activities'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = "Invalid sign up - try again"
  form = UserCreationForm()
  context = { 'form': form, 'error_message': error_message }
  return render(request, 'registration/signup.html', context)