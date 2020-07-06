#handles the structure of data to be converted ultimately to csv files

from bs4 import BeautifulSoup

# find year played
def find_index(rows):
	counter = 0
	ind = []
	for data in rows.find_all('a'):
		for cell in data:
			counter += 1
			if counter % 2 == 1:
				try:
					temp = int(cell)
				except:
					continue
				ind.append(temp)
	return ind

# find number of touchdowns
def find_rectd(rows):
	touchd = []
	for data in rows.find_all('td', {"data-stat":"rec_td"}):
		for cell in data:
			temp = ""
			for bit in str(cell):
				if bit.isnumeric():
					temp += bit
			touchd.append(int(temp))
	return touchd

# find receiving yards
def find_recyards(rows):
	yards = []
	for data in rows.find_all('td', {"data-stat":"rec_yds"}):
		for cell in data:
			temp = ""
			for bit in str(cell):
				if bit.isnumeric():
					temp += bit
			yards.append(int(temp))
	return yards


#find number of games played
def find_games(rows):
	games = []
	for data in rows.find_all('td', {"data-stat":"g"}):
		for cell in data:
			temp = ""
			for bit in str(cell):
				if bit.isnumeric():
					temp += bit
			games.append(int(temp))
	return games

#find number of targets
def find_targets(rows):
	targets = []
	for data in rows.find_all('td', {"data-stat":"targets"}):
		for cell in data:
			temp = ""
			for bit in str(cell):
				if bit.isnumeric():
					temp += bit
			targets.append(int(temp))
	return targets

# find number of receptions 
def find_receptions(rows):
	receptions = []
	for data in rows.find_all('td', {"data-stat":"rec"}):
		for cell in data:
			temp = ""
			for bit in str(cell):
				if bit.isnumeric():
					temp += bit
			receptions.append(int(temp))
	return receptions