#data after pd.read ...
#bool data like in bool_bad_data_index_2 = data_index_2['ISO3'] == 'MEX'
def map(data, bool_bad_data, biome_type, plot_name):
    # Bad longitude, latitude and biome from input
    bad_data = data[bool_bad_data == True]
    bad_long = bad_data['Lon']
    bad_lat = bad_data['Lat']
    bad_biome = bad_data[biome_type]
    
    # Combine longitude and latitude into a GeoDataFrame
    bad_geom = [Point(lon, lat) for lon, lat in zip(bad_long, bad_lat)]
    bad_gdf = gpd.GeoDataFrame(bad_data, geometry=bad_geom)
    
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
    }
    
    # Create a base map
    fig, ax = plt.subplots(figsize=(12, 12),dpi=300)
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
     
    #Now we crop the world to focus on the locations whose biome was predicted wrongly
    ax.set_xlim((min(bad_long),max(bad_long))) #Longitude
    ax.set_ylim((min(bad_lat),max(bad_lat))) #Latitude
    
    ax = world.plot(ax=ax, color='white', edgecolor='black')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
       
    # Plot points with different colors based on bad_biome
    for b in set(bad_biome):
        bad_gdf_b = bad_gdf[bad_gdf['Biome_obs'] == b]
        bad_gdf_b.plot(ax=ax, color=biome_colors[b], label=f'Biome_obs {b}', 
                       marker= 's', markersize=5)
     
    # Store and show the map
    plt.savefig('../plots/' + plot_name, dpi=300, bbox_inches='tight')
    plt.show()
    
def save_plot(figure, figurename = 'my_plot'):
    figure.savefig('../plots/' + figurename + '.pdf', bbox_inches='tight')
    
def stats(data, bool_data=False, name_data, head=False, describe=False, bool_data=False, 
          hists=False, hists_hue=False, dens_hists=False, dens_hists=False, scatts=False, groupby=False):
    
    if bool_data != False:
        data = data[bool_data == True]
    
    #head
    if head == True:
        data.head()
    
    #count, mean, std, min, 25%, 50%, 75%, max
    if describe == True:
        print(data.describe())
    
    #histogram(s)
    hists != False:
        for obs_data in hists: #['Lon','Lat','clay'] for example
            fig, ax = plt.subplots() #figsize = (8,4)
            ax = sns.histplot(data, x = obs_data)
            save_plot(fig, figurename = 'histplot_' + name_data + '_' + obs_data)
    
    #histogram(s) with hue
    hists_hue != False:
        for obs_data in hists_hue: #[('Lon','Lat'), ('clay','silt')] for example
            fig, ax = plt.subplots() #figsize = (8,4)
            ax = sns.histplot(data, x = obs_data[0], hue = obs_data[1])
            save_plot(fig, figurename = 'hist_hue_plot_' + name_data + '_' + obs_data[0] + '_' + obs_data[1])
    
    #density histogram(s)
    dens_hists != False:
        for obs_data in dens_hists: #['Lon','Lat','clay','silt'] for example
            fig, ax = plt.subplots() #figsize = (8,4)
            ax = sns.histplot(data, x = obs_data, stat = "density", kde = True)
            save_plot(fig, figurename = 'dens_histplot_' + name_data + '_' + obs_data)
    
    
    #scatterplot(s)
    scatts != False:
        for obs_data in scatts: #[('Lon','Lat'), ('clay','silt')] for example
            fig, ax = plt.subplots()
            ax = sns.scatterplot(data, x = obs_data[0], y = obs_data[1])
            save_plot(fig, figurename = 'scatterplot_' + name_data + '_' + obs_data[0] + '_' + obs_data[1])
    
            
    #scatterplot(s) with hue
    scatts != False:
        for obs_data in scatts: #[('Lon','Lat', 'clay')] for example, order is x,y,hue
            fig, ax = plt.subplots()
            ax = sns.scatterplot(data, x = obs_data[0], y = obs_data[1], hue = obs_data[2])
            save_plot(fig, figurename = 'scatter_hue_plot_' + name_data + '_' + obs_data[0] + '_' + obs_data[1] + '_' + obs_data[2])
    
    #describe with groupby
    if groupby != False:
        print(data.groupby(groupby).describe.transpose())