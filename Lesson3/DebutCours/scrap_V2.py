import requests
from bs4 import BeautifulSoup
import numpy as np

def getAVG(link) :
	pages = ["", "1", "2", "3", "4", "5"]
	reducs = []
	for page in pages :
		pageNum = page
		page = requests.get(link)
		soup = BeautifulSoup(page.text,'html.parser')
		remises = soup.find_all('p', class_='darty_prix_barre_remise darty_small separator_top')
		reducs += [float(remise.text[2:-1]) for remise in remises]
	return sum(reducs)/len(reducs)

def getAll(marques):
	pageNum = ""
	marque = "hp"
	for m in marques :
		marque = m
		link = f'https://www.darty.com/nav/achat/informatique/ordinateur_portable/portable/marque_{pageNum}_{marque}__{marque.upper()}.html'
		print('Moyenne des soldes de ' + marque + ' : ' + str(getAVG(link)))


marques = ['hp', 'dell']
getAll(marques)