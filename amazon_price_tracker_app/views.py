from django.shortcuts import render, HttpResponse

# Create your views here.

# our home page 
def home(request):
    return render(request, 'home.html')