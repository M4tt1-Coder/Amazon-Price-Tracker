import requests
import bs4 as bs
import lxml

Url = input("Enter URL: ")
header = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
scrap = requests.get(Url,headers=header)
inhalt=scrap.content
print("scraping erfolgreich")

#try:
inhalt_pars = bs.BeautifulSoup(inhalt, features="lxml")#
target_price_full= inhalt_pars.find('span', attrs={'class':'a-price-whole'})
target_price_fraction= inhalt_pars.find('span', attrs={'class':'a-price-fraction'})
price = 0
if target_price_full is not None:
    price_full = target_price_full.text
    price_fraction = target_price_fraction.text
    price = price_full + price_fraction
else:
    price = "suche des preises nicht erfolgreich"
print(price)




#except Exception as e:
 #   print("fehler ist aufgetreten")

