# libraries
import matplotlib.pyplot as plt
import pandas as pd
import squarify

# create data frame with fake data
df = pd.DataFrame({
    'nb_people': [8, 3, 4, 2],
    'group': ['group A', 'group B', 'group C', 'group D']
})

# plot squarified data
squarify.plot(sizes=df['nb_people'], label=df['group'])

# turn off axis
plt.axis('off')

# show squarified plot
plt.show()
