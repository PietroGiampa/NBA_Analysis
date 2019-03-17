#########################
# LVJ Shooting Analysis #
# --------------------- #
# Pietro Giampa, 2019   #
#########################
import matplotlib.pyplot as plt
import numpy as np
import csv
import math
import sys
from draw_court import draw_court

# open file
file2008 = open('data/Season2007_2008.csv','r');
lines2008 = file2008.readlines()
file2013 = open('data/Season2012_2013.csv','r');
lines2013 = file2013.readlines()
file2016 = open('data/Season2015_2016.csv','r');
lines2016 = file2016.readlines()
file2019 = open('data/Season2018_2019.csv','r');
lines2019 = file2019.readlines()

# define arrays
outcome1 = []
xpos_made1 = np.zeros(2000)
xpos_miss1 = np.zeros(2000)
ypos_made1 = np.zeros(2000)
ypos_miss1 = np.zeros(2000)
outcome2 = []
xpos_made2 = np.zeros(2000)
xpos_miss2 = np.zeros(2000)
ypos_made2 = np.zeros(2000)
ypos_miss2 = np.zeros(2000)
outcome3 = []
xpos_made3 = np.zeros(2000)
xpos_miss3 = np.zeros(2000)
ypos_made3 = np.zeros(2000)
ypos_miss3 = np.zeros(2000)
outcome4 = []
xpos_made4 = np.zeros(2000)
xpos_miss4 = np.zeros(2000)
ypos_made4 = np.zeros(2000)
ypos_miss4 = np.zeros(2000)

# define variables
n1=0
made1=0
miss1=0
n2=0
made2=0
miss2=0
n3=0
made3=0
miss3=0
n4=0
made4=0
miss4=0

##-------------------------------++
## Loop throguh all shots        ++
##-------------------------------++
for x1 in lines2008:
    #get if the shot was made or missed
    outcome1.append(x1.split()[14])
    #only made shots
    if outcome1[n1]=='Made':
        xpos_made1[made1] = x1.split()[3]
        ypos_made1[made1] = x1.split()[1]
        xpos_made1[made1] = (-1.0)*(xpos_made1[made1]-250.0)
        ypos_made1[made1] = ypos_made1[made1]-50.0
        made1 = made1 + 1
    #only missed shots
    if outcome1[n1]=='Missed':
        xpos_miss1[miss1]= x1.split()[3]
        ypos_miss1[miss1] = x1.split()[1]
        xpos_miss1[miss1] = (-1.0)*(xpos_miss1[miss1]-250.0)
        ypos_miss1[miss1] = ypos_miss1[miss1]-50.0
        miss1 = miss1 + 1
    #good for keeping trac of outcome loop
    n1 = n1 +1

for x2 in lines2013:
    #get if the shot was made or missed
    outcome2.append(x2.split()[14])
    #only made shots
    if outcome2[n2]=='Made':
        xpos_made2[made2] = x2.split()[3]
        ypos_made2[made2] = x2.split()[1]
        xpos_made2[made2] = (-1.0)*(xpos_made2[made2]-250.0)
        ypos_made2[made2] = ypos_made2[made2]-50.0
        made2 = made2 + 1
    #only missed shots
    if outcome2[n2]=='Missed':
        xpos_miss2[miss2]= x2.split()[3]
        ypos_miss2[miss2] = x2.split()[1]
        xpos_miss2[miss2] = (-1.0)*(xpos_miss2[miss2]-250.0)
        ypos_miss2[miss2] = ypos_miss2[miss2]-50.0
        miss2 = miss2 + 1
    #good for keeping trac of outcome loop
    n2 = n2 +1

for x3 in lines2016:
    #get if the shot was made or missed
    outcome3.append(x3.split()[14])
    #only made shots
    if outcome3[n3]=='Made':
        xpos_made3[made3] = x3.split()[3]
        ypos_made3[made3] = x3.split()[1]
        xpos_made3[made3] = (-1.0)*(xpos_made3[made3]-250.0)
        ypos_made3[made3] = ypos_made3[made3]-50.0
        made3 = made3 + 1
    #only missed shots
    if outcome3[n3]=='Missed':
        xpos_miss3[miss3]= x3.split()[3]
        ypos_miss3[miss3] = x3.split()[1]
        xpos_miss3[miss3] = (-1.0)*(xpos_miss3[miss3]-250.0)
        ypos_miss3[miss3] = ypos_miss3[miss3]-50.0
        miss3 = miss3 + 1
    #good for keeping trac of outcome loop
    n3 = n3 +1

for x4 in lines2019:
    #get if the shot was made or missed
    outcome4.append(x4.split()[14])
    #only made shots
    if outcome4[n4]=='Made':
        xpos_made4[made4] = x4.split()[3]
        ypos_made4[made4] = x4.split()[1]
        xpos_made4[made4] = (-1.0)*(xpos_made4[made4]-250.0)
        ypos_made4[made4] = ypos_made4[made4]-50.0
        made4 = made4 + 1
    #only missed shots
    if outcome4[n4]=='Missed':
        xpos_miss4[miss4]= x4.split()[3]
        ypos_miss4[miss4] = x4.split()[1]
        xpos_miss4[miss4] = (-1.0)*(xpos_miss4[miss4]-250.0)
        ypos_miss4[miss4] = ypos_miss4[miss4]-50.0
        miss4 = miss4 + 1
    #good for keeping trac of outcome loop
    n4 = n4 +1

##-------------------------------++
## Get rid of zeros entries      ++
## Need to find a better way     ++
## for doing this                ++
##-------------------------------++
nxpos_made1 = np.zeros(made1)
nypos_made1 = np.zeros(made1)
nxpos_miss1 = np.zeros(miss1)
nypos_miss1 = np.zeros(miss1)

nxpos_made2 = np.zeros(made2)
nypos_made2 = np.zeros(made2)
nxpos_miss2 = np.zeros(miss2)
nypos_miss2 = np.zeros(miss2)

nxpos_made3 = np.zeros(made3)
nypos_made3 = np.zeros(made3)
nxpos_miss3 = np.zeros(miss3)
nypos_miss3 = np.zeros(miss3)

nxpos_made4 = np.zeros(made4)
nypos_made4 = np.zeros(made4)
nxpos_miss4 = np.zeros(miss4)
nypos_miss4 = np.zeros(miss4)

for i in range(0, (made1-1)):
    nxpos_made1[i] = xpos_made1[i]
    nypos_made1[i] = ypos_made1[i]
for k in range(0, (miss1-1)):
    nxpos_miss1[k] = xpos_miss1[k]
    nypos_miss1[k] = ypos_miss1[k]

for ii in range(0, (made2-1)):
    nxpos_made2[ii] = xpos_made2[ii]
    nypos_made2[ii] = ypos_made2[ii]
for kk in range(0, (miss2-1)):
    nxpos_miss2[kk] = xpos_miss2[kk]
    nypos_miss2[kk] = ypos_miss2[kk]

for iii in range(0, (made3-1)):
    nxpos_made3[iii] = xpos_made3[iii]
    nypos_made3[iii] = ypos_made3[iii]
for kkk in range(0, (miss3-1)):
    nxpos_miss3[kkk] = xpos_miss3[kkk]
    nypos_miss3[kkk] = ypos_miss3[kkk]

for iiii in range(0, (made4-1)):
    nxpos_made4[iiii] = xpos_made4[iiii]
    nypos_made4[iiii] = ypos_made4[iiii]
for kkkk in range(0, (miss4-1)):
    nxpos_miss4[kkkk] = xpos_miss4[kkkk]
    nypos_miss4[kkkk] = ypos_miss4[kkkk]

##-------------------------------++
## Print Whats Wanted            ++
##-------------------------------++
fig = plt.figure(facecolor='white', edgecolor='white')
draw_court(outer_lines=True)
plt.xlim(-250,250)
plt.ylim(-49,424)
plt.plot(nxpos_miss1, nypos_miss1, 'rx', label='Missed', alpha=0.5)
plt.plot(nxpos_made1, nypos_made1, 'go', label='Made', alpha=0.5)
plt.legend(loc='upper left',numpoints=1)
plt.title('Season 2007-2008: Box Chart')
plt.savefig('img/s2008_bc.png')
plt.show()

fig = plt.figure(facecolor='white', edgecolor='white')
draw_court(outer_lines=True)
plt.xlim(-250,250)
plt.ylim(-49,424)
plt.plot(nxpos_miss2, nypos_miss2, 'rx', label='Missed', alpha=0.5)
plt.plot(nxpos_made2, nypos_made2, 'go', label='Made', alpha=0.5)
plt.legend(loc='upper left',numpoints=1)
plt.title('Season 2012-2013: Box Chart')
plt.savefig('img/s2013_bc.png')
plt.show()

fig = plt.figure(facecolor='white', edgecolor='white')
draw_court(outer_lines=True)
plt.xlim(-250,250)
plt.ylim(-49,424)
plt.plot(nxpos_miss3, nypos_miss3, 'rx', label='Missed', alpha=0.5)
plt.plot(nxpos_made3, nypos_made3, 'go', label='Made', alpha=0.5)
plt.legend(loc='upper left',numpoints=1)
plt.title('Season 2015-2016: Box Chart')
plt.savefig('img/s2016_bc.png')
plt.show()

fig = plt.figure(facecolor='white', edgecolor='white')
draw_court(outer_lines=True)
plt.xlim(-250,250)
plt.ylim(-49,424)
plt.plot(nxpos_miss4, nypos_miss4, 'rx', label='Missed', alpha=0.5)
plt.plot(nxpos_made4, nypos_made4, 'go', label='Made', alpha=0.5)
plt.legend(loc='upper left',numpoints=1)
plt.title('Season 2018-2019: Box Chart')
plt.savefig('img/s2019_bc.png')
plt.show()
