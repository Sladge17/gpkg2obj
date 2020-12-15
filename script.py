# import fiona
import geopandas

countries_gdf = geopandas.read_file('/Users/jthuy/Desktop/BConv/engenier_network.gpkg')

print(countries_gdf.tail(291))


