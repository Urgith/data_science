# libraries
import matplotlib.pyplot as plt
import seaborn as sns

# dark background
sns.set(style='dark')

# data
df = sns.load_dataset('iris')

# plotting
sns.boxplot(x=df['species'], y=df['sepal_length'])
plt.show()
