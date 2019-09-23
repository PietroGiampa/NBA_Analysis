### Define Needed Libraries ###
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

### Define Functions ###
def getImage(path):
    im = plt.imread(path)
    return OffsetImage(im, zoom=0.035, alpha=0.85)

### Open Data ###
data = pd.read_csv('../data/TeamStats.csv', header=None, error_bad_lines=False, sep='\t')
data.columns = ['num','City','Team','G','MP','FG','FGA','FG%','3P','3PA','3P%','2P','2PA','2P%','FT','FTA','FT%','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS']

### Skim Data To Extract Usful Info ###
team = data['Team']
team = team[:-1]
FGA = data['FGA']
FGA_AVG = FGA[30]
FGA = FGA[:-1]
FGP = data['FG%']
FGP_AVG = FGP[30]
FGP = FGP[:-1]
FG = data['FG']
FG_AVG = FG[30]
FG = FG[:-1]

### Print Info ###
print('League Average FGA: ', FGA_AVG)
print('League Average FG%: ', FGP_AVG)

### Set Img Directories ###
base_path = '../../LOGOs/'
paths = []
for i in range(30):
    fullpath = base_path+team[i]+'.jpg'
    paths.append(fullpath)

### Print ###
fig, ax = plt.subplots()
ax.scatter(FGA, FG) 
ax.plot()
plt.plot([min(FGA)-1, max(FGA)+1], [FG_AVG, FG_AVG],'r--')
plt.plot([FGA_AVG, FGA_AVG],[min(FG)-1, max(FG)+1],'r--')
for x0, y0, path in zip(FGA, FG, paths):
    ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
    ax.add_artist(ab)
plt.xlim(min(FGA)-1,max(FGA)+1)
plt.ylim(min(FG)-1,max(FG)+1)
plt.xlabel('Field Goals Attempted')
plt.ylabel('Field Goals Made')
plt.grid(True)
plt.show()

