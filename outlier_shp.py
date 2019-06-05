
import pandas as pd
import geopandas
# from shapely.geometry import Point
# from shapely.geometry import MultiPoint
from shapely.geometry import  mapping

path = '/Users/jinsanity/OneDrive - UWM/Documents/CIV790/GIS_campus/outlier.shp'

gdf =  geopandas.read_file(path)

gdf['Place']