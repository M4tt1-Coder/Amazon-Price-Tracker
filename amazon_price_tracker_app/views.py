import hashlib
from .utils import get_all_products, get_product_by_id
from .get_productdata import get_data_np
from .data_analyser import delete_all_products, receive_data_np, delete_excel_sheet
from .plot_generator import plot_product_price
from django.shortcuts import render, redirect
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
                price, date, product, description, id = get_data_np(url)
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
                    delete_excel_sheet(excel_file_path,id)
                    return redirect("create")
            else:
                flag=True #sets a flag that we then can use to trigger a response in the template
                if request.method == "POST" and "go_back" in request.POST:#checks if user has clicked the back butten
                    flag=False
                    return redirect("create") #resets the page
    else:
        form = urlform()
    # butten next to the list that lets you delete products instantly
    if request.method == "POST" and "delete_product" in request.POST:
        value=request.POST.get("delete_product")
        value=value.strip()#nexessary cause django adds a whitespace after the link which leads to a different id etc.
        id1 = f"ID_{hashlib.sha256(value.encode()).hexdigest()[:7]}"
        #print("...")
        #print(value,"----------------------------------")
        with open(data_file_path, "r") as file:#usual delete functionality
            lines = file.readlines()
        #print(lines)
        with open(data_file_path, "w") as write:
            for line in lines:
                if line.strip() != value:
                    #print(line.strip("\n"))
                    write.write(line)
        #print("test")
        delete_excel_sheet(excel_file_path,id1)
        return redirect("create")
    return render(request, "create.html", {"form": form, "products": data, "flag": flag})


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

    """ 
    #updates the tracker with the newest price
    products = get_all_products()
    for lines in open(os.path.join(settings.BASE_DIR, "amazon_price_tracker_app/data/urls.txt"),"r"):
        receive_data_np(lines.strip(),os.path.join(settings.BASE_DIR, 'amazon_price_tracker_app/data/amazon_product_data.xlsx'))
    """
    # get all current products with the update
    products = get_all_products()
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
    # check if more than 2 products have been compared
    # it is not allowed to compare more than 2 products
    to_many_compared_products = len(comparison_product_ids) > 2

    # products that are not compared
    product_not_selected = []
    # products = getProducts()
    # get the products that the user wants to compare
    products_to_compare = []
    for product in products:
        if not to_many_compared_products:
            for product_id in comparison_product_ids:
                if product['id'] == product_id:
                    products_to_compare.append({"product": product, "chart_string": plot_product_price(products, product_id)})
            if product['id'] not in comparison_product_ids:
                product_not_selected.append(product)   
        else:
            request.session['compared_products_ids'] = []
            return redirect('home')
    # get the price development charts
    # set page context
    for i in range(len(products)):
        products[i]['price'] = products[i]['price'][len(products[i]["price"])-1]
        products[i]['date'] = products[i]['date'][len(products[i]["date"])-1]
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
    product_initial = get_product_by_id(product_id)
    product = {
        "id": id,
        "name": product_initial["name"],
        "description": product_initial["description"],
        "price": product_initial["price"][0],
        "date": product_initial["date"][0],
    }
    context = {"product": product, "prod_plot_string": plot_product_price(get_all_products(), product_id)}
    return render(request, "dashboard.html", context)
