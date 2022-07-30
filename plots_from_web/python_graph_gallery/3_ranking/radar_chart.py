# libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# data (only 1 for each is used now)
df = pd.DataFrame({
    'group': ['A', 'B', 'C', 'D'],
    'var1': [38, 1.5, 30, 4],
    'var2': [29, 10, 9, 34],
    'var3': [8, 39, 23, 24],
    'var4': [7, 31, 33, 14],
    'var5': [28, 15, 32, 14]
})

# number of variables
categories = list(df)[1:]
N = len(categories)

# something
values = df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]

# angle of each plot
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# initialize spider plot
ax = plt.subplot(111, polar=True)

# Draw one axe per variable + add labels
plt.xticks(angles[:-1], categories, color='grey', size=8)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([10, 20, 30], ['10', '20', '30'], color='grey', size=7)
plt.ylim(0, 40)

# plot data
ax.plot(angles, values, linewidth=1, linestyle='solid')

# fill area
ax.fill(angles, values, 'b', alpha=0.1)

# show plot
plt.show()
