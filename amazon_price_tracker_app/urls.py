from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
# TODO - Databases are not neccessary -> we get the data on runtime from the API

urlpatterns = [
    path('', views.home, name="home"),
    path("input", views.input, name="input")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)#this is neccessary for implementing external files like css files etc.