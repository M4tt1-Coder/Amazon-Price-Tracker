import pandas as pd
import matplotlib.pyplot as plt
from utils import get_all_products
import os
import io
import urllib
import base64

plt.style.use("fivethirtyeight")

def read_excel_data(file_path):
    return pd.read_excel(file_path, sheet_name=None) #Liest die Excel-Datei und gibt ein Dictionary mit Tabellen als DataFrames zurück

def plot_product_price(data, product_name): #Plottet die Preisentwicklung eines einzelnen Produkts
    # if product_name not in data:
    #     print(f"Produkt '{product_name}' nicht gefunden!")
    #     return
    df = {}
    print(product_name)
    for product in data:
        print(product)
        if product["id"] == product_name:
            df = product


 
    #df = data[product_name]
   
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['price'], marker='o', linestyle='-', label=product_name)
    plt.xlabel("Datum")
    plt.ylabel("Preis")
    plt.title(f"Preisentwicklung für {product_name}")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    #fig = plt.gcf()
    #buf = io.BytesIO()
    #fig.savefig(buf,format='png')
    #buf.seek(0)
    #string = base64.b64encode(buf.read())
    #uri =  urllib.parse.quote(string)
    
    #return uri # Rückgabe des Bild URLs als Base64-encoded PNG-Bild
excel_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/amazon_product_data.xlsx")
all_products = []
excel = pd.ExcelFile(excel_file_path)
for sheet_name in excel.sheet_names:
    
    sheet = pd.read_excel(excel_file_path, sheet_name=sheet_name)

    product = {
        "id": sheet_name,
        "name": sheet["name"][0],
        "description": sheet.get("description", ["No description"])[0],
        "price": sheet["price"].iloc[-1],
        "date": sheet["date"][0]
    }
    all_products.append(product)
plot_product_price(all_products, "ID_7e0f17b")
print(all_products)