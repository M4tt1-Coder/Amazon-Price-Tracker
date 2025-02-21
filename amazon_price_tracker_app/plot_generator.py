# Create your tests here.
import pandas as pd
from sklearn.linear_model import LinearRegression#errechnet einen wert b um den y erhöht wird wenn sich x um 1 erhöht
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import matplotlib.pyplot as plt
import os
import io
import urllib
import base64
from datetime import datetime, timedelta
from sklearn.pipeline import make_pipeline
import random


plt.style.use("fivethirtyeight")

def generate_price_predictions(initial_date: str, initial_price: float):
    # Generate past 2 months (approximately 60 days) of data for training the model
    past_days = 60
    start_date = datetime.strptime(initial_date, "%d/%m/%Y")
    dates = [start_date - timedelta(days=i) for i in range(past_days)]
    dates.reverse()  # Ensure dates are in chronological order

    # Generate example trend data (this can be replaced with actual historical data if available)
    prices = [initial_price * (1 + 0.01 * np.sin(2 * np.pi * i / 30)) for i in range(past_days)]

    # Prepare the data for the model
    df = pd.DataFrame({'date': dates, 'price': prices})
    df['day'] = df['date'].apply(lambda x: (x - start_date).days)
    
    X = df[['day']]
    y = df['price']

    # Randomly choose between linear regression and polynomial regression
    model_choice = random.choice(['linear', 'polynomial'])
    
    if model_choice == 'linear':
        model = LinearRegression()
    else:
        degree = random.randint(2, 4)  # Choose a polynomial degree between 2 and 4
        model = make_pipeline(PolynomialFeatures(degree), LinearRegression())

    # Fit the model
    model.fit(X, y)

    # Generate predictions for the next 10 days
    future_dates = [start_date + timedelta(days=i+1) for i in range(10)]
    future_days = [(date - start_date).days for date in future_dates]

    predicted_prices = model.predict(np.array(future_days).reshape(-1, 1))
    predicted_prices = [round(price, 2) for price in predicted_prices]

    # Create the result lists
    future_dates_str = [date.strftime("%d/%m/%Y") for date in future_dates]
    result_dates = future_dates_str
    result_prices = predicted_prices

    return result_dates, result_prices

def plot_product_price(products, product_id):
    product = next((p for p in products if p["id"] == product_id), None) # 

    if not product:
        print(f"Produkt '{product_id}' nicht gefunden!")
        return

    # Vorhersage berechnen mit externer Funktion (aus prediction_model_polynomial.py)
    dates, prices = generate_price_predictions(product["date"][0], product["price"][0])

    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, linestyle='dashed',marker='o', color='r', label="Vorhersage")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f"Preisentwicklung für {product_id}")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri =  urllib.parse.quote(string)
    
    return uri
    
excel_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/amazon_product_data.xlsx")
products = []
excel = pd.ExcelFile(excel_path)

for sheet in excel.sheet_names:
    data = pd.read_excel(excel_path, sheet_name=sheet)
    products.append({
        "id": sheet,
        "name": data["name"][0],
        "price": data["price"].tolist(),
        "date": data["date"].tolist()
    })
    
plot_product_price(products, "ID_7e0f17b")