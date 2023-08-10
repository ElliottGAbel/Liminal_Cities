#!/usr/bin/env python
import pandas as pd
import geopandas
import matplotlib.pyplot as plt
import numpy as np
import os
import requests
import gzip
import shutil
import glob
import folium

sharedFolder = '/work/group/egodat/reu23_clark/'
dataFolder = sharedFolder + 'data/'

for LODESYear in ['05', '10', '15', '19', '20']:
    print("Year:", LODESYear)

    if os.path.exists(dataFolder + "/od_data_combined" + LODESYear + ".pkl"):
        print("Loading cached file...")
        odData = pd.read_pickle(dataFolder + "/od_data_combined" + LODESYear + ".pkl")
    else:
        stateData = []
        print("No Cached File...")

        for path in glob.glob(dataFolder + "/LODES" + LODESYear + "/*_od_main_JT00_20*.csv"):
            print(".", end="")
            odData = pd.read_csv(path)
            odData = odData[['w_geocode', 'h_geocode', 'S000']]
            stateData.append(odData)

        odData = pd.concat(stateData)
        odData.to_pickle(dataFolder + "/od_data_combined" + LODESYear + ".pkl")
        # odData
