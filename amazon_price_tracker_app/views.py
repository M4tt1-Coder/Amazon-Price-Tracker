import hashlib
from .get_productdata import get_data_np
from .data_analyser import delete_all_products, receive_data_np, delete_excel_sheet
from django.shortcuts import render, redirect

from openpyxl import load_workbook
from .forms import urlform
import os
from django.conf import settings

# Create your views here.

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


# page for adding and deleting product urls
def create(request):
    data_file_path = os.path.join(  # erstellt den absoluten pfad fer datei im djagno verzeichniss data/...
        settings.BASE_DIR, "amazon_price_tracker_app/data/urls.txt"
    )
    excel_file_path = os.path.join( settings.BASE_DIR, "amazon_price_tracker_app/data/amazon_product_data.xlsx")
    expected = "https://fakestoreapi.com/"
    flag=False
    products=[]
    for lines in open(data_file_path):
        products.append(get_data_np(lines)[2])
    with open(data_file_path, "r") as file:
        urls=file.readlines()
    data =[]
    for i in range(len(products)):
        data.append({"url":urls[i],"product": products[i]})
    #print(data)

    if request.method == "POST":
        form = urlform(request.POST)
        if form.is_valid():
            url = form.cleaned_data["user_input"]
            if url[:len(expected)] == expected:  # checks if the input starts with the correct url for our API
                price, date, product, describtion, id = get_data_np(url)
                hash = f"ID_{hashlib.sha256(product.encode()).hexdigest()[:7]}"
                if request.POST.get("submit") == "submit":#if "add" button is clicked open the txt in append mode and write the url in
                    with open(data_file_path, "a") as file:
                        file.write(url + "\n")
                    receive_data_np(url, excel_file_path)
                    return redirect("create")  # update site to show new list
                elif request.POST.get("submit") == "delete":#if "delete" button is clicked delete the line
                    with open(data_file_path, "r") as file:
                        lines = file.readlines()
                    with open(data_file_path, "w") as write:
                        for line in lines:
                            if line.strip("\n") != url:
                                write.write(line)
                    wb = load_workbook(excel_file_path)
                    wb.remove(wb[hash])
                    wb.save(excel_file_path)
                    return redirect("create")  # update site to show new list
            else:
                flag=True #sets a flag that we then can use to trigger a response in the template
                if request.method == "POST" and "go_back" in request.POST:#checks if user has clicked the back butten
                    flag=False
                    return redirect("create") #resets the page

    else:
        form = urlform()

    return render(request, "create.html", {"form": form, "products": data,"flag":flag})


# our home page
def home(request):
    """
    Manages the home page where all products can be deleted.
    
    Products can be compared and examined in the dashboard by clicking on a redirecting button.
    
    Args:
        request (Django HTTP Request Object): HTTP request object

    Returns:
        Context and UI data that is displayed in the viewport
    """
    # TODO - Implement the getProducts function to fetch products from a data source (API, database, etc.).
    # get all current products
    products = mock_products
    # Set a empty list of product ids
    comparison_product_ids = []
    # if there are already some product ids in the session, load them into the comparison_product_ids list
    if "compared_products_ids" in request.session:
        comparison_product_ids = request.session["compared_products_ids"]
    else: # ... or create a new session
        request.session["compared_products_ids"] = []
    
    # when a POST request is made
    if request.method == "POST":
        # delete all the products
        if request.POST.get('action_operation') == "DELETE_ALL":
            # remove all the products from the comparison_product_ids list and reassign the comparison_product_ids to the new session
            comparison_product_ids = []
            request.session["compared_products_ids"] = comparison_product_ids
            # clear the excel file
            # amazon_price_tracker_app/data/amazon_product_data.xlsx
            delete_all_products(os.path.join(settings.BASE_DIR, 'amazon_price_tracker_app/data/amazon_product_data.xlsx'))
            # clear the urls textfile
            url_file_path = os.path.join(  # erstellt den absoluten pfad fer datei im djagno verzeichniss data/...
                settings.BASE_DIR, "amazon_price_tracker_app/data/urls.txt"
            )
            with open(url_file_path, "w") as url_txt:
                url_txt.truncate()
            return redirect("home")  # update site to show the empty comparison list
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
    
    # products that are not compared
    product_not_selected = []
    # products = getProducts()
    # get the products that the user wants to compare
    products_to_compare = []
    for product in products:
        if not to_many_compared_products:
            for product_id in comparison_product_ids:
                if product['id'] == product_id:
                    # TODO - Fetch the price development chart string for this product
                    products_to_compare.append({"product": product, "chart_string": ""})
            if product['id'] not in comparison_product_ids:
                product_not_selected.append(product)   
        else:
            request.session['compared_products_ids'] = []
            return redirect('home')
    
    # get the price development charts
    
    # set page context
    context = {
        "products_not_selected": product_not_selected,
        "products": products,
        "compared_products": products_to_compare,
        "to_many_compared_products": to_many_compared_products,
    }
    return render(request, "home.html", context)

def dashboard(request, product_id: str):
    """
    Entrypoint for the dashboard page.

    Args:
        request: The HTTP request object.
        product_id: The ID of the product to be included in the dashboard.
    """
    # TODO - Fetch the product from the excel file
    # product = get_product(product_id)
    mock_product = {
        "id": 4,
        "name": "Product 4",
        "description": "Easy upgrade for faster boot up, shutdown, application load and response (As compared to 5400 RPM SATA 2.5” hard drive; Based on published specifications and internal benchmarking tests using PCMark vantage scores) Boosts burst write performance, making it ideal for typical PC workloads The perfect balance of performance and reliability Read/write speeds of up to 535MB/s/450MB/s (Based on internal testing; Performance may vary depending upon drive capacity, host device, OS and application.)",
        "price": 345.99,
        "date": "2015-01-01T00:00:00"
    }
    product = mock_product
    
    # TODO - Also add here the product plot chart string function
    context = {"product": product, "prod_plot_string": ""}
    return render(request, "dashboard.html", context)
