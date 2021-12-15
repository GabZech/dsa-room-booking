#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 12:58:07 2021

@author: hannahschweren
"""

#%% import packages
import pandas as pd

#%% create data for dataset
data  = {'name': [2.31, 2.32, 2.35, 2.4, 2.6, 2.71, 3.01, 3.1, 3.22, 3.33, 3.35, 3.4, 3.5, 3.6], 'capacity': [2, 3, 8, 2, 4, 4, 35, 7, 3, 5, 12, 15, 17, 4],'quiet': ['True', 'True', 'False', 'True', 'True', 'False', 'False', 'False', 'True', 'True', 'True', 'False', 'False', 'True'], 'tv': ['True', 'False', 'False', 'True', 'False', 'False', 'True', 'True', 'False', 'False', 'False', 'True', 'False', 'False'], 'projector': ['False', 'False', 'False', 'False', 'True', 'False', 'False', 'False', 'False', 'False', 'True', 'True', 'False', 'False'], 'available_places': [2, 3, 8, 2, 4, 4, 35, 7, 3, 5, 12, 15, 17, 4]}

#%% create dataframe
df = pd.DataFrame(data)

#%% 
df_repeated = pd.concat([df]*8737, ignore_index=True)

#%% sort the data by name of the room
df_repeated = df_repeated.sort_values(by=['name'])
df_repeated = df_repeated.reset_index()

#%% create datetime array
a = pd.DataFrame({'date_time':pd.date_range(start='2022-01-01', end='2022-12-31', freq='H')})
a_repeated = pd.concat([a]*14, ignore_index=True)

#%% merge the room data witht he dstetime data
result = pd.concat([df_repeated, a_repeated], axis=1)

#%% change order of columns
result = result[["name", "capacity", "quiet", "tv", "projector", "date_time", "available_places"]]


#%% change format of datetime column
result['date_time'] = result['date_time'].dt.strftime('%m/%d/%Y, %H')

#%% save output to rooms file
result.to_csv('../data/raw/rooms.csv', index=False)
result.to_csv('../data/processing/rooms.csv', index=False)
