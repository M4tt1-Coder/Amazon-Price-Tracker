import pandas as pd
from random import random
import hashlib
import os
from get_productdata import get_data_np

# function for testing
#def get_data_np():
#    price = random()  # random price
#    date = random()   # random date
#    product = f"Product_{int(random() * 3)}"  # random product name (3 products for simulation)
#    return price, date, product

def receive_data_np(url,file):
    # declare variables for the return values of 'get_data_np()'
    price, date, product = get_data_np(url)
    
    # hash 'product' variable
    hash = f"ID_{hashlib.sha256(product.encode()).hexdigest()[:7]}"
    
    # declare excel file name 
    file_name = file
    
    # check if excel 'amazon_product_data.xlsx' in variable 'file_name' exists
    file_exists = os.path.exists(file_name)
    
    # create DataFrame
    new_data = pd.DataFrame([[price, date, product]], columns=['price', 'date', 'product'])

    # if variable 'file_exists' is true
    if file_exists:
        # reading data of 'file_name'
        excel_data = pd.ExcelFile(file_name)
        # if there is already a 'hash' variable written in a excel sheet-name
        if hash in excel_data.sheet_names:
            # read 'file_name' with the already existing 'hash' variable
            existing_data = pd.read_excel(file_name, sheet_name=hash)
            # add 'updated_data' to 'existing_data'
            updated_data = pd.concat([existing_data, new_data], ignore_index=True)
        # if there's no 'hash' variable written in a excel sheet-name
        else:
            # create new sheet with new data
            updated_data = new_data

    # if variable 'file_exists' is false
    else:
        # create new sheet with new data
        updated_data = new_data
        with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
            # write hash value into first excel sheet
            new_data.to_excel(writer, index=False, sheet_name=hash)
        print(f"Created new excel file '{file_name}'")
        print(f"price: {price}, date: {date}, product: {product}, sheet-name: {hash}")
        return

    # write data in excel
    with pd.ExcelWriter(file_name, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
        updated_data.to_excel(writer, index=False, sheet_name=hash)
    print(f"price: {price}, date: {date}, product: {product}, sheet-name: {hash}")
    
# call function for testing
# receive_data_np()
# receive_data_np()
# receive_data_np()
