# libraries
import matplotlib.pyplot as plt
from nxviz import annotate
import networkx as nx
import nxviz

# initialize empty graph
g = nx.Graph()

# add edges to graph
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 4)
g.add_edge(1, 5)

# draw graph
nxviz.ArcPlot(g)

# adds labels to nodes
annotate.arc_labels(g)

# show drawn graph
plt.show()
