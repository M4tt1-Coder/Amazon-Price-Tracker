import pandas as pd
from random import random

# 2 random values
def get_data_np():  # declare function to test program
    price = random()      # random 'price' value for testing
    date = random()       # random 'date' value for testing
    product = random()    # random 'product' value for testing
    return price, date, product

def receive_data_np():  
    # declare variables for the return values of 'get_data_np()'
    price, date, product = get_data_np()  

    # create DataFrame with columns
    product_data = pd.DataFrame([[price, date, product]], columns=['price', 'date', 'product'])

    try:
        # load existing 'product_data.xlsx'
        header = pd.read_excel('amazon_product_data.xlsx')
    except FileNotFoundError:
        # if 'product_data.xlsx' doesn't exist start with new DataFrame
        header = pd.DataFrame(columns=['price', 'date', 'product'])

    # add row to existing excel
    updated_data = pd.concat([header, product_data], ignore_index=True)

    # write 'updated_data' into excel
    updated_data.to_excel('amazon_product_data.xlsx', index=False, engine='openpyxl')

    # terimnal output
    print("new files were added successfully:")
    print(f"price: {price}, date: {date}, product: {product}")

# test function
receive_data_np()
receive_data_np()
receive_data_np()