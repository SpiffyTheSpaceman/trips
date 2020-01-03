from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('trips/', views.TripList.as_view(), name='trips_list'),
   path('trips/<int:trip_id>/', views.trips_detail, name='detail'),
   path('trips/create/', views.TripCreate.as_view(), name='trips_create'),
   path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name='trips_update'),
   path('trips/<int:pk>/delete/', views.TripDelete.as_view(), name='trips_delete'),
   path('trips/<int:trip_id>/add_city/', views.add_city, name='add_city'),
   path('trips/<int:trip_id>/assoc_activity/<int:activity_id>/', views.assoc_activity, name='assoc_activity'),
   path('trips/<int:trip_id>/unassoc_activity/<int:activity_id>/', views.unassoc_activity, name='unassoc_activity'),
   path('trips/<int:city_id>/delete_city/', views.delete_city, name='delete_city'),
   path('activities/', views.ActivityList.as_view(), name='activities_list'),
   path('activities/<int:pk>/', views.ActivityDetail.as_view(), name='activities_detail'),
   path('activities/create/', views.ActivityCreate.as_view(), name='activities_create'),
   path('activities/<int:pk>/update/', views.ActivityUpdate.as_view(), name='activities_update'),
   path('activities/<int:pk>/delete/', views.ActivityDelete.as_view(), name='activities_delete'),
   path('accounts/signup/', views.signup, name='signup'),
]