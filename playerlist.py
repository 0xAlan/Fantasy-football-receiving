#Downloads a list of players and returns links for respective players with at least one reception


import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

def playerList():
	url = "https://www.pro-football-reference.com/years/2019/receiving.htm"

	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')

	rows = soup.find('tbody')


	names = []
	link = []
	filenames = []
	for links in rows.find_all('td', {"data-stat":"player"}):
		names.append(links['csk'])
		link.append(links["data-append-csv"])
		temp = links['csk'].split(',')
		filenames.append(temp[1] + temp[0])


	playerlistlinks = {'player': names, 'hyperlink': link, 'file name': filenames}

	playerdf = pd.DataFrame(playerlistlinks)

	return playerdf