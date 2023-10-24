# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 16:37:53 2023

@author: Carmen
"""
###############################################################################
#   INPUT AND OTHER PREPARATIONS
###############################################################################
import pandas as pd
# Load data
df = pd.read_csv('data_index_2.csv')

# Input
bad_input = df['ISO3'] == '\'MEX\''

# Bad longitude, latitude and biome from input
bad_df = df[bad_input == True]
bad_long = bad_df['Lon']
bad_lat = bad_df['Lat']
bad_biome = bad_df['Biome_obs']

import geopandas as gpd
from shapely.geometry import Point

# Combine longitude and latitude into a GeoDataFrame
bad_geom = [Point(lon, lat) for lon, lat in zip(bad_long, bad_lat)]
bad_gdf = gpd.GeoDataFrame(bad_df, geometry=bad_geom)

biome_colors = {
    1: (0.5, 1, 1),    # Red
    2: (0, 0.6, 0.6),    # Blue
    3: (0.31, 0.94, 0.65),    # Green
    4: (0.8, 1, 0.84),
    5: (0.45, 1, 0),
    6: (0.1, 0.49, 0.73),
    7: (0.55, 0.71, 0),
    8: (0.05, 0.85, 0.25),
    9: (0, 0.55, 0.2),
    10: (0.78, 0.53, 0.14),
    11: (0.8, 1, 0),
    12: (0.85, 0.7, 0),
    13: (0.98, 0.78, 0),
    14: (1, 0.88, 0.41),
    15: (1, 0.29, 0.6),
    16: (0.94, 1, 0.9),
    17: (1, 1, 0.7),
    18: (0.8, 0.8, 1)
    # Add more colors for other biomes using RGB values
}

###############################################################################
#   3.4: PLOT OF LOCATIONS WHOSE BIOME WAS PREDICTED WRONGlY
###############################################################################
import geopandas as gpd
import matplotlib.pyplot as plt

# Create a base map
fig, ax = plt.subplots(figsize=(12, 12),dpi=300)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

  
#Now We crop the world to focus on the locations whose biome was predicted wrongly
ax.set_xlim((min(bad_long),max(bad_long))) #Longitude
ax.set_ylim((min(bad_lat),max(bad_lat))) #Latitude

ax = world.plot(ax=ax, color='white', edgecolor='black')
plt.xlabel('Longitude')
plt.ylabel('Latitude')


    
# Plot points with different colors based on bad_biome
for b in set(bad_biome):
    bad_gdf_b = bad_gdf[bad_gdf['Biome_obs'] == b]
    bad_gdf_b.plot(ax=ax, color=biome_colors[b], label=f'Biome_obs {b}', markersize=5)
    
# Show the map
plt.show()
plt.savefig('test3.4_map.png', dpi=300, bbox_inches='tight')

###############################################################################
#   4.6: I WOULD NEED TO KNOW BETTER WHAT YOU WANT TO BE SHOWN HERE
###############################################################################


###############################################################################
#   5.3: SAME HERE
###############################################################################
