from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# NBA season we will be analyzing
team = input('Enter Team: ')
# URL page we will scraping (see image above)
url = "https://www.basketball-reference.com/teams/{}/2019_games.html".format(team)

# this is the HTML from the given URL
html = urlopen(url)
soup = BeautifulSoup(html,features="html.parser")

# use findALL() to get the column headers
soup.findAll('tr', limit=2)
# use getText()to extract the text we need into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

# exclude the first column as we will not need
# the ranking order from Basketball Reference for the analysis
#headers = headers[1:]
headers = ['Date','Start','n0','BoxScore','n1','Opponent','Result','n2','TeamScore','OppScore','W','L','Streak','Notes']
# avoid the first header row
rows = soup.findAll('tr')[1:]
team_game = [[td.getText() for td in rows[i].findAll('td')]for i in range(len(rows))]
game_log = pd.DataFrame(team_game, columns = headers)

path_exp = r'/Users/GiampaPietro/Desktop/NBA_Analysis/TeamReview_S2019/data/GameLog_{}_2019.csv'.format(team)
export_csv = game_log.to_csv (path_exp, index = None, header=True, sep='\t')
print('!!!!   DONE   !!!!')
