# libraries
import matplotlib.pyplot as plt
import seaborn as sns

# change chart style
plt.style.use('ggplot')

# data
df = sns.load_dataset('iris')

# plotting
sns.violinplot(x=df['species'], y=df['sepal_length'])
plt.show()
