from django.urls import path
from . import views

# TODO - Databases are not neccessary -> we get the data on runtime from the API

urlpatterns = [
    path('/', views.home, name="home")
]