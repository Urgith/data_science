# libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# random data
df = pd.DataFrame({'group': list(map(chr, range(65, 85))), 'values': np.random.uniform(size=20)})

# sorting
ordered_df = df.sort_values(by='values')
my_range = range(df.shape[0])

# plotting
plt.stem(ordered_df['values'])
plt.xticks(my_range, ordered_df['group'])
plt.show()
