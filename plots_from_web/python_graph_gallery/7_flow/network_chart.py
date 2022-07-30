# libraries
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

# dataframe with connections
df = pd.DataFrame({
    'from': ['A', 'B', 'C', 'A'],
    'to': ['D', 'A', 'E', 'C']
})

# build graph
G = nx.from_pandas_edgelist(df, 'from', 'to')

# plot graph
nx.draw(G, with_labels=True)
plt.show()
