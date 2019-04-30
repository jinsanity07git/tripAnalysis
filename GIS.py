import geopandas as gpd

# Set filepath (fix path relative to yours)
fp = "Data/MCTS Routes and Bus Stops - March 2019/AllRoutesMar19.shp"

# Read file using gpd.read_file()
data = gpd.read_file(fp)