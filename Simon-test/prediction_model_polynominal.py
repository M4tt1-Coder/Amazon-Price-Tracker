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

#np.array(y).reshape(-1,1)
print(y)
#füllt den neuen array mit (in dem fall) den folgenden jahren um so vorhersagen für die zukunft machen zu können
for items in x_d:
    x_new.append(items+len(x))

#---------------------------------------------------------------------------
#degree =
poly = PolynomialFeatures(degree = 2)
poly_features = poly.fit_transform(np.array(x).reshape(-1,1))#wir brauchen einen zweidimensionalen array bei dem in der 2. splate die x werte ^^2 sind um uns so an ein polynom anzunähern
print(poly_features)
poly_predict = poly.fit_transform(np.array(x_new).reshape(-1,1))

model = LinearRegression()#erstellt ein modell das nachher für die vorhersage benutzt wird

model.fit(poly_features,y)# passt das modell auf unser datenset an jetzt aber mit unseren angepassten x-Werten

prediction = model.predict(poly_features) # multipliziert den wert den wir von unserem model als "steigung" bekommen und addiert einen wert der vom moddel als basiswert errechnet wurde


print(prediction)