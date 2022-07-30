# libraries
import matplotlib.pyplot as plt
import numpy as np

# better chart style
plt.style.use('fivethirtyeight')

# data
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))

# bars
plt.bar(y_pos, height)

# names
plt.xticks(y_pos, bars)

# show chart
plt.show()
