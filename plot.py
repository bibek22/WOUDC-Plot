#!/usr/bin/python

import numpy as np
import pylab
import matplotlib.pyplot as plt
import sys
inFile = sys.argv[1]

# Read the data in a numpy array

try:
    corpus = np.loadtxt(inFile)
except Exception as e:
    print("Failed to load file into array. Exiting...")
    print(e)
    sys.exit(-1)

time = (60*60*corpus[:,0] + 60*corpus[:,1] + corpus[:,2])/60/60
air_mass = corpus[:,5]
total_ozone = corpus[:,6]
total_sd = corpus[:,9]
temp = corpus[:,12]
f324 = corpus[:,13]
title = input("Title of the plot: ")

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

# plt.show()
pylab.savefig("plot.png")
