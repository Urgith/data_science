# libraries
import networkx as nx
from nxviz import CircosPlot
import matplotlib.pyplot as plt

# initialize empty graph
g = nx.Graph()

# add edges to the graph
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(1, 5)
g.add_edge(2, 3)
g.add_edge(2, 7)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(5, 6)
g.add_edge(6, 7)

# create and display circos plot
c = CircosPlot(g)
plt.show()
