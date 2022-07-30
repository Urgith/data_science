# import libraries
import matplotlib.pyplot as plt
import mapclassify as mc
import geopandas as gpd
#import seaborn as sns
import pandas as pd
import geoplot

# load the json file with county coordinates
geo_data = gpd.read_file('https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/US-counties.geojson')

# make sure that 'id' column is an integer
geo_data.id = geo_data.id.astype(str).astype(int)

# remove Alaska, Hawaii and Puerto Rico
state_to_remove = ['02', '15', '72']
geo_data = geo_data[~geo_data.STATE.isin(state_to_remove)]

# bacis plot with just county outlines
#geoplot.polyplot(geo_data)
#plt.show()

# read file with unemployment rates
data = pd.read_csv('https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/unemployment-x.csv')

# show the histribution of unemployment rate
#sns.histplot(data['rate'])
#plt.show()

# merge geospatial and unemployment rate data
full_data = geo_data.merge(data, left_on=['id'], right_on=['id'])

# set up the color sheme
scheme = mc.Quantiles(full_data['rate'], k=10)

fig, ax = plt.subplots(1, 1, figsize=(16, 12))

# create choropleth map
geoplot.choropleth(full_data, hue='rate', linewidth=0.5, scheme=scheme, cmap='inferno_r', legend=True, edgecolor='black', ax=ax)
ax.set_title('Unemployment rate in US counties', fontsize=13)

plt.show()
