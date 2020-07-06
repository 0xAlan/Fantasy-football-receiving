#Please create folder "playerfiles".  There will be many csv files created
#Also, please make sure beautifulsoup is installed

import pandas as pd
import numpy as np
import statistics
import re
import requests
from bs4 import BeautifulSoup
from fields import *
from playerlist import *

playerdata = playerList()

listlen = len(playerdata)
for i in range(listlen):

	# construct hyperlink for individual player

	urlbase = "https://www.pro-football-reference.com/players/"
	firstletter = playerdata.loc[i]['hyperlink'][0]
	hyperlink = playerdata.loc[i]['hyperlink']
	url = urlbase + firstletter + "/" + hyperlink + ".htm"
	filename_ = "playerfiles/" + playerdata.loc[i]["file name"] + str(i) + ".csv"
	page = requests.get(url)

	soup = BeautifulSoup(page.text,'html.parser')

	rows = soup.find('tbody')

	ind = find_index(rows) # year played
	touchd = find_rectd(rows) # touchdowns
	yards = find_recyards(rows) # receiving yards
	games = find_games(rows) # games
	targets = find_targets(rows) # targets
	receptions = find_receptions(rows) # receptions n 


	data = {"Year": ind, "Games played": games,"Targets" : targets, "Rec" : receptions,"Yds" : yards, "TD" : touchd}

	# check if all vectors are the same length, before they are combined into data frame
	lens = [len(ind),len(games), len(targets), len(receptions), len(yards), len(touchd)]

	if np.std(lens) != 0:
		continue

	#print(url)
	df = pd.DataFrame(data)
	df.to_csv(filename_)