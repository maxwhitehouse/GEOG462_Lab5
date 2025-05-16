# Lab 5 scripts
import os

import msw_lab5_functions as l5

#  Part 1:


print("VSCode is running Python!")

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

import matplotlib.pyplot as plt

# Optional: set style
plt.style.use('ggplot')

# Plot the tax lots with NDVI values
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the GeoDataFrame with NDVI color scale
smart_vector.gdf.plot(
    column="ndvi_mean",         # the field with zonal stats
    ax=ax,
    legend=True,                # show colorbar
    cmap="YlGn",                # colormap (Yellow-Green)
    edgecolor="black",          # outlines
    linewidth=0.2,              # thin borders
    missing_kwds={              # styling for missing data
        "color": "lightgrey",
        "label": "No Data"
    }
)

# Add title and axes off
ax.set_title("Benton County Tax Lots\nAverage NDVI by Parcel", fontsize=14)
ax.axis("off")

# Save the figure (optional)
plt.savefig("ndvi_taxlots_map.png", dpi=300)
plt.show()





# Simple Python script

# Print a greeting
print("Hello, world!")

# Calculate the sum of the first 10 positive integers
total = sum(range(1, 11))
print("The sum of the first 10 positive integers is:", total)

