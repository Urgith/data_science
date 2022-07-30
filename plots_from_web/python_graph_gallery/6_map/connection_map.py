# libraries
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd

# set the plot size
plt.rcParams['figure.figsize'] = (15, 12)

# a basic map
m = Basemap(llcrnrlon=-100, llcrnrlat=20, urcrnrlon=30, urcrnrlat=70, projection='merc')
m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
m.fillcontinents(color='grey', alpha=0.7, lake_color='grey')
m.drawcoastlines(linewidth=0.1, color='white')

# add a connection between New York and London
startlat = 40.78
startlon = -73.98
arrlat = 51.53
arrlon = 0.08
m.drawgreatcircle(startlon, startlat, arrlon, arrlat, linewidth=2, color='orange')
plt.show()

# creating dataframe with list of a few cities and their coordinates
cities = {
    'city': ['Paris', 'Melbourne', 'Saint.Petersburg', 'Abidjan',
             'Montreal', 'Nairobi', 'Salvador'],
    'lon': [2, 145, 30.32, -4.03, -73.57, 36.82, -38.5],
    'lat': [49, -38, 59.93, 5.33, 45.52, -1.29, -12.97]
}

df = pd.DataFrame(cities, columns=['city', 'lon', 'lat'])

# background map
m = Basemap(llcrnrlon=-179, llcrnrlat=-60, urcrnrlon=179, urcrnrlat=70, projection='merc')
m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
m.fillcontinents(color='#f2f2f2', alpha=0.7)
m.drawcoastlines(linewidth=0.2, color='white')

# loop on every pair of cities to add the connection
for start_index, start_row in df.iterrows():
    for end_index in range(start_index + 1, df.shape[0]):
        end_row = df.iloc[end_index]
        m.drawgreatcircle(start_row.lon, start_row.lat, end_row.lon, end_row.lat,
                          linewidth=1, color='#69b3a2')

# add city names
for i, row in df.iterrows():
    plt.annotate(row.city, xy=m(row.lon + 3, row.lat), va='center')

# show connections map
plt.show()
