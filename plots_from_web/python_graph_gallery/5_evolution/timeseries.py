# libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# graph style
plt.style.use('seaborn')

# random data
df = pd.DataFrame({'xvalues': range(1, 101), 'yvalues': np.random.randn(100)})

# plot
plt.plot('xvalues', 'yvalues', data=df)

# show the graph
plt.show()
