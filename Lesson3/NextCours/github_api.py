import numpy as np
import pandas as pd
import requests
import json


df = pd.read_csv('./UserNames.csv', index_col = 0)

file = open("./auth.txt","r")
token = file.read()

temp = []
print(temp)

for user in df['UserName'] :
	url = f'https://api.github.com/users/{user}/repos'
	r = requests.get(url, auth = ('EMBSKD', token))
	js = r.json()

	count = 0
	moy = 0

	for repo in js :
		count += repo['stargazers_count']
	if (len(js) != 0) :
		moy = count/len(js)
	else :
		moy = 0
	temp.append([user, moy])


users_score = pd.DataFrame(temp, columns = ["User", "Score"])
users_score.to_csv('Results.csv', sep = ',')