import requests
import bs4 as bs
import numpy as np
from datetime import datetime
import json
import hashlib

def get_data_np(Url):
    response = requests.get(Url)
    if response.status_code == 200:
        text = response.text
        data=json.loads(text)
        price=data["price"]
        name=data["title"]
        description=data["description"]
        id=f"ID_{hashlib.sha256(Url.encode()).hexdigest()[:7]}"
        date=datetime.today().strftime("%d/%m/%Y")
    else:
        return "An error occurred"

    return price,date,name,description,id


def get_date_wp(Url):
    """
    This function uses proxies, maby usefull if scraping normally is not functioning.
    But amazon does sometimes recognize these proxies to be malicious so try to use the other function first

    [ Unused ]

    Args:
        Url (str): URL from the API endpoint to fetch from.
    """
    proxy_list = []
    for line in open("../get_productdata_function/proxies.txt", "r"):
        proxy_list.append(line.strip())

    random_proxy = proxy_list[np.random.randint(len(proxy_list))]
    # print(proxy_list)
    used_proxy = {
        "http": random_proxy,
        "https": random_proxy,
    }
    header = ({
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
        'Accept-Language': 'en-US,en;q=0.5',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1'})
    scrap = requests.get(url=Url, headers=header,proxies=used_proxy)
    inhalt = scrap.text
    #print("scraping erfolgreich")

    # try:
    inhalt_pars = bs.BeautifulSoup(inhalt, features="lxml")
    # print(inhalt_pars)
    target_price_full = inhalt_pars.find('span', attrs={'class': 'a-price-whole'})
    target_price_fraction = inhalt_pars.find('span', attrs={'class': 'a-price-fraction'})
    price = 0
    if target_price_full:
        price_full = target_price_full.text
        price_fraction = target_price_fraction.text
        price = price_full + price_fraction
        date = datetime.today().strftime("%d/%m/%Y")
    else:
        price = "suche des preises nicht erfolgreich"
        date = None
    return price, date
