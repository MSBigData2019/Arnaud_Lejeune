import pandas as pd
import numpy as np
import re

def DataMedecin():
	#  --- Import des 2 feuilles csv ---
	spe = pd.read_csv('Specialistes.csv', sep = ",", header = 0)
	gen = pd.read_csv('Generalistes.csv', sep = ",", header = 0)

		# Renommage des premieres colonnes de chaque df
	spe = spe.rename(columns={'Spécialistes': 'SPECIALITE'})
	gen = gen.rename(columns={'Généralistes et compétences MEP': 'SPECIALITE'})
		
		# Fusion des 2 df
	data = spe.append(gen)

	print(data.shape)

	#  --- Cleaning du DataFrame---
	data_cleaned = data.copy()

		# Valeurs non renseignees
	data_cleaned = data_cleaned.replace('nc', np.NaN)
		# Lignes TOTAL par specialitees
	data_cleaned['SPECIALITE'] = data_cleaned['SPECIALITE'].replace(to_replace = r'TOTAL(.*)', value = np.NaN, regex = True)
		# Lignes TOTAL par departement
	data_cleaned['DEPARTEMENT'] = data_cleaned['DEPARTEMENT'].replace(to_replace = r'TOTAL(.*)', value = np.NaN, regex = True)
		# Lignes aux effectifs = 0
	data_cleaned['EFFECTIFS'] = data_cleaned['EFFECTIFS'].replace(to_replace = '0', value = np.NaN)
		# Suppression des lignes 'selectionnes' precedemment
	data_cleaned = data_cleaned.dropna(axis = 0, how = 'any')

	print(data_cleaned.shape)


	# --- Renommage des colonnes utilisees ensuite, puis passage en int---
	data_cleaned = data_cleaned.rename(columns={'HONORAIRES SANS DEPASSEMENT (Euros)': 'HONORAIRES', 'DEPASSEMENTS (Euros)': 'DEPASSEMENTS'})
	data_cleaned['EFFECTIFS'] = pd.to_numeric(data_cleaned['EFFECTIFS'].replace({r'\s': ''}, regex=True))
	data_cleaned['HONORAIRES'] = pd.to_numeric(data_cleaned['HONORAIRES'].replace({r'\s': ''}, regex=True))
	data_cleaned['DEPASSEMENTS'] = pd.to_numeric(data_cleaned['DEPASSEMENTS'].replace({r'\s': ''}, regex=True))
	# --- Export ---
	data_cleaned.to_csv('cleaned_data.csv')

def DataPopulation() :
	temp = pd.read_csv('population.csv', sep = ",", header = None)
	population = pd.DataFrame(columns = ['DEPARTEMENT', 'POPULATION'])
	population['DEPARTEMENT'] = temp[0] + "- " + temp[1]
	population['POPULATION'] = temp[2]
	population['POPULATION'] = pd.to_numeric(population['POPULATION'].replace({r'\s': ''}, regex=True))
	population.to_csv('cleaned_population.csv')
