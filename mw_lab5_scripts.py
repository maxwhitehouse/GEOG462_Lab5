# Lab 5 scripts
import os

import msw_lab5_functions as l5

#  Part 1:

#  Assign a variable to the Landsat file 


# Pass this to your new smart raster class



# Calculate NDVI and save to and output file

landsat_path = "Landsat_image_corv.tif"  # update with your actual filename
smart_raster = l5.SmartRaster(landsat_path)
ndvi = smart_raster.calculate_ndvi()
ndvi_output_path = "ndvi_output_test1.tif"
smart_raster.save_raster(ndvi, ndvi_output_path)






# Part 2:
# Assign a variable to the parcels data shapefile path


#  Pass this to your new smart vector class


#  Calculate zonal statistics and add to the attribute table of the parcels shapefile
import importlib
importlib.reload(l5)


vector_path = "Benton_County_TaxLots.shp"  # update with actual shapefile name
smart_vector = l5.SmartVector(vector_path)
smart_vector.calculate_zonal_stats(ndvi_output_path)
smart_vector.save_vector("taxlots_with_ndvi_test1.shp")




#  Part 3: Optional
#  Use matplotlib to make a map of your census tracts with the average NDVI values








# Simple Python script

# Print a greeting
print("Hello, world!")

# Calculate the sum of the first 10 positive integers
total = sum(range(1, 11))
print("The sum of the first 10 positive integers is:", total)

