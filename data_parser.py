import pandas as pd
import os
import glob

#path = "/Users/rjromero/Data/disneyland_park_times/*"
fp = "/Users/rjromero/Data/disneyland_park_times/1578881703111.json"

df = pd.read_json(fp)

df = df [['name', 'waitTime', 'status', 'lastUpdate']]

df = df.loc[df.status == "Operating"]

ef = df.iloc[0].lastUpdate

print(df)
print(ef)