# libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# set seaborn style
sns.set_theme()

# data
values = np.cumsum(np.random.randn(1000, 1))

# plotting
plt.plot(values)
plt.show()
