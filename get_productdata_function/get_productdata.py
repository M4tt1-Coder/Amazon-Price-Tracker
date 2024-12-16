import requests
import bs4 as bs
import lxml
import numpy as np
import pandas as pd
from datetime import datetime


def get_data_np(Url):
    header = ({
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
        'Accept-Language': 'en-US,en;q=0.5',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1'})

    scrap = requests.get(url=Url, headers=header)
    inhalt = scrap.text
    #print("scraping erfolgreich")

    # try:
    inhalt_pars = bs.BeautifulSoup(inhalt, features="lxml")
    # print(inhalt_pars)
    target_price_full = inhalt_pars.find('span', attrs={'class': 'a-price-whole'})
    target_price_fraction = inhalt_pars.find('span', attrs={'class': 'a-price-fraction'})
    target_product_name = inhalt_pars.find('span', attrs={"id":"productTitle",'class': 'a-size-large product-title-word-break'})
    price = 0
    if target_price_full:
        price_full = target_price_full.text
        price_fraction = target_price_fraction.text
        product_name = target_product_name.text
        price = price_full + price_fraction
        date = datetime.today().strftime("%d/%m/%Y")
    else:
        price = "suche des preises nicht erfolgreich"
        date = None
        product_name = None
    return price,date,product_name


#this function uses proxies, maby usefull ich scraping normally ist not functioning.
#But amazon does sometimes recognize these proxies to be malicious so try to use the other function first
def get_date_wp(Url):
    proxy_list = []
    for line in open("proxies.txt", "r"):
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
