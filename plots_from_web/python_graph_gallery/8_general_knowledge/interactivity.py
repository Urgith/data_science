# libraries
import plotly.express as px

# LINE
# data
df = px.data.gapminder().query("continent=='Oceania'")

# interactive plot
fig = px.line(df, x='year', y='lifeExp', color='country')
fig.show()

# SCATTER
df = px.data.iris()

fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species',
                 size='petal_length', hover_data=['petal_width'])
fig.show()
