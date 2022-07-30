# libraries
import matplotlib.pyplot as plt
import seaborn as sns

# iris dataset
df = sns.load_dataset('iris')

# plotting
sns.pairplot(df)
plt.show(block=True)
