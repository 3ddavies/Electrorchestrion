import requests
from bs4 import BeautifulSoup
import csv

url = ('https://en.wikipedia.org/wiki/List_of_pipe_organ_stops')

page= requests.get(url).content
soup = BeautifulSoup(page, "html.parser")
table = soup.find('table')

f = csv.writer(open("OrganStopScrape.csv", "w"))

f.writerow(["Stop name", "Alternative name", "Type", "Note"])
# variable to check length of rows
x = (len(table.findAll('tr')) - 1)
# set to run through x
for row in table.findAll('tr')[1:x]:
	col = row.findAll('td')
	name = col[0].getText().replace("\n", "")
	altnames = col[1].getText().replace("\n", "").split()
	musicalfam = col[2].getText().replace("\n", "")
	note = col[3].getText().replace("\n", "").replace('"'. '\\"')
	print('"' + name + '": [', altnames, ', "' + musicalfam + '", "' + note + '"],')