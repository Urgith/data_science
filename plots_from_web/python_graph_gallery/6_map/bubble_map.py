# libraries
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd

# read the data
data = pd.read_csv('https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/TweetSurfData.csv', sep=';')

# set the size of the figure
plt.rcParams['figure.figsize'] = (15, 10)

# make the background map
m = Basemap(llcrnrlon=-180, llcrnrlat=-65, urcrnrlon=180, urcrnrlat=80)
m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
m.fillcontinents(color='grey', alpha=0.3)
m.drawcoastlines(linewidth=0.1, color='white')

# prepare a color for each point depending on the continent
data['labels_enc'] = pd.factorize(data['homecontinent'])[0]

# add point per position
m.scatter(
    x=data['homelon'],
    y=data['homelat'],
    s=data['n'] / 6,
    alpha=0.4,
    c=data['labels_enc'],
    cmap='Set1'
)

# copyright and source data info
plt.text(-175, -62,
         'Where people talk about #surf\n\nData collected on twitter by @R_Graph_Gallery during 300 days\nPlot realized with Python and the Basemap library',
         ha='left', va='bottom', size=9, color='#555555')

plt.show()
