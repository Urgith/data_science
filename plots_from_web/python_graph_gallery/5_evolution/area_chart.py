# libraries
import matplotlib.pyplot as plt
import numpy as np

# data
x = np.arange(1, 6)
y = np.array([1, 4, 6, 8, 4])

# area plot
plt.fill_between(x, y)
plt.show()
