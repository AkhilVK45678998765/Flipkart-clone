from django.urls import path

from .views import *




urlpatterns = [
    path('index/',index),
    path('login/',login),
    path('register/',register),
    path('flipkartprofile/',flipkartprofile),
    path('contact/',contact),
    path('navbar/',navbar)



]