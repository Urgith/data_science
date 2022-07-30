# libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# getting the data
temp = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2016-weather-data-seattle.csv')
temp['month'] = pd.to_datetime(temp['Date']).dt.month

# month column creation
month_dict = {
    1: 'january',
    2: 'february',
    3: 'march',
    4: 'april',
    5: 'may',
    6: 'june',
    7: 'july',
    8: 'august',
    9: 'september',
    10: 'october',
    11: 'november',
    12: 'december'
}
temp['month'] = temp['month'].map(month_dict)

# calculate mean temperature for each month
month_mean_serie = temp.groupby('month')['Mean_TemperatureC'].mean()
temp['mean_month'] = temp['month'].map(month_mean_serie)

# prepare plot
g = sns.FacetGrid(temp, row='month', hue='mean_month', aspect=15, height=0.75)

# densities kdeplots for each month
g.map(sns.kdeplot, 'Mean_TemperatureC', fill=True)

for i, ax in enumerate(g.axes.flat):
    ax.text(-15, 0.02, month_dict[i+1],
            fontweight='bold', fontsize=15)

g.figure.subplots_adjust(hspace=0)
g.set_titles('')
g.set(yticks=[], ylabel='')
g.despine(bottom=True, left=True)

# show plot
plt.show(block=True)
