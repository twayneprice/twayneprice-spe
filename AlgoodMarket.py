from spe import *
from coupons import *
def parseAlgoodMarket1(page):
	import datetime
	import sys
	sys.path.append('./BeautifulSoup-3.2.0')
	from BeautifulSoup import BeautifulSoup
	soup = BeautifulSoup("".join(page))
	for i in soup('div',{ "id" : "offer" }):

		store = "Algood Market"
	   
		pricesValid=""
		startDate=""
		endDate=""
		pricesValidInput = i.find('p')
		if pricesValidInput:
			pricesValid = " ".join(removeNonAscii(pricesValidInput.renderContents()).split())
			startDate = datetime.datetime.now().strftime("%m/%d/%Y").lstrip('0')
			endDate = pricesValid[17:99]

		title=""
		titleInput = i.find('h3')
		if titleInput:
			title = removeNonAscii(titleInput.renderContents())

		description = title

		price = ""
		priceInput = i.find('h1')
		if priceInput:
			price = removeNonAscii(priceInput.renderContents())

		if title:
			print (store+'|'+startDate+'|'+endDate+'|'+title+'|'+description+'|'+price).replace("\r\n"," ")
			addToSales(store,startDate,endDate,title,description,price)
	return
def scrapeAlgoodMarket1():

	import urllib
	f = urllib.urlopen("http://algoodmarket.com/page/sales")
	addPageToDb("AlgoodMarket1",f.read())
	return
def processAlgoodMarket1():
	from datetime import datetime
	from sqlite3 import connect

	rows = getPagesFromDb("AlgoodMarket1")

	for row in rows:
		parseAlgoodMarket1(row[0])
#		setPageAsProcessed(row[1])
	return

