#####################################################
## Getting Shooting Info from Basketball-Reference ##
#####################################################
## Pietro Giampa, August 2019                      ##
#####################################################

#####################################################
##              Define Dependencies                ##
#####################################################
import requests
import numpy as np
import re
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
    
#####################################################
##         ExportShootingToText Function           ##
#####################################################
def ExportShootingToText(player, year):
    print('...Fetching...')
    pre_tag = player[0]
    url_path = 'https://www.basketball-reference.com/players/'+pre_tag+'/'+player+'/shooting/'+year
    website_url = requests.get(url_path).text
    soup = BeautifulSoup(website_url,features="html.parser")
    array = soup.find_all(id="all_shot-chart")
    output_name = '../data/'+player+'_'+year+'_raw.txt'
    with open(output_name, "w") as output:
        output.write(str(array))

#####################################################
##            FormatDataAll Function               ##
#####################################################
def FormatDataAll(player, year):
    print('... Formatting ...')
    input_name = '../data/'+player+'_'+year+'_raw.txt'
    file = open(input_name,'r')
    nloop=0
    content = []
    output_name = '../data/'+player+'_'+year+'_all_proc.txt'
    with open(output_name, 'w') as output:
        for line in file.readlines(): 
            content.append(re.findall(r'\d+', line))
            testo = ''
            for i in range(int(len(content[nloop]))): 
                testo += str(content[nloop][i])+'\t'
            testo += '\n'
            if int(len(content[nloop]))>5:
                output.write(testo)
            nloop += 1

#####################################################
##            FormatDataTeam Function              ##
#####################################################
def FormatDataTeam(player, year, team):
    print('... Formatting ...')
    input_name = '../data/'+player+'_'+year+'_raw.txt'
    file = open(input_name,'r')
    nloop=0
    content = []
    output_name = '../data/'+player+'_'+year+'_'+team+'_proc.txt'
    with open(output_name, 'w') as output:
        for line in file.readlines():
            if team in line:
                content.append(re.findall(r'\d+', line))
                testo = ''
                for i in range(int(len(content[nloop]))):
                    testo += str(content[nloop][i])+'\t'
                testo += '\n'
                if int(len(content[nloop]))>5:
                    output.write(testo)
                nloop += 1

###################################################
##                  Main Body                    ##
###################################################
player = str(input('Player Name (BR code): '))
year = str(input('Year of Analysis (xxxx): '))
check_all_or_team = str(input('Do You Need a Specific Team? [Y/N]: '))
if check_all_or_team=='N':
    ExportShootingToText(player, year)
    FormatDataAll(player, year)
if check_all_or_team=='Y':
    team = str(input('Opp Team for Analysis (XXX): '))
    ExportShootingToText(player, year)
    FormatDataTeam(player, year, team)
