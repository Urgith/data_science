# libraries
import matplotlib.pyplot as plt

# different style
plt.style.use('dark_background')

# data and bins
hours = [17, 20, 22, 25, 26, 27, 30, 31, 32, 38, 40, 40, 45, 55]
bins = [10, 20, 30, 40, 50, 60]

# plot
plt.hist(hours, bins=bins, edgecolor='k')
plt.show()
