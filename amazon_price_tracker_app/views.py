from django.shortcuts import render, redirect

# import pandas as pd
from .forms import urlform
import os
from django.conf import settings

# Create your views here.


# page for adding and deleting product urls
def create(request):
    data_file_path = os.path.join(  # erstellt den absoluten pfad fer datei im djagno verzecihniss data/...
        settings.BASE_DIR, "amazon_price_tracker_app/data/urls.txt"
    )
    with open(data_file_path, "r") as txt:
        data = txt.readlines()
    if request.method == "POST":
        form = urlform(request.POST)
        if form.is_valid():
            url = form.cleaned_data["user_input"]
            if request.POST.get("submit") == "submit":
                print('Add a new URL')
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
                return redirect("create")  # update site to show new list

    # todo make the products be showed under each other not in a list
    else:
        form = urlform()

    return render(request, "create.html", {"form": form, "products": data})


# our home page
def home(request):
    # store comparison information in session -> https://docs.djangoproject.com/en/5.1/topics/http/sessions/

    # Set a empty list of product ids
    comparison_product_ids = []
    # if there are already some product ids in the session, load them into the comparison_product_ids list
    if "compared_products_ids" in request.session:
        comparison_product_ids = request.session["compared_products_ids"]
    else: # ... or create a new session
        request.session["compared_products_ids"] = []
    
    # when a POST request is made
    if request.method == "POST":
        # when the user added a new product
        if request.POST.get('action_operation').split('|')[1] == 'ADD':
            # get the product id from the form data and add it to the comparison_product_ids list
            product_id = request.POST.get('action_operation').split('|')[0]
            comparison_product_ids.append(product_id)
            # apply the comparison_product_ids to the new session
            request.session["compared_products_ids"] = comparison_product_ids
        # when the user deleted a product
        elif request.POST.get('action_operation').split('|')[1] == 'DELETE': 
            # get the product id from the form data
            product_id = request.POST.get('action_operation').split('|')[0]
            # remove the product from the comparison_product_ids list and reassign the comparison_product_ids to the new session
            if product_id in request.session["compared_products_ids"]:
                comparison_product_ids = []
                for id in request.session["compared_products_ids"]:
                    if id != product_id:
                        comparison_product_ids.append(id)
                request.session["compared_products_ids"] = comparison_product_ids
        return redirect("home")  # update site to show new comparison list
    

    # check if more than 3 products have been compared
    # it is not allowed to compare more than 3 products
    to_many_compared_products = len(comparison_product_ids) > 3

    # Mock data for dashboard page
    # mock data test data
    # TODO - Remove this when we are finished
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

    # TODO - Implement the getProducts function to fetch products from a data source (API, database, etc.).
    # products that are not compared
    product_not_selected = []
    # products = getProducts()
    # get the products that the user wants to compare
    products_to_compare = []
    print(to_many_compared_products)
    for product in mock_products:
        if not to_many_compared_products:
            for product_id in comparison_product_ids:
                if product['id'] == product_id:
                    products_to_compare.append(product)
            if product['id'] not in comparison_product_ids:
                product_not_selected.append(product)   
        else:
            request.session['compared_products_ids'] = []
            return redirect('home')
    # add and remove forms
    # cmp_form = ModifyProdCmpListForm()
    
    # set page context
    context = {
        "products_not_selected": product_not_selected,
        "products": mock_products,
        "compared_products": products_to_compare,
        "to_many_compared_products": to_many_compared_products,
        # "cmp_form": cmp_form, # the add_cmp_form for adding a product to the compare list // the remove_cmp_form for removing a product
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
    # product = get_product(product_id)
    mock_product = {
        "id": 4,
        "name": "Product 4",
        "description": "Some Product 4",
        "price": 345.99,
    }
    context = {"product": mock_product}
    return render(request, "dashboard.html", context)
