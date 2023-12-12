# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 19:56:32 2023

@author: losir
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_data(filename):
    '''
    This should read csv files,filter the countries and years as two coloumns
    and transpose the data


    Parameters
    ----------
    filename : TYPE
        This should  be pandas datafiles.

    Returns
    -------
    data1 : TYPE
        Returns Transposed file.
    data1_t : TYPE
        Returns Non Transposed file.

    '''
    # Load data from the CSV file
    data1 = pd.read_csv(filename, skiprows=3)

    # Set the index and select specific countries and years
    data1.index = data1.iloc[:, 0]
    data1 = data1.iloc[:, 1:]
    countries = ["China", "United States","India", "Brazil","South Africa","Japan", "Germany"]
    years = np.arange(1990,2020).astype("str") #   ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997',
             #'1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005']
    data1 = data1.loc[countries, years]

    # Transpose the data for easier plotting
    data1_t = data1.T
    data1_t.index = data1_t.index.astype(int)
    return data1, data1_t


def print_describe_statics(title, data_state):
    '''
    This should inspect the Stastical Properties of data frame using skewness,
    kurtosis and median.

    Parameters
    ----------
    title : TYPE
      The title of specified dataset

    data_state : TYPE
       This should  be pandas datafiles.


    Returns
    -------
    None.

    '''
    # return the title
    print("======="+title+'=======')
    # return the describe
    print("---describe------")
    print(data_state.describe())
    # return skewness
    print("-----skewness-------")
    print(data_state.skew())
    # Return Kurtosis
    print("-----kurtosis------")
    print(data_state.kurtosis())
    # Return Median
    print("-----Median------")
    print(data_state.median())


def bar_plot(df_bar, xlbl, ylbl, title):
    '''
    It will return barplots for specified years and countries

    Parameters
    ----------
    df : TYPE
        This should  be pandas datafiles
    xlbl : TYPE
        Label of X label.
    ylbl : TYPE
        Label of Y label.
    title : TYPE
       Title of graph.

    Returns
    -------
    None.

    '''
    # Sorting of years
    years = [1990, 1995, 2000, 2005]
    # Filter the data
    df_filter = df_bar.loc[years, :]
    plt.figure()
    # The label locations
    x_range = np.arange(len(df_filter.columns))
    # The width of the bars
    width = 0.1
    multiplier = 0
    # Plot the subplot
    plt.subplots(layout='constrained')
    # looping statement for bar plot
    for number in df_filter.index:
        offset = width * multiplier
        plt.bar(x_range + offset, df_filter.loc[number].values.flatten(),
                width, label=number)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels.
    plt.xlabel(xlbl)
    plt.ylabel(ylbl)
    plt.title(title)
    # set the X axis ticks and revolve them to 60 degrees
    plt.xticks(x_range + width, df_filter.columns, rotation=60)
    plt.legend(ncols=3)
    # Save the  bar plot to png
    plt.savefig(title+".png", dpi=300, bbox_inches="tight")
    plt.show()


def plot_line(data_path, title, ylabel, xlabel):
    """
    It will return lineplots for specified years and countries


    Parameters
    ----------
    data_path : TYPE
        This should  be pandas datafiles.
    title : TYPE
        Title of graph
    ylabel : TYPE
       Label of Y label .
    xlabel : TYPE
        Label of X label .
    linestyle : TYPE, optional
        The default is '-'.

    Returns
    -------
    None.

    """
    # plot the figure size
    plt.figure(figsize=(10, 6))
    # Plot the specified line type
    print(title)
    print(data_path)
    data_path.plot(linestyle='--')
    # plot the x label,y label and title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    # Plot the legend
    plt.legend(bbox_to_anchor=(1, 0.5))
    # Save the  line plot to png
    plt.savefig(title+".png", dpi=300, bbox_inches="tight")
    plt.show()


def heat(country, df1, df2, df3, df4, df5, df6,df7,df8):
    """
    It will produce correlation heatmap for specified country and indicators

    Parameters
    ----------
    country : TYPE
       Name of the specified country.
    df1 : TYPE
        This should  be pandas datafiles.
    df2 : TYPE
        This should  be pandas datafiles.
    df3 : TYPE
       This should  be pandas datafiles.
    df4 : TYPE
       This should  be pandas datafiles.
    df5 : TYPE
       This should  be pandas datafiles.
    df6 : TYPE
       This should  be pandas datafiles.

    Returns
    -------
    None.

    """
    # plot the correlation heat map
    dt_corr = pd.DataFrame()
    dt_corr["Methane (KT)"] = df1.loc[country, :].values
    dt_corr["Revenue"] = df2.loc[country, :].values
    dt_corr["Urban Population"] = df3.loc[country, :].values
    dt_corr["Agriculture Land"] = df4.loc[country, :].values
    dt_corr["Arable land"] = df5.loc[country, :].values
    dt_corr["Forest land"] = df6.loc[country, :].values
    dt_corr["Gdp"] = df7.loc[country, :].values
    dt_corr["Electricity"] = df8.loc[country, :].values
    
    
    # correlation calculating
    corr = dt_corr.corr().round(2)
    # plot the figure size
    plt.figure()
    # plot the colour map
    plt.imshow(corr, cmap='Accent_r')
    # Plot the color bar
    plt.colorbar()
    # Label the xticks and yticks
    plt.xticks(np.arange(len(corr.columns)), labels=corr.columns, rotation=90)
    plt.yticks(np.arange(len(corr.columns)), labels=corr.columns)
    # plot the title
    plt.title(country)
    # Comment with correlation values
    for (i, j), corr_ab in np.ndenumerate(corr):
        plt.text(i, j, corr_ab, ha='center', va='center')
    # Save the  heat plot to png
    plt.savefig(country+".png", dpi=300, bbox_inches="tight")
    plt.show()


########### Main ##########
# Load the csv files
data, data_t = read_data("API_EN.ATM.METH.KT.CE_DS2_en_csv_v2_5995564.csv")
data2, data2_t = read_data("API_GC.REV.XGRT.GD.ZS_DS2_en_csv_v2_6235008.csv")
data3, data3_t = read_data("API_SP.URB.TOTL.IN.ZS_DS2_en_csv_v2_5996759.csv")
data4, data4_t = read_data("API_AG.LND.AGRI.ZS_DS2_en_csv_v2_5995314.csv")
data5, data5_t = read_data("API_AG.LND.ARBL.ZS_DS2_en_csv_v2_5995308.csv")
data6, data6_t = read_data("API_AG.LND.FRST.ZS_DS2_en_csv_v2_5994693.csv")
data7, data7_t = read_data("API_NY.GDP.MKTP.CD_DS2_en_csv_v2_6224532.csv")
data8, data8_t = read_data("API_EG.USE.ELEC.KH.PC_DS2_en_csv_v2_6229098.csv")

# Print all the bar plot
bar_plot(data_t, 'Years', 'Methane Emission (KT)',
         'Methane Emission by Countries and Years')
bar_plot(data3_t, 'Years', 'Urban population (% of total population)',
         'Urban  Population')
# Print all the line plot
plot_line(data6_t, 'Forest Land', 'Forest area (% of land area)','Years')
plot_line(data5_t, 'Arable Land', 'Arable land (% of land area','Years')
print()
# Print   all the heat map
heat("India", data, data2, data3, data4, data5, data6,data7,data8)
heat("Brazil", data, data2, data3, data4, data5, data6,data7,data8)
heat("China", data, data2, data3, data4, data5, data6,data7,data8)
# print  all the Stastical Method
print_describe_statics("methane", data_t)
