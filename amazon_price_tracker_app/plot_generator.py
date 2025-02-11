import pandas as pd
import matplotlib.pyplot as plt
import io
import urllib
import base64

plt.style.use("fivethirtyeight")

def read_excel_data(file_path):
    return pd.read_excel(file_path, sheet_name=None) #Liest die Excel-Datei und gibt ein Dictionary mit Tabellen als DataFrames zurück

def plot_product_price(data, product_name): #Plottet die Preisentwicklung eines einzelnen Produkts
    if product_name not in data:
        print(f"Produkt '{product_name}' nicht gefunden!")
        return
    
    df = data[product_name]
   
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Price'], marker='o', linestyle='-', label=product_name)
    plt.xlabel("Datum")
    plt.ylabel("Preis")
    plt.title(f"Preisentwicklung für {product_name}")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    # plt.show()
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    
    return uri # Rückgabe des Bild URLs als Base64-encoded PNG-Bild

