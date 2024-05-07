#authors: Fergus Mcclean, Chris Iliadis
#host: Newcastle University
import geopandas as gpd
from citycatio.utils import geoseries_to_string
import os

class SpatialRainfall:
    """Areas representing different spatial rainfall

    Args:
        data: Table containing spatial rainfall polygons

    """
    def __init__(self, data: gpd.GeoDataFrame):
        assert type(data) == gpd.GeoDataFrame
        self.data = data

    def write(self, path):
        with open(os.path.join(path, 'Rainfall_polygons.txt'), 'w') as f:
            f.write(geoseries_to_string(self.data.geometry))

input_folder = r'C:\Users\steve\Documents\citycat\SpatialRainfall/'
name_shp_file = 'SpatialRainfall-test'

gdf = gpd.read_file(input_folder + name_shp_file + '.shp')
SpatialRainfall(gdf).write('.')

# Just printing the output of the file to show what's in it
with open('Rainfall_polygons.txt') as f:
  print(*f.readlines()[:10])