import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


link_list = 'https://gist.github.com/paulmillr/2657075'

page = requests.get(link_list)
soup = BeautifulSoup(page.text,'html.parser')

table_lines = soup.find('article', class_='markdown-body entry-content').find('table').find_all('tr')[1::]
links = [t.find('a').text for t in table_lines]

df = pd.DataFrame(links, columns = ['UserName'])
df.to_csv('UserNames.csv', sep = ',')