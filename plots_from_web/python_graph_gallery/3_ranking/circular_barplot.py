# libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# build a dataset
df = pd.DataFrame(
    {
        'Name': ['item' + str(i) for i in range(1, 51)],
        'Value': np.random.randint(low=10, high=100, size=50)
    }
)

# set coordinates limits
upperlimit = 100
lowerlimit = 30

# compute max and min in the dataset
maximum = df['Value'].max()

# compute heights into lowerlimit-upperlimit
slope = (maximum - lowerlimit) / maximum
heights = slope*df.Value + lowerlimit

# width of each bar
width = 2*np.pi / df.shape[0]

# compute the angle each bar is centered od
angles = [element * width for element in range(1, df.shape[0] + 1)]

# initialize polar plot
plt.subplot(111, polar=True)
# plot polar bar
plt.bar(
    x=angles,
    height=heights,
    width=width,
    bottom=lowerlimit,
    linewidth=2,
    edgecolor='k'
)
# remove axis
plt.axis('off')
# show plot
plt.show()
