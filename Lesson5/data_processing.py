import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

data = pd.read_csv('cleaned_data.csv', sep = ",", index_col = 0)

col = ['EFFECTIFS','HONORAIRES','DEPASSEMENTS']

departement = data.groupby(['DEPARTEMENT'])[col].sum()
specialites = data.groupby(['SPECIALITE'])[col].sum()

departement['RATIO'] = departement['DEPASSEMENTS'] / (departement['DEPASSEMENTS'] + departement['HONORAIRES'])
specialites['RATIO'] = specialites['DEPASSEMENTS'] / (specialites['DEPASSEMENTS'] + specialites['HONORAIRES'])


ax1 = departement.plot(x = 'EFFECTIFS', y = 'RATIO', marker = 'o', linewidth= 0 ,  color = 'cornflowerblue')
ax1.set_title("% de depassement fonction de l'effectif du departement")

ax2 = specialites.plot(x = 'EFFECTIFS', y = 'RATIO', marker = 'o', linewidth= 0 ,  color = 'firebrick')
ax2.set_title("% de depassement fonction de l'effectif de la specialites")

plt.show()