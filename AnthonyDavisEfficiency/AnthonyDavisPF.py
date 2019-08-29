from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

#######################################
#######################################
# Tag # Name             # Player Tag #
#######################################
#  0  # Anthony Davis    # davisan02  #
#  1  # Kevin Garnett    # garneke01  #
#  2  # Tim Duncan       # duncati01  #
#  3  # Charles Barkley  # barklch01  #
#  4  # Dirk Nowitzki    # nowitdi01  # 
#######################################
#######################################

# Necessary Arrays
Players = ["AnthonyDavis","KevinGarnett","TimDuncan","CharlesBarkley","DirkNowitzki"]
PlayersName = ["Anthony Davis", "Kevin Garnett","Tim Duncan","Charles Barkley","Dirk Nowitzki"]
PlayerTag = ["davisan02", "garneke01","duncati01","barklch01","nowitdi01"]
PlayerTagL = ['d','g','d','b','n']

plr_points = []
plr_age = []
plr_rebounds = []
plr_minutes = []
plr_offeff = []
plr_rebeff = []
loop = 0

for plr in range(5):

    #Print Info
    print(PlayersName[loop])
    
    # URL page we will scraping (see image above)
    url = "https://www.basketball-reference.com/players/"+PlayerTagL[plr]+"/"+PlayerTag[plr]+".html"

    # this is the HTML from the given URL
    html = urlopen(url)
    soup = BeautifulSoup(html,features="html.parser")
    
    # use findALL() to get the column headers
    soup.findAll('tr', limit=2)
    # use getText()to extract the text we need into a list
    headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

    # exclude the first column as we will not need 
    # the ranking order from Basketball Reference for the analysis
    headers = headers[1:]

    # avoid the first header row
    rows = soup.findAll('tr')
    player_stats = [[td.getText() for td in rows[i].findAll('td')]for i in range(len(rows))]
    stats = pd.DataFrame(player_stats, columns = headers)
    points = stats['PTS']
    points = pd.to_numeric(points, downcast='float')
    plr_points.append(points)
    age = stats['Age']
    age = pd.to_numeric(age, downcast='float')
    plr_age.append(age)
    minutes = stats['MP']
    minutes = pd.to_numeric(minutes, downcast='float')
    plr_minutes.append(minutes)

    rebounds = stats['TRB']
    rebounds = pd.to_numeric(rebounds, downcast='float')
    plr_rebounds.append(rebounds)

    offeff = np.divide(points,minutes)
    rebeff = np.divide(rebounds,minutes)
    plr_offeff.append(offeff)
    plr_rebeff.append(rebeff)
    #plt.plot(plr_age[loop],plr_rebeff[loop],'-',label=PlayersName[loop])
    loop += 1

plt.plot(plr_age[0],plr_offeff[0],'-',label=PlayersName[0])
plt.plot(plr_age[1],plr_offeff[1],'-',label=PlayersName[1])
plt.plot(plr_age[2],plr_offeff[2],'-',label=PlayersName[2])
plt.plot(plr_age[3],plr_offeff[3],'-',label=PlayersName[3])
plt.plot(plr_age[4],plr_offeff[4],'-',label=PlayersName[4])
plt.xlabel('Age [Years]')
plt.ylabel('Points / Minute')
plt.xlim(0,0.5)
plt.legend()
plt.grid(True)
plt.show()

plt.plot(plr_age[0],plr_rebeff[0],'-',label=PlayersName[0])
plt.plot(plr_age[1],plr_rebeff[1],'-',label=PlayersName[1])
plt.plot(plr_age[2],plr_rebeff[2],'-',label=PlayersName[2])
plt.plot(plr_age[3],plr_rebeff[3],'-',label=PlayersName[3])
plt.plot(plr_age[4],plr_rebeff[4],'-',label=PlayersName[4])
plt.xlabel('Age [Years]')
plt.ylabel('Points / Minute')
plt.xlim(0,0.5)
plt.legend()
plt.grid(True)
plt.show()

