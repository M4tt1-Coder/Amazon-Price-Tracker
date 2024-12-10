import requests
import bs4 as bs
import lxml

Url = input("Enter URL: ")
scrap = requests.get(Url)
inhalt=scrap.content
print("scraping erfolgreich")

#try:
inhalt_pars = bs.BeautifulSoup(inhalt, features="lxml")#
target_price= inhalt_pars.find('span', attrs={'class':'a-price-whole'})
price = 0
if target_price is not None:
    price = target_price.text
else:
    price = "suche des preises nicht erfolgreich"
print(price)




#except Exception as e:
 #   print("fehler ist aufgetreten")

