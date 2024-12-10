import requests
import bs4 as bs
import lxml

Url = input("Enter URL: ")
header = ({'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0',
                    'Accept-Language':'en-US,en;q=0.5',
                    'Sec-Fetch-Dest':'document',
                    'Sec-Fetch-Mode':'navigate',
                    'Sec-Fetch-Site':'same-origin',
                    'Sec-Fetch-User':'?1',
                    'Upgrade-Insecure-Requests':'1'})
scrap = requests.get(Url,headers=header)
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
else:
    price = "suche des preises nicht erfolgreich"
print(price)




#except Exception as e:
 #   print("fehler ist aufgetreten")

