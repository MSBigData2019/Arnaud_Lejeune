import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

data = pd.read_csv('cleaned_data.csv', sep = ",", index_col = 0)

col = ['EFFECTIFS','HONORAIRES','DEPASSEMENTS']

departement = data.groupby(['DEPARTEMENT'])[col].sum()
specialites = data.groupby(['SPECIALITE'])[col].sum()

departement['RATIO_DEPASSEMENT'] = departement['DEPASSEMENTS'] / (departement['DEPASSEMENTS'] + departement['HONORAIRES'])
specialites['RATIO_DEPASSEMENT'] = specialites['DEPASSEMENTS'] / (specialites['DEPASSEMENTS'] + specialites['HONORAIRES'])

population = pd.read_csv('cleaned_population.csv', index_col = 0)

departement = pd.merge(departement, population, on = 'DEPARTEMENT', left_index=True, right_index=False)

departement['RATIO_EFFECTIF_POP'] = departement['EFFECTIFS'] / departement['POPULATION']

def plot_1():
	ax1 = departement.plot(x = 'EFFECTIFS', y = 'RATIO_DEPASSEMENT', marker = 'o', linewidth= 0 ,  color = 'cornflowerblue')
	ax1.set_title("% de depassement fonction de l'effectif du departement")

	ax2 = specialites.plot(x = 'EFFECTIFS', y = 'RATIO_DEPASSEMENT', marker = 'o', linewidth= 0 ,  color = 'firebrick')
	ax2.set_title("% de depassement fonction de l'effectif de la specialites")

	plt.show()


def plot_2():
	ax3 = departement.plot(x = 'POPULATION', y = 'RATIO_DEPASSEMENT', marker = 'o', linewidth= 0 ,  color = 'forestgreen')
	plt.show()


def plot_3():
	ax4 = departement.plot(x = 'RATIO_EFFECTIF_POP', y = 'RATIO_DEPASSEMENT', marker = 'o', linewidth= 0 ,  color = 'darkorange')
	plt.show()