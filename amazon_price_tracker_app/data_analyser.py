import pandas as pd
from random import random

# 2 random values
def get_data_np():      # declare function to test program
    price = random()    # random 'price' value for testing
    date = random()     # random 'date' value for testing
    product = random()     # random 'date' value for testing
    return price, date, product  # return 'price' and 'date' values

def receive_data_np():      # declare function for receiving return values from 'get_data_np()' function
    price, date, product = get_data_np()    # save the two return values of 'get_data_np()' function in 'product', 'date' and 'product'
    data = {'price': [price], 'date': [date], 'product': [product]}  # create a dictionary with your values
    df = pd.DataFrame(data)             # convert to DataFrame
    print(price)                            # print 'price' value in terminal to compare, if it is the same value, that is written into the excel
    print(date)                            # print 'date' value in terminal to compare, if it is the same value, that is written into the excel
    print(product)                            # print 'product' value in terminal to compare, if it is the same value, that is written into the excel
    df.to_excel('output.xlsx', index=False)
receive_data_np()
