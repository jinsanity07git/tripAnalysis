import json
from sklearn.cluster import KMeans
import numpy as np

inputfile01 = 'Data/Geojson/02_Origin.geojson'
inputfile02 = 'Data/Geojson/02_Destination.geojson'

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