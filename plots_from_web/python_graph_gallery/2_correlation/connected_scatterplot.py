# libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# data
df = pd.DataFrame({
    'x_axis': range(1, 10),
    'y_axis': 80*np.random.rand(9) + range(1, 10)
})

# plot
plt.plot('x_axis', 'y_axis', data=df, marker='o')
plt.show()
