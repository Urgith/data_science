# libraries
import matplotlib.pyplot as plt

# data
size_of_groups = [12, 11, 3, 30]

# plotting pie chart
plt.pie(size_of_groups)

# adding circle
plt.gca().add_artist(plt.Circle((0, 0), 0.7, color='white'))

# showing plot
plt.show()
