# libraries
import matplotlib.pyplot as plt
import pandas as pd
import circlify

# data
df = pd.DataFrame({
    'Name': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Value': [10, 2, 23, 87, 12, 65]
})

# compute circle positions:
circles = circlify.circlify(
    df['Value'].tolist(),
    show_enclosure=False,
    target_enclosure=circlify.Circle(x=0, y=0, r=1)
)

# create figure with one subplot
fig, ax = plt.subplots(figsize=(10, 10))

# remove axes
ax.axis('off')

# find axis boundaries
lim = max(
    max(
        abs(circle.x) + circle.r,
        abs(circle.y) + circle.r
    )
    for circle in circles
)
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)

# plot circles
for circle in circles:
    x, y, r = circle

    ax.add_patch(plt.Circle((x, y), r, fill=False))

# show circles
plt.show()
