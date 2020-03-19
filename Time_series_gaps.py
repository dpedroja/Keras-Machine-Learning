# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 08:29:06 2020

@author: dpedroja
"""
import pandas as pd

# load in data set
TodasEstaciones = pd.read_csv('Est1_Est2_Est3.csv',index_col=0,parse_dates=True)

# set index & rename data
all_stations = TodasEstaciones.reset_index()
# find all nulls in Est2 column
nulls = pd.isnull(all_stations["Est2"])
df = all_stations[nulls]

# create a new index based on the subset of null values
# This operation turns the original index for the full data set, into a new data column which will be used to find gaps
df = df.reset_index()

# rename the new data column "row," change spanish date to "date"
df.columns = ['row', 'date', 'Est1', 'Est2', 'Est3']

# find gaps in the original index value which indicates the beginning and end of gaps
df["gap"] = (df["row"].diff(periods= -1)) < -1
df["gap2"] = (df["row"].diff(periods= 1)) > 1

# set the index to "date" so that the date values can be selected
df = df.set_index("date")

# select the start, middle, end of date list
start = df.index[0]
ranges = df.index[df["gap"] == True].tolist()
end = df.index[-1]

# insert the start to the middle, and append the end
ranges.insert(0, start)
ranges.append(end)
print(ranges)

# now we need to find the distance between the start and end

