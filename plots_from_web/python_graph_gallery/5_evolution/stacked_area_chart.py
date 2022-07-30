# libraries
import matplotlib.pyplot as plt
import numpy as np

# create data
x = range(1, 6)
y1 = [1, 4, 6, 8, 9]
y2 = [2, 2, 7, 10, 12]
y3 = [2, 8, 5, 10, 6]

# basic stacked area chart
plt.stackplot(x, y1, y2, y3, labels=['A', 'B', 'C'])

# add legend
plt.legend(loc='upper left')

# show chart
plt.show()
