# libraries
from cartogram_geopandas import make_cartogram
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import numpy as np

# load the json file with county coordinates
geo_data = gpd.read_file('https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/US-counties.geojson')

# make sure that 'id' column is an integer
geo_data.id = geo_data.id.astype(str).astype(int)

# remove Alaska, Hawaii and Puerto Rico
state_to_remove = ['02', '15', '72']
geo_data = geo_data[~geo_data.STATE.isin(state_to_remove)]

# read file with unemployment rates
data = pd.read_csv('https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/unemployment-x.csv')

# merge geospatial and unemployment rate data
cartogram = geo_data.merge(data, left_on=['id'], right_on=['id'])

# create cartogram
n = 1
for i in range(n):
    cartogram = make_cartogram(cartogram, 'rate', 1)

# create ratio areas for every county
cartogram['area'] = cartogram['geometry'].area
sum_areas = cartogram['area'].sum()
cartogram['ratio_area'] = cartogram['area'].div(sum_areas)

# create ratio rate for every county
sum_rates = cartogram['rate'].sum()
cartogram['ratio'] = cartogram['rate'].div(sum_rates)

# error of cartogram map
cartogram['error'] = np.abs((cartogram['ratio_area'] / cartogram['ratio']) - 1)

# set colors for cartogram
jet = plt.get_cmap('jet')
cartogram['color'] = cartogram['error'].apply(lambda x: jet(x))

# plot cartogram
cartogram.plot(color=cartogram['color'])

# statistical summary
print(cartogram['error'].describe(percentiles=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.94, 0.97, 0.99, 0.995, 0.999, 0.9995, 0.9999]))

# axis is useless
plt.axis('off')
plt.show()
