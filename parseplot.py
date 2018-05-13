#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import sys
from os.path import dirname, abspath
import datetime
inFile = sys.argv[1]

fd = open(inFile, "r")

data = np.empty((0,14))
while ("ObsCode" not in fd.readline()):
    continue

while True:
    line = fd.readline()[:-1]
    line = line.replace(":",",").split(",")
    line = [ None if i =="" else i for i in line]
    if  len(line)==1: break
    if ( len(line)==13): line.append(0)
    try:
        data = np.append(data, [line],axis=0)
    except Exception as e:
        print("Error:", e)
        break

fd.close()

# Backup the ObsCode before replacing it with 0s.
ObsCode = data[:,4:5]
data[:,4:5] = 0
data = data.astype(np.float16)
time = (60*60*data[:,0] + 60*data[:,1] + data[:,2])/60/60
air_mass = data[:,5]
total_ozone = data[:,6]
total_sd = data[:,9]
temp = data[:,12]
f324 = data[:,13]

# Generate title from the date and the station of the data
print(data[0:6,:])
date = datetime.datetime.strptime(inFile[:8], "%Y%m%d")
station = dirname(abspath(inFile))
title =  date.strftime("%d %b, %Y") + " " + station.split("/")[-1].upper()

plt.subplot(5,1,1)
plt.plot(time,air_mass)
plt.ylabel("Air Mass")
plt.title(title)

plt.subplot(5,1,2)
plt.plot(time,total_ozone)
plt.ylabel("Total Ozone")

plt.subplot(5,1,3)
plt.plot(time,total_sd)
plt.ylabel("Total SO2")

plt.subplot(5,1,4)
plt.plot(time,temp)
plt.ylabel("Temp. (C)")

plt.subplot(5,1,5)
plt.plot(time,temp)
plt.xlabel("Hour")
plt.ylabel("F324")

fig = plt.gcf()
plt.show()
if input("save plot? (y/n) : ") == "y":
    fig.savefig("plot.png")
    print('Saved !')
