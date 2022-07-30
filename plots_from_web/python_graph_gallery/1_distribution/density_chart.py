# libraries
import matplotlib.pyplot as plt
import seaborn as sns

# other seaborn style
sns.set(style='darkgrid')

# data
df = sns.load_dataset('iris')

# plotting [kernel density estimation]
sns.kdeplot(df['sepal_width'])
plt.show()
