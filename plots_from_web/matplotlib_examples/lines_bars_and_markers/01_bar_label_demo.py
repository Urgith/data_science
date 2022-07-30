# libraries
import matplotlib.pyplot as plt
import numpy as np

# define the data
N = 5
men_means = (20, 35, 30, 35, -27)
women_means = (25, 32, 34, 20, -25)
men_std = (2, 3, 4, 1, 2)
women_std = (3, 5, 2, 3, 3)
ind = np.arange(N)  # the x locations for the groups
width = 0.35        # the width of the bars: can also be len(x) sequence

# ---------- stacked bar plot with error bars ----------
fig, ax = plt.subplots()

p1 = ax.bar(ind, men_means, width, yerr=men_std, label='Men')
p2 = ax.bar(ind, women_means, width, bottom=men_means, yerr=women_std, label='Women')

ax.axhline(0, color='grey', linewidth=0.8)
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
ax.legend()

# labels with label_type 'center' instead of the default 'edge'
ax.bar_label(p1, label_type='center')
ax.bar_label(p2, label_type='center')
ax.bar_label(p2)

plt.show()

# ---------- horizontal bar chart ----------
np.random.seed(19680801)

# example data
people = ('Tom', 'Dick', 'Marry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10*np.random.rand(len(people))
error = np.random.rand(len(people))

fig, ax = plt.subplots()

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()   # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

# label with specially formatted floats
ax.bar_label(hbars, fmt='%.2f')
ax.set_xlim(right=15)   # adjust xlim to fit labels

plt.show()

# ---------- some of the more advanced things that one can do with bar labels ----------

fig, ax = plt.subplots()

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis() # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

# label with given captions, custom padding and annotate options
ax.bar_label(hbars, labels=[f'±{np.round(e, 2)}' for e in error],
             padding=8, color='b', fontsize=14)
ax.set_xlim(right=16)

plt.show()
