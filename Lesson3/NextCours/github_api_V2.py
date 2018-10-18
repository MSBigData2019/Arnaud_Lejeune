import numpy as np
import pandas as pd
import requests
import json


df = pd.read_csv('./UserNames.csv', index_col = 0)

file = open("./auth.txt","r")
token = file.read()

temp = []

for user in df['UserName'] :
	count = 0
	moy = 0

	url1 = f'https://api.github.com/users/{user}'
	r1 = requests.get(url1, auth = ('EMBSKD', token))
	js1 = r1.json()

	nb_repos = js1['public_repos']

	for page in range((nb_repos // 100) + 1) :
		url2 = f'https://api.github.com/users/{user}/repos?page={page + 1}&per_page=100'
		r2 = requests.get(url2, auth = ('EMBSKD', token))
		js2 = r2.json()
		for repo in js2 :
			count += repo['stargazers_count']

	if (nb_repos != 0) :
		moy = count/nb_repos
	else :
		moy = 0
	temp.append([user, moy])


users_score = pd.DataFrame(temp, columns = ["User", "Score"])
users_score.to_csv('Results_V2.csv', sep = ',')