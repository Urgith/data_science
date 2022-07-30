# libraries
import matplotlib.pyplot as plt
import geopandas as gpd
import geoplot

# map of France
data = gpd.read_file('https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/france.geojson')

# creating map
geoplot.polyplot(data, projection=geoplot.crs.AlbersEqualArea(),
                 edgecolor='darkgrey', facecolor='lightgrey', linewidth=0.3)
plt.show()
