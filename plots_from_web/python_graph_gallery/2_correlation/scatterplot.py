# libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# change plot style
plt.style.use('ggplot')

# random dataset
df = pd.DataFrame({'x_values': range(1, 101), 'y_values': 15*np.random.randn(100) + range(1, 101)})

# plotting
plt.scatter('x_values', 'y_values', data=df)
plt.show()
