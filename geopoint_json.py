import geopandas as gpd
import  json
from shapely.geometry import  mapping

input01 = 'inprocess_results/prowline stops.shp'

output01  = 'center_prowl.json'


gdf  =  gpd.read_file(input01)
# gdf['Name']
dict_center  = {}
for i in range(len(gdf)):
    dict_i =  mapping(gdf['geometry'][i])
    coord =  dict_i['coordinates']
    name = gdf['Name'][i]
    dict_center.update({name  : coord})
    
with open(output01, 'w') as f:
   json.dump(dict_center, f)