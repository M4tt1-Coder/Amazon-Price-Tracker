import openpyxl
import pandas as pd
import hashlib
from .get_productdata import *
from .data_analyser import *
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
            #todo delete sheet from excel
                wb = load_workbook(excel_file_path)
                print(f"---------------------------------------------{wb}----------------------------------------")
                wb.remove(wb[hash])
                wb.save(excel_file_path)
                return redirect("create")  # update site to show new list


    else:
        form = urlform()

    return render(request, "create.html", {"form": form, "products": data})


# our home page

