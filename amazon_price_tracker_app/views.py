from django.shortcuts import render, HttpResponse, redirect
import pandas as pd
from .forms import  urlform
import os
from django.conf import settings
# Create your views here.

# our home page 
def home(request):
    return render(request, 'home.html')

#page for adding and deleting product urls
def create(request):
    data_file_path = os.path.join(#erstellt den absoluten pfad fer datei im djagno verzecihniss data/...
        settings.BASE_DIR,
        "amazon_price_tracker_app/data/urls.txt"
    )
    with open(data_file_path, "r") as txt:
        data = txt.readlines()
    if request.method == "POST":
        form = urlform(request.POST)
        if form.is_valid():
            url = form.cleaned_data['user_input']
            if request.POST.get("submit")=="submit":
                with open(data_file_path, "a") as file:
                    file.write(url+"\n")
                return redirect("create") #update site to show new list
            elif request.POST.get("submit")=="delete":
                with open(data_file_path, "r") as file:
                    lines=file.readlines()
                with open(data_file_path, "w") as write:
                    for line in lines:
                            if line.strip("\n")!=url:
                                write.write(line)
                return redirect("create")#update site to show new list

#todo make the products be showed under each other not in a list
    else: form = urlform()

    return render(request, 'create.html',{"form":form,"products":data})