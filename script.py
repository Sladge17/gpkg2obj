# import fiona
# import geopandas

# countries_gdf = geopandas.read_file('/Users/jthuy/Desktop/BConv/engenier_network.gpkg')

# print(countries_gdf.tail(291))

import os

path = "/Users/jthuy/Desktop/BConv/"
file = "engenier_network.gpkg"

if not os.path.isdir(path + "result"):
	os.mkdir(path + "result")
