# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patheffects


fig, ax = plt.subplots(figsize=(6, 6))
ax.plot([0, 1], [0, 1], label='line',
        path_effects=[patheffects.withTickedStroke(spacing=7, angle=135)])

nx = 101
x = np.linspace(0, 1, nx)
y = 0.3*np.sin(8 * x) + 0.4
ax.plot(x, y, label='Curve', path_effects=[patheffects.withTickedStroke()])

ax.legend()

plt.show()
