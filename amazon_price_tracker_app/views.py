from django.shortcuts import render, HttpResponse
import pandas as pd
from .forms import  urlform

# Create your views here.

# our home page 
def home(request):
    return render(request, 'home.html')


def input(request):
    if request.method == "GET":
        form = urlform(request.GET)
        if form.is_valid():
            url = form.cleaned_data['user_input']
            with open("database/urls.txt", "a") as file:
                file.write(url)
    else: form = urlform()
    with open("database/urls.txt", "r") as txt:
        data = txt.read()

    return render(request, 'input.html',{"form":form})