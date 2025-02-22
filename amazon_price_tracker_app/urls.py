from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# Defined routes for the app
urlpatterns = [
    path('', views.home, name="home"),
    path("create", views.create, name="create"),
    path('dashboard/<str:product_id>/', views.dashboard, name="dashboard"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)#this is neccessary for implementing external files like css files etc.