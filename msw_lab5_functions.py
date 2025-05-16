#####################
# Block 1:  Import the packages you'll need
# 
# 

import os, sys
import rasterio
import geopandas as gpd
import numpy as np
from rasterstats import zonal_stats 


##################
# Block 2: 
# set the working directory to the directory where the data are

# Change this to the directory where your data are

data_dir = r"R:\2025\Spring\GEOG562\Students\whitehom\Lab5"
os.chdir(data_dir)
print(os.getcwd())


##################
# Block 3: 
#   Set up a new smart raster class using rasterio  
#    that will have a method called "calculate_ndvi"


class SmartRaster:
    def __init__(self, raster_path):
        self.raster_path = raster_path
        self.dataset = rasterio.open(raster_path)
        self.meta = self.dataset.meta

    def calculate_ndvi(self, nir_band=4, red_band=3):
        """Calculate NDVI from NIR and Red bands (1-indexed)."""
        nir = self.dataset.read(nir_band).astype(float)
        red = self.dataset.read(red_band).astype(float)
        ndvi = (nir - red) / (nir + red + 1e-6)
        return ndvi

    def save_raster(self, array, output_path):
        """Save array as raster using original metadata."""
        meta = self.meta.copy()
        meta.update(dtype=rasterio.float32, count=1)
        with rasterio.open(output_path, 'w', **meta) as dst:
            dst.write(array.astype(rasterio.float32), 1)
            print(f"Saved output to {output_path}")









##################
# Block 4: 
#   Set up a new smart vector class using geopandas
#    that will have a method similar to what did in lab 4
#    to calculate the zonal statistics for a raster
#    and add them as a column to the attribute table of the vector




class SmartVector:
    def __init__(self, vector_path):
        self.vector_path = vector_path
        self.gdf = gpd.read_file(vector_path)

    def calculate_zonal_stats(self, raster_path, stats=["mean"], stat_column_name="ndvi_mean"):
        """Add zonal statistics to attribute table."""
        zs = zonal_stats(self.vector_path, raster_path, stats=stats)
        self.gdf[stat_column_name] = [z[stats[0]] if z else None for z in zs]
        print(f"Added zonal stats to GeoDataFrame under '{stat_column_name}'")

    def save_vector(self, output_path):
        try:
            self.gdf.to_file(output_path)
            print(f"✅ Shapefile saved successfully to: {os.path.abspath(output_path)}")
        except Exception as e:
            print(f"❌ Failed to save shapefile. Error: {e}")
