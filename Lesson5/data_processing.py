import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('cleaned_data.csv', sep = ",", index_col = 0)

col = ['EFFECTIFS','HONORAIRES','DEPASSEMENTS']

departement = data.groupby(['DEPARTEMENT'])[col].sum()
specialites = data.groupby(['SPECIALITE'])[col].sum()

departement['RATIO_DEPASSEMENT'] = departement['DEPASSEMENTS'] / (departement['DEPASSEMENTS'] + departement['HONORAIRES'])
specialites['RATIO_DEPASSEMENT'] = specialites['DEPASSEMENTS'] / (specialites['DEPASSEMENTS'] + specialites['HONORAIRES'])

population = pd.read_csv('cleaned_population.csv', index_col = 0)

departement = pd.merge(departement, population, on = 'DEPARTEMENT', left_index=True, right_index=False)

departement['DENSITE_MED'] = departement['EFFECTIFS'] / departement['POPULATION']

def plot(input, output):
	X = departement[[input]]
	Y = departement[[output]]
	reg = LinearRegression(fit_intercept = True).fit(X, Y)
	coef = reg.coef_[0]
	R2 = reg.score(X,Y)
	df = pd.DataFrame(index = departement.index)
	df[str(input)] = X
	df[str(output)] = Y
	df['LinearRegression'] = reg.intercept_ + coef * X

	ax = df.plot(x = input, y = output, marker = 'o', linewidth= 0 ,  color = 'slategrey', legend = False)
	
	df.plot(x = input, y = 'LinearRegression',  color = 'firebrick', ax=ax, legend = True)
	ax.text(0.25, 0.85, 'R2 = ' + str(R2), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
	plt.show()

def OLS(inputs, output):
	X = departement[input]
	Y = departement[output]
	reg = LinearRegression(fit_intercept = True).fit(X, Y)
	print("Score : " + str(reg.score(X,Y)))
	print("Coeffs : " + str(reg.coef_))

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
	ax4 = departement.plot(x = 'DENSITE_MED', y = 'RATIO_DEPASSEMENT', marker = 'o', linewidth= 0 ,  color = 'darkorange')
	plt.show()


def plot_4():
	inputs = ['POPULATION']
	output = ['EFFECTIFS']
	ax5 = departement.plot(x = 'POPULATION', y = 'EFFECTIFS', marker = 'o', linewidth = 0, color = 'slategrey')
	plt.show()
	OLS(inputs, output)


