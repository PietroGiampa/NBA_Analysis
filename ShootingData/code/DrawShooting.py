from draw_court import draw_court
import matplotlib.pyplot as plt
import seaborn as sns
import re

player = str(input('Player Name (BR code):'))
player_name = str(input('Player Full Name:'))
year = str(input('Year of Analysis (xxxx):'))

check_all_or_team = str(input('Do You Need a Specific Team? [Y/N]: '))
if check_all_or_team=='N':
    input_name = '../data/'+player+'_'+year+'_all_proc.txt'
if check_all_or_team=='Y':
    team = str(input('Opp Team for Analysis (XXX): '))
    input_name = '../data/'+player+'_'+year+'_'+team+'_proc.txt'

file = open(input_name,'r')
nloop=0
content = []
posx_mk = []
posx_ms = []
posy_mk = []
posy_ms = []
for line in file.readlines():
    content.append(re.findall(r'\d+', line))    
    if int(content[nloop][11])==215:
        posx_mk.append((1.0)*float(content[nloop][1])-238.)
        posy_mk.append(float(content[nloop][0])-47.5)
    if int(content[nloop][11])==9679:
        posx_ms.append((1.0)*float(content[nloop][1])-238.)
        posy_ms.append(float(content[nloop][0])-47.5)
    nloop += 1

plt.figure(figsize=(6,5))
draw_court()
plt.xlim(-250,250)
plt.ylim(422.5,-47.5)
plt.plot(posx_ms, posy_ms, 'go', alpha=0.6,label='Miss')
plt.plot(posx_mk, posy_mk, 'rx', alpha=0.6,label='Make')
if check_all_or_team=='N':
    title_name = player_name+', Season '+year
if check_all_or_team=='Y':
        title_name = player_name+', vs '+team+', Season '+year
plt.title(title_name)
plt.grid(True)
plt.show()

