import requests
from bs4 import BeautifulSoup

keyword = 'Macron'
titles = []

for i in range(50) :
	pageNum = str(i)
	link = f'https://www.lemonde.fr/recherche/?keywords={keyword}&page_num={pageNum}&operator=and&exclude_keywords=&qt=recherche_texte_titre&author=&period=since_1944&start_day=01&start_month=01&start_year=1944&end_day=06&end_month=10&end_year=2018&sort=desc'

	page = requests.get(link)

	soup = BeautifulSoup(page.text,'html.parser')

	#print(soup.prettify())

	articles = soup.find_all(class_='grid_12 alpha enrichi mgt8')
	h3 = [article.find('h3', class_='txt4_120') for article in articles]
	a = [div.find_all('a') for div in h3]

	titles_temp = [x[0].text for x in a]
	titles.append(titles_temp)

for j in titles:
	print(j)
