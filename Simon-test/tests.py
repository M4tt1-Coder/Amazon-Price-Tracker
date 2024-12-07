import requests
import bs4 as bs
import lxml

Url = input("Enter URL: ")
scrap = requests.get(Url)
if scrap.status_code == 200:
    inhalt=scrap.text
    print("scraping erfolgreich")
else:
    print("error")
    exit()
#try:
inhalt_pars = bs.BeautifulSoup(inhalt, features="lxml")
target_price_full= inhalt_pars.find("span", attrs={"class": "a-price-whole"})
price_full = target_price_full.get_text()
target_price_fraction = inhalt_pars.find("span", attrs={"class": "a-price-fraction"})
price_fraction = target_price_fraction.get_text()
print(target_price_fraction)
price=price_full+price_fraction


print(price)

#except Exception as e:
 #   print("fehler ist aufgetreten")

