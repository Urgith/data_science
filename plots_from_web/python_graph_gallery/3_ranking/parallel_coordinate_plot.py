# libraries
from pandas.plotting import parallel_coordinates
import matplotlib.pyplot as plt
import seaborn as sns

# take the iris dataset
data = sns.load_dataset('iris')

# make plot
parallel_coordinates(data, 'species', colormap=plt.get_cmap('Set1'))
plt.show()
