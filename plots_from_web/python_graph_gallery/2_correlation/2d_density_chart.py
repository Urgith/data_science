# libraries
import matplotlib.pyplot as plt
import numpy as np

# create data
x = np.random.normal(size=50_000)
y = 3*x + np.random.normal(size=50_000)

# big bins
plt.hist2d(x, y, bins=(50, 50), cmap=plt.cm.jet)
plt.show()

# small bins
plt.hist2d(x, y, bins=(300, 300), cmap=plt.cm.jet)
plt.show()

# without setting the same value for X and Y, bins won't be a square!
plt.hist2d(x, y, bins=(300, 30), cmap=plt.cm.jet)
plt.show()
