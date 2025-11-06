from django.urls import path
from . import views
app_name = 'reservation'
urlpatterns = [
    path('reserv/', views.reserv, name='reserv'),
]