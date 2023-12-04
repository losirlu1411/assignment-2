# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 19:56:32 2023

@author: losir
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
data = pd.read_csv("API_EN.ATM.METH.KT.CE_DS2_en_csv_v2_5995564.csv", skiprows=3)

# Set the index and select specific countries and years
data.index = data.iloc[:, 0]
data = data.iloc[:, 1:]
countries = ["China", "India", "Russian Federation","Brazil", "Indonesia","Australia"]
years = ['1990', '1995', '2000', '2005']
data = data.loc[countries, years]

# Transpose the data for easier plotting
data_t = data.T
data_t.index = data_t.index.astype(int)

################################################################
###########################################################


plt.figure()
#species = data_t.columns
#penguin_means = data_t

x = np.arange(len(data_t.columns))  # the label locations

width = 0.1  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')
#print(penguin_means.items())
for ii in data_t.index:
    print(data_t.loc[ii])
for ii in data_t.index:
    print(ii)
    offset = width * multiplier
    rects = ax.bar(x + offset, data_t.loc[ii].values.flatten(), width, label=ii)
    #rects = ax.bar(x + offset, measurement, width, label=attribute)
   # ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, data_t.columns)
ax.legend(ncols=3)

##########################################################
################################################

plt.show()




