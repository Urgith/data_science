# libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# create a dataset
df = pd.DataFrame(np.random.random((5, 5)), columns=['a', 'b', 'c', 'd', 'e'])

# heatmap
sns.heatmap(df)

# show plot
plt.show()
