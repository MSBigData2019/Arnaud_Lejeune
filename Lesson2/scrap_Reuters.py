import requests
from bs4 import BeautifulSoup


link_LVMH = 'https://www.reuters.com/finance/stocks/financial-highlights/LVMH.PA'
link_Airbus = 'https://www.reuters.com/finance/stocks/financial-highlights/AIR.PA'
link_Danone = 'https://www.reuters.com/finance/stocks/financial-highlights/DANO.PA'
links = [link_LVMH, link_Airbus, link_Danone]

Companies = ["LVMH", "Airbus", "Danone"]

"""
	Returns [# of Estimates	, Mean , High , Low , 1 Year Ago]
"""
def getQ4Data(soup):
	stripes = soup.find_all(class_='stripe')
	QuarterDiv = stripes[0]
	QuarterDiv_Raw_Data = QuarterDiv.find_all('td')[1::]
	Q4Data = [data.text for data in QuarterDiv_Raw_Data]
	for i in range(len(Q4Data)):
		if Q4Data[i] != "--" :		#Other cases might be added if site not consistent 
			Q4Data[i] = float(Q4Data[i].replace(',',''))

	return Q4Data

"""
	Returns [Action price , currency , last price change]
"""
def getAction(soup):
	header = soup.find("div", {"id": "headerQuoteContainer"})
	""" --- Action Price --- """
	action_spans = header.find(class_="sectionQuote nasdaqChange").find_all('span')[1:3:]
	action = [float(action_spans[0].text), action_spans[1].text] #[action_price, currency]

	""" --- Price Change --- """
	change_spans = header.find(class_="sectionQuote priceChange").find(class_="valueContent").find_all('span')[0].text
	selectedChar = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
	temp = ""
	for car in change_spans:
		if car in selectedChar:
			temp+=car
	if temp.strip() == "" :
		temp = "--"
	else :
		temp = float(temp)
	change = [temp]
	return action + change

"""
	Returns percentage of shares hold by institutional holders
"""
def getPercentageOfShares(soup):
	module_stripe = soup.find(class_="column2 gridPanel grid4").find_all(class_="module")[3].find(class_="stripe")
	percentage = module_stripe.find(class_="data").text
	return percentage

"""
	Returns percentage of shares hold by institutional holders
"""
def getDividend(soup):
	stripe = soup.find_all(class_="stripe")[9]
	data = stripe.find_all(class_="data")
	dividend = [float(d.text) for d in data]
	return dividend

def main():
	for i in range(3) :
		page = requests.get(links[i])
		soup = BeautifulSoup(page.text,'html.parser')

		print("- - - - - " + Companies[i] + " - - - - -")

		print("\t --- Q4 Financial Results ---")
		print("\t \t" + str(getQ4Data(soup)))

		print("\t --- Action Price ---")
		print("\t \t" + str(getAction(soup)))

		print("\t --- Percentage of Share hold by institutional holders ---")
		print("\t \t" + str(getPercentageOfShares(soup)))

		print("\t --- Dividend Yield ---")
		print("\t \t" + str(getDividend(soup)))

		print("- - - - - - - - - - - - - - - - - -" + "\n")

main()