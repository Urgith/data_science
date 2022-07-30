# libraries
import matplotlib.pyplot as plt
import numpy as np

# create data
x = np.random.rand(40)
y = np.random.rand(40)
z = np.random.rand(40)

# plotting
plt.scatter(x, y, s=1000*z, alpha=0.5)
plt.show()
