import matplotlib.pyplot as plt
import io
import urllib
import base64
from .utils import generate_price_predictions

plt.style.use("fivethirtyeight")

def plot_product_price(products, product_id):
    """
    Plots the price development of a product over time.

    Args:
        products (list): List of all products
    """
    
    product = next((p for p in products if p["id"] == product_id), None) # 

    if not product:
        print(f"Produkt '{product_id}' nicht gefunden!")
        return
    # Vorhersage berechnen mit externer Funktion (aus prediction_model_polynomial.py)
    dates, prices = generate_price_predictions(product["date"][(len(product["date"])-1)], product["price"][(len(product["price"])-1)],product["price"],product["date"])
    # is for rendering the plot
    plt.switch_backend("AGG")
    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, linestyle='dashed',marker='o', color='r', label="Vorhersage")
    current_values = plt.gca().get_yticks()
    # all float values should have 2 digits in precision
    plt.gca().set_yticklabels(['{:.2f}'.format(x) for x in current_values])
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    # convert into a 64-base encoded string
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    
    return uri
    