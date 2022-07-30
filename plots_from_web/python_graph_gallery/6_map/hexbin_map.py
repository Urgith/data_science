# libraries
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd

# set the plot size
plt.rcParams['figure.figsize'] = (13, 13)

# load file
url = 'https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/us_states_hexgrid.geojson.json'
geo_data = gpd.read_file(url)

# draw a map with matplotlib
geo_data.plot(color='white', edgecolor='black', linewidth=0.5)
plt.axis('off')
plt.show()

# add a 'centroid' column with the centroid position of each state
geo_data['centroid'] = geo_data['geometry'].apply(lambda x: x.centroid)

# redraw the empty hexbin map:
geo_data.plot(color='white', edgecolor='black', linewidth=0.5)
plt.axis('off')

# for each state, annotate with the state name located at the centroid coordinates
for idx, row in geo_data.iterrows():
    plt.annotate(text=row['iso3166_2'], xy=row['centroid'].coords[0], horizontalalignment='center', va='center')

plt.show()

# read the mariage date stored on github
mariage_data = pd.read_csv('https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/State_mariage_rate.csv')
print(geo_data.columns)
# add a new column to the geo dataframe that will be used for joining
geo_data['state'] = geo_data['google_name'].str.replace(' \(United States\)', '')

# merge the mariage dataset with geospatial information
geo_data = geo_data.set_index('state').join(mariage_data.set_index('state'))

# create map
geo_data.plot(column='y_2015', cmap='viridis')
plt.show()

# initialize a new figure
fig, ax = plt.subplots(1, figsize=(13, 13))

# map states with the right color
geo_data.plot(ax=ax, column='y_2015', cmap='BuPu',
              norm=plt.Normalize(vmin=2, vmax=13),
              edgecolor='black', linewidth=0.5)

# remove useless axis
ax.axis('off')

# add title, subtitle and author
ax.annotate('Marriage rate in the US', xy=(10, 600), xycoords='axes pixels',
            ha='left', va='top', fontsize=14, color='black')
ax.annotate('Yes, people love to get married is Vegas', xy=(10, 580),
            xycoords='axes pixels', ha='left', va='top', fontsize=11,
            color='#808080')
ax.annotate('python-graph-gallery.com', xy=(700, 0), xycoords='axes pixels',
            ha='left', va='top', fontsize=8, color='#808080')

# for each state, annotate with the state name located at the centroid coordinates
for idx, row in geo_data.iterrows():
    ax.annotate(
        text=row['iso3166_2'],
        xy=row['centroid'].coords[0],
        ha='center',
        va='center',
        color='white'
    )

# add color bar
sm = plt.cm.ScalarMappable(cmap='BuPu', norm=plt.Normalize(vmin=2, vmax=13))
fig.colorbar(sm, orientation='horizontal', aspect=50, fraction=0.005, pad=0)

# display map
plt.show()
