from spe import *
from coupons import *
def parseBaldwin1(page):
	import urllib
	import datetime
	import sys
	sys.path.append('./BeautifulSoup-3.2.0')
	from BeautifulSoup import BeautifulSoup
	soup = BeautifulSoup("".join(page))
	select = soup.find('select',{ "id" : "Manufacturer" })
	option_tags = select.findAll('option')
	option_tags = option_tags[1:]
	for option in option_tags:
		f = urllib.urlopen('http://catalog.baldwinfilter.com/LoadModels.asp?Vehicleref=3&Manufacturer='+option['value'])
		addPageToDb("Baldwin2",f.read())
		print 'http://catalog.baldwinfilter.com/LoadModels.asp?Vehicleref=3&Manufacturer='+option['value']
	
	return
def parseBaldwin2(page):
	import urllib
	import datetime
	import sys
	sys.path.append('./BeautifulSoup-3.2.0')
	from BeautifulSoup import BeautifulSoup
	soup = BeautifulSoup("".join(page))
	mfg = soup.find(attrs={"name":'txtManufacturer'})['value']
	models = soup.find('select',{ "id" : "Model" })
	option_tags = models.findAll('option')
	option_tags = option_tags[1:]
	for option in option_tags:
		f = urllib.urlopen('http://catalog.baldwinfilter.com/LoadDescriptions.asp?Vehicleref=3&Manufacturer='+mfg+'&Make=&Model=TT'+option['value'])
		addPageToDb("Baldwin3",f.read())
		print option['value']
	return
def scrapeBaldwin1():

	import urllib
	f = urllib.urlopen("http://catalog.baldwinfilter.com/LoadManufacturers.asp?VehicleRef=3&Manufacturer=")
	addPageToDb("Baldwin1",f.read())
	return
def processBaldwin1():
	from datetime import datetime
	from sqlite3 import connect

	rows = getPagesFromDb("Baldwin1")

	for row in rows:
		parseBaldwin1(row[0])
		setPageAsProcessed(row[1])
	return
def processBaldwin2():
	from datetime import datetime
	from sqlite3 import connect

	rows = getPagesFromDb("Baldwin2")

	for row in rows:
		parseBaldwin2(row[0])
		setPageAsProcessed(row[1])
	return

