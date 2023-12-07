# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 19:56:32 2023

@author: losir
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_data(filename):
    #Load data from the CSV file
    data1 = pd.read_csv(filename, skiprows=3)

    # Set the index and select specific countries and years
    data1.index = data1.iloc[:, 0]
    data1 = data1.iloc[:, 1:]
    countries = ["China", "India", "Russian Federation","Brazil","Indonesia", "United States"]
    years = ['1990', '1995', '2000', '2005'] # all all tghe year like 1990 to 2008
    data1 = data1.loc[countries, years]

    # Transpose the data for easier plotting
    data1_t = data1.T
    data1_t.index = data1_t.index.astype(int)
    return data1, data1_t

def  bar(df,xlbl,ylbl,title):
    years = [1990, 1995, 2000, 2005]
    df_filter=df.loc[years,:]
    plt.figure()
    x = np.arange(len(df_filter.columns))  # the label locations

    width = 0.1  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')


    for ii in df.index:
        offset = width * multiplier
        reacts = ax.bar(x + offset, df_filter.loc[ii].values.flatten(), width, label=ii)
        #rects = ax.bar(x + offset, measurement, width, label=attribute)
       # ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel(xlbl)
    ax.set_ylabel(ylbl )
    ax.set_title(title)
    ax.set_xticks(x + width, df_filter.columns)
    ax.legend(ncols=3)


    plt.show()

def heat(country,df1,df2,df3):
    dt_corr = pd.DataFrame()
    dt_corr["Agriculture Methane"] = df2.loc[country,:].values
    dt_corr["Urban Population"] = df2.loc[country,:].values
    dt_corr["Methane (KT)"] = df1.loc[country,:].values

    corr = dt_corr.corr().round(3)
    print(corr)
    plt.figure()
    grid = plt.imshow(corr,cmap='Accent_r')
    plt.colorbar()
    plt.xticks(np.arange(len(corr.columns)), labels=corr.columns, rotation=90)
    plt.yticks(np.arange(len(corr.columns)), labels=corr.columns)


    plt.title(country)
    for (i, j), z in np.ndenumerate(corr):
        plt.text(i,j,z,ha='center',va='center')

    plt.show()


###########################
data, data_t =  read_data("API_EN.ATM.METH.KT.CE_DS2_en_csv_v2_5995564.csv")
data2, data2_t =  read_data("API_EN.ATM.METH.AG.ZS_DS2_en_csv_v2_5995573.csv")
data3, data3_t =  read_data("API_SP.URB.TOTL.IN.ZS_DS2_en_csv_v2_5996759.csv")


bar(data_t,'Years','Methane Emission (KT)','Methane Emission by Countries and Years' )
bar(data2_t,'Years','Agriculture Methane Emission (KT)',\
    'Agriculture Methane Emission by Countries and Years')
heat("India",data,data2,data3)
heat("Brazil",data,data2,data3)
heat("China",data,data2,data3)
