# libraries
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# data
x = np.arange(1990, 2020)
y = [np.random.randint(0, 5, size=30) for _ in range(5)]

# stackplot
fig, ax = plt.subplots(figsize=(10, 7))
ax.stackplot(x, y)
plt.show()

# baseline change
fig, ax = plt.subplots(figsize=(10, 7))
ax.stackplot(x, y, baseline='sym')
ax.axhline(0, color='black', ls='--')
plt.show()

# smoothing function
def gaussian_smooth(x, y, sd):
    weights = np.array([stats.norm.pdf(x, m, sd)for m in x])
    weights = weights / weights.sum(1)
    return (weights * y).sum(1)

# smoothed plot
fig, ax = plt.subplots(figsize=(10, 7))
y_smoothed = [gaussian_smooth(x, y_, 1) for y_ in y]
ax.stackplot(x, y_smoothed, baseline='sym')
plt.show()
