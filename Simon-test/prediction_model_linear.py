import pandas as pd
from sklearn.linear_model import LinearRegression#errechnet einen wert b um den y erhöht wird wenn sich x um 1 erhöht
from sklearn.preprocessing import PolynomialFeatures
import openpyxl
import numpy as np

data = pd.read_excel('test_data.xlsx')#daten einlesen
x_d= data["Date"]
y_d= data["Price"]

x=[]
y=[]
x_new=[]
weigth =[]
#wandelt die in x_d/x_y übergebenen tuples in arrays um
for items in x_d:
    x.append(items)
for items in y_d:
    y.append(items)
#füllt den neuen array mit (in dem fall) den folgenden jahren um so vorhersagen für die zukunft machen zu können
for items in x_d:
    x_new.append(items+len(x))
x=np.array(x).reshape(-1,1)#convertiert den array in einen zweidimensionalen array

#füllt einen array mit der gewichtung der einzelnen einträge in x. dabei soll der älteste eintrag die niedrigse und der neueste die höchste geiwchtung haben
for i in range(0,len(x)):
    weigth.append(i+1)
x_new=np.array(x_new).reshape(-1,1)
print(x_new)

model = LinearRegression()#erstellt ein modell das nachher für die vorhersage benutzt wird

model.fit(x,y,sample_weight=weigth)# passt das modell auf unser datenset an

prediction = model.predict(x_new) # multipliziert den wert den wir von unserem model als "steigung" bekommen und addiert einen wert der vom moddel als basiswert errechnet wurde

print(prediction)

dict_pred = {}
for i in range(0,len(x_new)-1):
    dict_pred[int(x_new[i][0])] = float(prediction[i])#typecast da numpy einen eigenen datentyp hat dessen name sonst mit ausgegeben wird

print(dict_pred)
