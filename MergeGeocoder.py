import requests
from geopy.geocoders import GoogleV3
from geopy.exc import GeocoderTimedOut
from geopy.exc import GeocoderQueryError

import pandas as pd
import csv,json
import time

## GoogleV3(api_key=myKey, timeout=3)  geocoding too slow
start = time.time()
print("hello")


location = {'O':'Pick Up Location', 'D':'Drop Off Location'}
path  = 'Data/2019_02.csv'
OD_type = location['D']
Rela_ad = 'inprocess_results/'

infile01 = Rela_ad + 'boss02_'+location['O']+ '.csv'
infile02 = Rela_ad + 'boss02_'+location['D']+ '.csv'
infile03 = Rela_ad + 'Matching.json'


outfile01 = Rela_ad + 'boss02All' + '.csv'


df01 = pd.read_csv(infile01,encoding = 'unicode_escape')
df02 =pd.read_csv(infile02,encoding = 'unicode_escape')
df01.columns

with open(infile03) as json_file:
    Mdict = json.load(json_file)

df01['long'][2] in Mdict

for i in range(0, len(df01)):
    place = df01['long'][i]
    if place in Mdict:
        print (df01['long'][i])

        df01.loc[i,['long']] = Mdict[place]['longitude']
        df01.loc[i,['lat']] = Mdict[place]['latitude']


for i in range(0, len(df02)):
    place = df02['long'][i]
    if place in Mdict:
        print (df02['long'][i])

        df02.loc[i,['long']] = Mdict[place]['longitude']
        df02.loc[i,['lat']] = Mdict[place]['latitude']


df01['LatDrop'] =df02['lat']
df01['LongDrop'] =df02['long']

df01.to_csv(outfile01)