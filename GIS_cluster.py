
import json
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


inputfile01 = 'Data/boss_trianning.geojson'
inputfile02 = 'Data/Geojson/boss_destination.geojson'
outfile01 = 'Data/Geojson/02_Origin.geojson'
outfile02 = 'Data/Geojson/02_Destination.geojson'
outfile03 = 'inprocess_results/flows.png'
outfile04 = 'inprocess_results/centers.json'

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
kmeans = kmeans.fit(coordinates)


#Plot clusters
# figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
# fig = plt.figure()
fig , ax = plt.subplots()

cc = kmeans.predict(coordinates)
cc.tolist()
# # for i in range(cc):
# for i,val in enumerate(cc.tolist()) :
#     print (i,val)
cluster_ty =  3
x= [coordinates[i, 0] for i,val in enumerate(cc.tolist()) if val == cluster_ty ]
y= [coordinates[i, 1] for i,val in enumerate(cc.tolist()) if val == cluster_ty ]
(np.mean(x),np.mean(y))
Center = kmeans.cluster_centers_
# y_point = [coordinates[i][1] for i in range(len(coordinates)) ]
# x_point = [coordinates[i][0] for i in range(len(coordinates)) ]

# plt.scatter(x_point, y_point, c=cc, s=50, cmap='viridis')
# plt.xlim(min(coordinates[:, 0])*1.0001, max(coordinates[:, 0]*0.9999))
# plt.ylim(min(coordinates[:, 1])*1.001, max(coordinates[:, 1]*0.999))
ax.scatter(coordinates[:, 0], coordinates[:, 1], c=kmeans.predict(coordinates), s=num_clusters, cmap='viridis')
ax.scatter(Center[:, 0], Center[:, 1], marker='*', s=200, c=['red','orange','yellow','green','blue','white','purple'])
# #Plot clusters __center
# kmeans.
# plt.show()
# import geopandas
import matplotlib.lines as lines
# ax.lines([-87.87939476,  43.07645978], [-87.89377587,  43.05531122])
Center[0, 0]
ax.annotate('0-1', xy=(Center[0, 0],  Center[0, 1]), xytext=(Center[1, 0],  Center[1, 1]),
             arrowprops=dict(facecolor='red', shrink=0.5),
             )
ax.annotate('1-2', xy=(Center[1, 0],  Center[1, 1]), xytext=(Center[2, 0],  Center[2, 1]),
             arrowprops=dict(facecolor='red', shrink=0.5),
             )

plt.show()
fig.savefig(outfile03)


# df = geopandas.read_file(geopandas.datasets.get_path('nybb'))
# ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')

from geojson import Point, Feature, FeatureCollection, dump
### TO add classifier information into the GEOjson file or shape file
Len01 = len(data01['features'])
for i in range(Len01):
    data01['features'][i]['properties'].update({'class':'cluser_'+ str(cc[i])})

with open(outfile01, 'w') as f:
   dump(data01, f)

Len02 = len(cc) - Len01
for i in range(Len02):
    data02['features'][i]['properties'].update({'class':'cluser_'+ str(cc[i])})

with open(outfile02, 'w') as f:
   dump(data02, f)

dict_center ={}
for i in range(len(Center)):
    dict_center.update({'cluser_' + str(i) : Center[i].tolist() })

with open(outfile04, 'w') as f:
   json.dump(dict_center, f)
# import json
# with open('02_Origin.json','w') as f:
#     json.dump(data, f)