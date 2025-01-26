import openpyxl
import pandas as pd
import hashlib
from get_productdata import get_data_np
from django.shortcuts import render, redirect

from openpyxl import load_workbook
from .forms import urlform
import os
from django.conf import settings

# Create your views here.


# page for adding and deleting product urls
def create(request):
    data_file_path = os.path.join(  # erstellt den absoluten pfad fer datei im djagno verzeichniss data/...
        settings.BASE_DIR, "amazon_price_tracker_app/data/urls.txt"
    )
    excel_file_path = os.path.join( settings.BASE_DIR, "amazon_price_tracker_app/data/amazon_product_data.xlsx")
    with open(data_file_path, "r") as txt:
        data = txt.readlines()
    if request.method == "POST":
        form = urlform(request.POST)
        if form.is_valid():
            url = form.cleaned_data["user_input"]
            price, date, product = get_data_np(url)
            hash = f"ID_{hashlib.sha256(product.encode()).hexdigest()[:7]}"
            if request.POST.get("submit") == "submit":
                with open(data_file_path, "a") as file:
                    file.write(url + "\n")
                return redirect("create")  # update site to show new list
            elif request.POST.get("submit") == "delete":
                with open(data_file_path, "r") as file:
                    lines = file.readlines()
                with open(data_file_path, "w") as write:
                    for line in lines:
                        if line.strip("\n") != url:
                            write.write(line)
            #todo delete sheet from excel
                with openpyxl.load_workbook(excel_file_path) as excel:
                    excel.remove(hash)

                return redirect("create")  # update site to show new list


    else:
        form = urlform()

    return render(request, "create.html", {"form": form, "products": data})


# our home page
def home(request):
    # store comparison information in session -> https://docs.djangoproject.com/en/5.1/topics/http/sessions/
    # TODO - Add the comparison feature
    comparison_product_ids = []
    if "compared_products" in request.session:
        comparison_product_ids = request.session["compared_products"]
    else:
        request.session["compared_products"] = []

    # check if more than 3 products have been compared
    # it is not allowed to compare more than 3 products
    to_many_compared_products = len(comparison_product_ids) > 3

        

    # Mock data for dashboard page
    # mock data test data
    mock_products = [
        {
            "id": "be81a713-523d-46e1-a4c2-1b52e3f53604",
            "name": "Product 1",
            "description": "Some Product 1",
            "price": 1.99,
        },
        {
            "id": "be81a713-523d-46e1-a4c2-2b52e3f53604",
            "name": "Product 2",
            "description": "Some Product 2",
            "price": 34.99,
        },
        {
            "id": "be81a713-523d-46e1-a4c2-3b52e3f53604",
            "name": "Product 3",
            "description": "Some Product 3",
            "price": 13.59,
        },
        {
            "id": "be81a713-523d-46e1-a4c2-4b52e3f53604",
            "name": "Product 4",
            "description": "Some Product 4",
            "price": 345.99,
        },
        {
            "id": "be81a713-523d-46e1-a4c2-5b52e3f53604",
            "name": "Product 5",
            "description": "Some Product 5",
            "price": 23.00,
        },
        {
            "id": "be81a713-523d-46e1-a4c2-6b52e3f53604",
            "name": "Product 6",
            "description": "Some Product 6",
            "price": 3.99,
        },
        {
            "id": "be81a713-523d-46e1-a4c2-7b52e3f53604",
            "name": "Product 7",
            "description": "Some Product 7",
            "price": 7.49,
        },
    ]

    # TODO - Implement the getProducts function to fetch products from a data source (API, database, etc.)
    # products that are not compared
    product_not_selected = []
    # products = getProducts()
    # get the products that the user wants to compare
    products_to_compare = []
    for product in mock_products:
        for product_id in comparison_product_ids:
            if product['id'] == product_id:
                products_to_compare.append(product)
                break  # stop searching if the product is found to avoid duplicates
        product_not_selected.append(product)
        
    # set page context
    context = {
        "products_not_selected": product_not_selected,
        "products": mock_products,
        "compared_products": products_to_compare,
        "to_many_compared_products": to_many_compared_products,
    }
    return render(request, "home.html", context)


# TODO - Finish the dashboard page


def dashboard(request, product_id):
    """
    Entrypoint for the dashboard page.

    Args:
        request: The HTTP request object.
        product_id: The ID of the product to be included in the dashboard.
    """
    # TODO - Include // Finish the 'get_product' function
    # product = get_product(product_id)
    mock_product = {
        "id": 4,
        "name": "Product 4",
        "description": "Some Product 4",
        "price": 345.99,
    }
    context = {"product": mock_product}
    return render(request, "dashboard.html", context)
