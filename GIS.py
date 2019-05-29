import geopandas
from descartes import PolygonPatch
# Set filepath (fix path relative to yours)
# fp = "Data/MCTS Routes and Bus Stops - March 2019/AllRoutesMar19.shp"

fp ='/Users/jinsanity/OneDrive - UWM/project/Taiyuan/太原卡口数据分析/taiyuan.shp'
# Read file using gpd.read_file()
data = geopandas.read_file(fp)

print (type(data))





import matplotlib.pyplot as plt
fig = plt.figure(figsize=(20,30)) 
fig, ax = plt.subplots(1, 1)

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
data.head()
data['sas'] =1

type(data['geometry'][1])


data.plot(column='卡口id', ax=ax, legend=True)

# fig.show()