%matplotlib inline
import os
import re
import pandas as pd
import datetime as dt
import numpy as np
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [16, 10]
plt.rcParams['font.size'] = 14
import seaborn as sns
import warnings
fig = plt.gcf()
fig.set_size_inches( 16, 10)

import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon


accidents = pd.read_csv("accidents_2017.csv")

cortsacc = accidents[accidents['Street'].str.contains("Corts Catalanes")]
noncortsacc = accidents[~accidents['Street'].str.contains("Corts Catalanes")]

crs = {'init': 'epsg:4326'}
cortsgeometry = [Point(xy) for xy in zip(cortsacc["Longitude"], cortsacc["Latitude"])]
noncortsgeometry =  [Point(xy) for xy in zip(noncortsacc["Longitude"], noncortsacc["Latitude"])]
allgeo =[Point(xy) for xy in zip(accidents["Longitude"], accidents["Latitude"])]
cortsgeo_acc = gpd.GeoDataFrame(cortsacc,
                          crs = crs,
                          geometry = cortsgeometry)

noncortsgeo_acc = gpd.GeoDataFrame(noncortsacc,
                          crs = crs,
                          geometry = noncortsgeometry)
allaccgeo = gpd.GeoDataFrame(accidents,
                          crs = crs,
                          geometry = allgeo)

street_map = gpd.read_file('BCN_Barri_ED50_SHP.shp')
street_map.crs
constreet_map = street_map.to_crs({'init': 'epsg:4326'}) 



fig,ax = plt.subplots(figsize= (15,15))
constreet_map.plot(ax=ax, alpha = .4, color = "grey")
allaccgeo[allaccgeo["Vehicles involved"] == 2].plot(ax = ax, markersize = 20, color = "blue", marker = "o", label = "Accidents involving 2 cars")
allaccgeo[allaccgeo["Vehicles involved"] == 3].plot(ax = ax, markersize = 20, color = "red", marker = "^", label = "Accidents involving 3 cars")
allaccgeo[allaccgeo["Vehicles involved"] > 3].plot(ax = ax, markersize = 20, color = "white", marker = "^", label = "Accidents greater than 3 cars")
plt.legend(prop={'size':15})

janacc = allaccgeo[allaccgeo["Hour"] == 20]

fig,ax = plt.subplots(figsize= (15,15))
constreet_map.plot(ax=ax, alpha = .4, color = "grey")
janacc[janacc["Vehicles involved"] == 2].plot(ax = ax, markersize = 20, color = "blue", marker = "o", label = "Accidents involving 2 cars")
janacc[janacc["Vehicles involved"] == 3].plot(ax = ax, markersize = 20, color = "red", marker = "^", label = "Accidents involving 3 cars")
janacc[janacc["Vehicles involved"] > 3].plot(ax = ax, markersize = 20, color = "white", marker = "^", label = "Accidents greater than 3 cars")
plt.legend(prop={'size':15})