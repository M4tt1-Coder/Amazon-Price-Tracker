import pandas as pd
from random import random

# 2 random values
def get_data_np():      # declare function to test program
    price = random()    # random 'price' value for testing
    date = random()     # random 'date' value for testing
    return price, date  # return 'price' and 'date' values

def receive_data_np():      # declare function for receiving return values from 'get_data_np()' function
    p, d = get_data_np()    # save the two return values of 'get_data_np()' function in 'p' and 'd' 

    data = {'price': [p], 'date': [d]}  # create a dictionary with your values
    df = pd.DataFrame(data)             # convert to DataFrame
    print(p)                            # print 'p' value in terminal to compare, if it is the same value, that is written into the excel
    print(d)                            # print 'd' value in terminal to compare, if it is the same value, that is written into the excel
    df.to_excel('output.xlsx', index=False)
receive_data_np()
