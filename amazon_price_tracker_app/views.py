from django.shortcuts import render, HttpResponse
import pandas as pd
from .forms import  urlform
import os
from django.conf import settings
# Create your views here.

# our home page 
def home(request):
    return render(request, 'home.html')


def input(request):
    data_file_path = os.path.join(#erstellt den absoluten pfad fer datei im djagno verzecihniss data/...
        settings.BASE_DIR,
        "amazon_price_tracker_app/data/urls.txt"
    )
    if request.method == "POST":
        form = urlform(request.POST)
        if form.is_valid():
            url = form.cleaned_data['user_input']
            if request.POST.get("action")=="submit":
                with open(data_file_path, "a") as file:
                    file.write(url+"\n")
            elif request.POST.get("action")=="delete":
                with open(data_file_path, "w") as file:
                    for line in file:
                        if line!=url:
                            file.write(line)


    else: form = urlform()
    with open(data_file_path, "r+") as txt:
        data = txt.read()

    return render(request, 'input.html',{"form":form,"products":data})