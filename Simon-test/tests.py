import requests
import bs4 as bs
import lxml
import numpy as np
import pandas as pd
from datetime import datetime
import json


def get_data_np(Url):
    response = requests.get(Url)
    if response.status_code == 200:
        text = response.text
        data=json.loads(text)
        price=data["price"]
        name=data["title"]
        date=datetime.today().strftime("%d/%m/%Y")
    else:
        return "An error occurred"


    return price,date,name


test=get_data_np("https://fakestoreapi.com/products/1")
print(test)


#except Exception as e:
 #   print("fehler ist aufgetreten")

