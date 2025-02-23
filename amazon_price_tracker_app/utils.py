import os
import pandas as pd 
from django.conf import settings 
from datetime import datetime, timedelta
from sklearn.pipeline import make_pipeline
import random
from sklearn.linear_model import LinearRegression#errechnet einen wert b um den y erhöht wird wenn sich x um 1 erhöht
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

def get_product_by_id(id):
    """
    Uses the id of the product to get the product from the excel file.
    
    Args:
        id (str): ID of the product

    Returns:
        Product: Product object with the ID of the product
    """
    excel_file_path = os.path.join(settings.BASE_DIR, "amazon_price_tracker_app/data/amazon_product_data.xlsx")
    try:
        excel = pd.ExcelFile(excel_file_path)
        if id in excel.sheet_names:
            sheet = pd.read_excel(excel_file_path, sheet_name=id)
            product = {
                "id": id,
                "name": sheet["name"][0],
                "description": sheet.get("description", ["No description"])[0],
                "price": sheet["price"],
                "date": sheet["date"]
            }    
            return product
        else:
            return f"Product with ID {id} was not found."
    except Exception as e:
        print(f"Error reading Excel file : {str(e)}")
        return None

def get_all_products() -> list:
    """
    Fetches all products from the Excel file.

    Returns:
        list: All products from the Excel file
    """
    excel_file_path = os.path.join(settings.BASE_DIR, "amazon_price_tracker_app/data/amazon_product_data.xlsx")
    all_products = []
    try:
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
        return all_products
    except Exception as e:
        print(f"Error reading Excel file: {str(e)}")
        return []
    
def generate_price_predictions(initial_date: str, initial_price: float, prices_list, dates_list):
    """
    Uses a model to generate price predictions for the given date and price.
    
    Returns a list of prices for the given date and price.

    Args:
        initial_date (str): The starting date of the initial price
        initial_price (float): Starting price
        prices_list: list of historic prices
        dates_list: list of historical dates

    Returns:
        list: Dates for the predictions, and corresponding predicted prices
    """
    # Generate past 2 months (approximately 60 days) of data for training the model if no data is available
    past_days = 60
    start_date = datetime.strptime(initial_date, "%d/%m/%Y")
    dates_pred = [start_date - timedelta(days=i) for i in range(past_days)]
    dates_pred.reverse()  # Ensure dates are in chronological order

    # Generate example trend data
    prices_pred = [initial_price * (1 + 0.01 * np.sin(2 * np.pi * i / 30)) for i in range(past_days)]
    #checks if there is a sufficient amount of historical data (if not uses the generated data from above)
    if(len(prices_list)<=1):
        prices=prices_pred
        dates=dates_pred
    else:
        dates=[]
        for i in range(len(dates_list)):
            dates.append(datetime.strptime(dates_list[i], "%d/%m/%Y"))
        prices=prices_list
        print(dates, prices)

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