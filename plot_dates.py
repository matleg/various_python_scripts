import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
import os
import time
import csv
import matplotlib.dates as mdates
import datetime

cwd = os.getcwd()
print(cwd)
lstfi = os.listdir(cwd)

print(time.ctime())

ftoanaly = []

for f in lstfi:
    if f[-4:] == ".csv":
        ftoanaly.append(f)

print("csv files: ", ftoanaly)

for f in ftoanaly:
    dates_full = np.loadtxt(f, delimiter=',', usecols=([0]), skiprows=1, dtype=str)
    prices = np.loadtxt(f, delimiter=',', usecols=([1]), skiprows=1, dtype=float)
print(dates_full)

dates_strip = np.array([i[3:-11] for i in dates_full])

print("dates ", dates_strip)
print("prices ", prices)

formatter = mdates.DateFormatter('%d/%m/%Y')  # format x axis

# conversion of dates to numbers to be able to plot
dates = [datetime.datetime.strptime(d, '%Y-%m-%d').date() for d in dates_strip]
plt.plot_date(dates, prices, '-')
ax = plt.gcf().axes[0]  # get current figure
ax.xaxis.set_major_formatter(formatter)
plt.gcf().autofmt_xdate(rotation=60)

plt.show()
