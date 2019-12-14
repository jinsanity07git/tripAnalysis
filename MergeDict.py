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
inputfile01 = Rela_ad + 'Request_data_testAProofed.csv'

inputfile02 = Rela_ad + 'Request_data_testPK.csv'

outfile01 = Rela_ad + 'Matching.json'


df = pd.read_csv(inputfile01,encoding = 'unicode_escape')
df.columns

df_new= df[['address','latitude','longitude']]
df_new =df_new.set_index('address')
df_dict = df_new.to_dict('index')


df02 = pd.read_csv(inputfile02,encoding = 'unicode_escape')
df_new02= df02[['address','latitude','longitude']]
df_new02 =df_new02.set_index('address')
df_new02.index[2]

for i in range(len(df_new02)):
    if df_new02.index[i] in df_dict:
        pass
    else:
        print (df_new02.index[i])


with open(outfile01,'w',encoding='utf-8') as json_file:
     json.dump(df_dict, json_file)

end = time.time()
print(str(int((end - start)/60)) + ' min' )

