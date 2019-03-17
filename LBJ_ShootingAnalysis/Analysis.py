#########################
# LVJ Shooting Analysis #
# --------------------- #
# Pietro Giampa, 2019   #
#########################
import matplotlib.pyplot as plt
import numpy as np
import csv
import math

# open file
file = open('data/Season2007_2008.csv','r');
lines = file.readlines()

# define arrays
outcome = []
xpos_made = np.zeros(2000)
xpos_miss = np.zeros(2000)
ypos_made = np.zeros(2000)
ypos_miss = np.zeros(2000)

# define variables
n=0
made=0
miss=0

##-------------------------------++
## Loop throguh all shots        ++
##-------------------------------++
for x in lines:
    #get if the shot was made or missed
    outcome.append(x.split()[13])
    
    #only made shots
    if outcome[n]=='Made':
        xpos_made[made] = x.split()[3]
        ypos_made[made] = x.split()[1]
        xpos_made[made] = (-1.0)*(xpos_made[made]-250.0)
        ypos_made[made] = ypos_made[made]-50.0
        made = made + 1
        
    #only missed shots
    if outcome[n]=='Missed':
        xpos_miss[made]= x.split()[3]
        ypos_miss[made] = x.split()[1]
        xpos_miss[made] = (-1.0)*(xpos_miss[miss]-250.0)
        ypos_miss[made] = ypos_miss[miss]-50.0
        miss = miss + 1
        
    #good for keeping trac of outcome loop
    n = n +1

##-------------------------------++
## Print Whats Wanted            ++
##-------------------------------++

