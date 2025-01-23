from django.shortcuts import render, HttpResponse, redirect
import pandas as pd
from .forms import  urlform
import os
from django.conf import settings

# Create your views here.


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


    else: form = urlform()

    return render(request, 'create.html',{"form":form,"products":data})

# our home page 
def home(request):
    return render(request, 'home.html')
    # store comparison information in session -> https://docs.djangoproject.com/en/5.1/topics/http/sessions/
    # TODO - Add the comparison feature
    comparison_product_ids = []
    if 'compared_products' in request.session:
        comparison_product_ids = request.session['compared_products']
    else:
        request.session['compared_products'] = []
    # Mock data for dashboard page
    # mock data test data
    mock_products = [
        {'id': 'be81a713-523d-46e1-a4c2-1b52e3f53604', 'name': 'Product 1', 'description': 'Some Product 1', 'price': 1.99},
        {'id': 'be81a713-523d-46e1-a4c2-2b52e3f53604', 'name': 'Product 2', 'description': 'Some Product 2', 'price': 34.99},
        {'id': 'be81a713-523d-46e1-a4c2-3b52e3f53604', 'name': 'Product 3', 'description': 'Some Product 3', 'price': 13.59},
        {'id': 'be81a713-523d-46e1-a4c2-4b52e3f53604', 'name': 'Product 4', 'description': 'Some Product 4', 'price': 345.99},
        {'id': 'be81a713-523d-46e1-a4c2-5b52e3f53604', 'name': 'Product 5', 'description': 'Some Product 5', 'price': 23.00},
        {'id': 'be81a713-523d-46e1-a4c2-6b52e3f53604', 'name': 'Product 6', 'description': 'Some Product 6', 'price': 3.99},
        {'id': 'be81a713-523d-46e1-a4c2-7b52e3f53604', 'name': 'Product 7', 'description': 'Some Product 7', 'price': 7.49},
    ]
    context = {
        'products': mock_products,
        'compared_product_ids': comparison_product_ids
    }
    return render(request, 'home.html', context)

# TODO - Finish the dashboard page
def dashboard(request, product_id):
    # TODO - Include // Finish the 'get_product' function
    # product = get_product(product_id)
    product = {'id': 4, 'name': 'Product 4', 'description': 'Some Product 4', 'price': 345.99}
    context = {
        'product': product
    }
    return render(request, 'dashboard.html', context)
