



import json
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

inputfile01 = 'Data/boss_trianning.geojson'
inputfile02 = 'Data/Geojson/boss_destination.geojson'
outfile01 = 'Data/Geojson/02_Origin.geojson'
outfile02 = 'Data/Geojson/02_Destination.geojson'

with open(inputfile01) as f:
    data01 = json.load(f)

with open(inputfile02) as f:
    data02 = json.load(f)

coordinates01 = [feature['geometry']['coordinates'] for feature in data01['features']]
coordinates02 = [feature['geometry']['coordinates'] for feature in data02['features']]
coordinates = coordinates01 +  coordinates02
coordinates = np.array(coordinates) # for array of list coordinates[:, 0]
#Train model
num_clusters = 7
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(coordinates)


#Plot clusters
figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

cc = kmeans.predict(coordinates)
# y_point = [coordinates[i][1] for i in range(len(coordinates)) ]
# x_point = [coordinates[i][0] for i in range(len(coordinates)) ]

# plt.scatter(x_point, y_point, c=cc, s=50, cmap='viridis')
# plt.xlim(min(coordinates[:, 0])*1.0001, max(coordinates[:, 0]*0.9999))
# plt.ylim(min(coordinates[:, 1])*1.001, max(coordinates[:, 1]*0.999))
plt.scatter(coordinates[:, 0], coordinates[:, 1], c=kmeans.predict(coordinates), s=num_clusters, cmap='viridis')

# #Plot clusters __center
# centers = kmeans.cluster_centers_
# plt.xlim(min(coordinates[:, 0]) - 10, -50)
# plt.scatter(
# centers[:, 0],
# centers[:, 1],
# c='black',
# s=200,
# alpha=0.5
# # );
plt.show()
# import geopandas

# df = geopandas.read_file(geopandas.datasets.get_path('nybb'))
# ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')

from geojson import Point, Feature, FeatureCollection, dump
### TO add classifier information into the GEOjson file or shape file
Len01 = len(data01['features'])
for i in range(Len01):
    data01['features'][i]['properties'].update({'class':str(cc[i])})

with open(outfile01, 'w') as f:
   dump(data01, f)

Len02 = len(cc) - Len01
for i in range(Len02):
    data02['features'][i]['properties'].update({'class':str(cc[i])})

with open(outfile02, 'w') as f:
   dump(data02, f)


# import json
# with open('02_Origin.json','w') as f:
#     json.dump(data, f)