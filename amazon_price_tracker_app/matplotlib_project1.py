import pandas as pd
from matplotlib.pyplot import pyplot as plt

plt.style.use("fivethirtyeight") 

data = pd.read_excel ('data1.xlsx')

date = data['Date']
price_1 = data['Product_1']



spaltenname = "Spaltenname"  # Ersetze das mit dem Namen deiner Spalte


if data[spaltenname].isna().all():
    print(f"Die Spalte '{spaltenname}' ist leer.")
else:
    print(f"Die Spalte '{spaltenname}' ist nicht leer.")
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)






ax1.plot(date, price_1, color='#444444', linestyle='--', label='All Devs')
ax2.plot(date, price_2, label='Python' )

plt.title('Amazon-Price-Tracker')

plt.tight_layout()
plt.legend(loc='upper left')
plt.show()

