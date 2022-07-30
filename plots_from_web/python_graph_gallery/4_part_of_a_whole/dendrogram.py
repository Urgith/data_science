# libraries
from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
import numpy as np

# understandable version
ytdist = [[662], [877], [255], [412], [996], [295], [468], [268],
          [400], [754], [564], [138], [219], [869], [669]]

# ? version
ytdist = np.array([662, 877, 255, 412, 996, 295, 468, 268,
                   400, 754, 564, 138, 219, 869, 669])

# creating dendrogram
Z = hierarchy.linkage(ytdist, 'single')
dn = hierarchy.dendrogram(Z)

# show dendrogram
plt.show()
