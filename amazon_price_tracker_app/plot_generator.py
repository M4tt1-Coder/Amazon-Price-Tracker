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
    print(products)
    # Vorhersage berechnen mit externer Funktion (aus prediction_model_polynomial.py)
    dates, prices = generate_price_predictions(products["date"][-1], products["price"][-1],products["price"],products["date"])
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
    