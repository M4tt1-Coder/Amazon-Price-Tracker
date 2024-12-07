import requests
import bs4 as bs
import lxml

Url ="https://www.amazon.de/Edelstahlkette-langgliedrig-%C3%A4hnlich-DIN763-Meter/dp/B07Z96FR8N?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=25KG0EIKCAM7C&dib=eyJ2IjoiMSJ9.mVbN-QEoe_syptOIlx_bnkQTn48sW5Zy-Opq1vA9fKiTjPVKdJVmoh4_z4on526fslUCPLZIWi7fdsSRpjDekvY_69Fr_X4-abZ_ubcakfWsYOVcnFGkJBQZdZ4kjdZjCua5RyXJvlusGa-L7rAwXFyA3jW2ElmWCbCNOee-RZTQ7gJymaznN8fty1wDfSXdebQDmwLsYeXq2H2OfsVLGxNkT4QrCYZEyEm3C6D7zNQSXICPjVCXuHOhDvPqVD1acCK11SfiMqPBU8a19Zru6BWzRn4PKv4RQwsJDIM9_Tc.0ZD0ufATMp9zaAWrE-iSQOz_dydQ6naJ5hgfGcTalvs&dib_tag=se&keywords=ketten&qid=1733481248&sprefix=ketten%2Caps%2C141&sr=8-9"
scrap = requests.get(Url)
if scrap.status_code == 200:
    inhalt=scrap.text
    print("scraping erfolgreich")
else:
    print("error")
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

