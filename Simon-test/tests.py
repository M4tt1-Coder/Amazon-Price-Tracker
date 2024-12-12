import requests
import bs4 as bs
import lxml
import numpy as np
import pandas as pd
from datetime import datetime


proxy_list=[]
for line in open("proxies.txt","r"):
    proxy_list.append(line.strip())

random_proxy = proxy_list[np.random.randint(len(proxy_list))]
#print(proxy_list)
Url = input("Enter URL: ")
used_proxy = {
    "http":random_proxy,
    "https":random_proxy,
}
header = ({'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
                    'Accept-Language':'en-US,en;q=0.5',
                    'Sec-Fetch-Dest':'document',
                    'Sec-Fetch-Mode':'navigate',
                    'Sec-Fetch-Site':'same-origin',
                    'Sec-Fetch-User':'?1',
                    'Upgrade-Insecure-Requests':'1'})

scrap = requests.get(url=Url,headers=header)
inhalt=scrap.text
print("scraping erfolgreich")

#try:
inhalt_pars = bs.BeautifulSoup(inhalt, features="lxml")
#print(inhalt_pars)
target_price_full= inhalt_pars.find('span', attrs={'class':'a-price-whole'})
target_price_fraction= inhalt_pars.find('span', attrs={'class':'a-price-fraction'})
price = 0
if target_price_full:
    price_full = target_price_full.text
    price_fraction = target_price_fraction.text
    price = price_full + price_fraction
    date = datetime.today().strftime("%d/%m/%Y")
else:
    price = "suche des preises nicht erfolgreich"
print(price,date)




#except Exception as e:
 #   print("fehler ist aufgetreten")

