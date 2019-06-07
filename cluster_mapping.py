import json
from sklearn.cluster import KMeans
import numpy as np

inputfile01 = 'Data/Geojson/02_Origin.geojson'
inputfile02 = 'Data/Geojson/02_Destination.geojson'

Rela_ad = 'inprocess_results/'
outfile01 = 'Data/Geojson/address_class_dic.json'
outfile02 = Rela_ad + '02_ODflow.csv'

### step01 preparing address class to a {address : class_type} dict for indexing
with open(inputfile01) as f:
    data01 = json.load(f)

with open(inputfile02) as f:
    data02 = json.load(f)
i = 1999
address = data01['features'][i]['properties']['Pick Up Lo']
if data01['features'][i]['properties']['Pick Up Lo'] == address :
    print (1)


for index in range(2000):
    if data01['features'][index]['properties']['Pick Up Lo'] == address :
        class_ty = data01['features'][index]['properties']['class']
        print (class_ty)
        print (index)
        break

dic_all = {}
len01 = len(data01['features'])
for index in range(len01):
    key   = data01['features'][index]['properties']['Pick Up Lo']
    value = data01['features'][index]['properties']['class']
    dic_all.update({key:value})
    # print (index)

# dic02 = {}
len02 = len(data02['features'])
for index in range(len02):
    key   = data02['features'][index]['properties']['Drop Off Location']
    value = data02['features'][index]['properties']['class']
    dic_all.update({key:value})

with open(outfile01,'w') as f:
    json.dump(dic_all,f)
# dic01[address]




###
###step02 mapping address to the cluster 
import pandas as pd
path  = 'Data/2019_02.csv'

df = pd.read_csv(path,encoding = 'unicode_escape')
'''
df.columns
df.columnsdf.co
Index(['Requested Pick Up Time', '# of Pass-engers', 'Pick Up Location',
       'Drop Off Location', 'Cancellation Time', 'Pickup Time',
       'Drop Off Time', 'Wait Time (min)', 'Passenger Canceled?',
       'Cancellation Message'],
      dtype='object')
'''
# df.loc[5,'O_type'] 

df['O_type'],df['D_type'] = None,None
for i in range(len(df)):
    try:
        O_address = df['Pick Up Location'][i]
        D_address = df['Drop Off Location'][i]
        # df['O_type'][i] = dic_all[O_address]
        # df['D_type'][i] = dic_all[D_address]
        df.loc[i,'O_type']  = dic_all[O_address]
        df.loc[i,'D_type']  = dic_all[D_address]
    except:
        
        pass


### Filter out nan rows in a specific column
df.dropna(subset=['O_type', 'D_type'])[['O_type', 'D_type']]
# df.dropna(subset=['']) 
# df[df['O_type'].isnull()].drop()

### print groupby count from O to D
df_agg = df.groupby(['O_type', 'D_type']).count()['Requested Pick Up Time']

### 2 levels groupby dataframe transform to a 2D matrix
df_agg.to_csv(outfile02)