# libraries
from bokeh.sampledata.les_mis import data
from bokeh.plotting import show
from holoviews import opts, dim
import holoviews as hv
import pandas as pd

# setting bokeh as backend
hv.extension('bokeh')

# data sets
links = pd.DataFrame(data['links'])
nodes = hv.Dataset(pd.DataFrame(data['nodes']), 'index')

# chord diagram
chord = hv.Chord((links, nodes), ).select(value=(5, None))
# diamgrams parameters
chord.opts(
    opts.Chord(
        cmap='Category20',
        edge_cmap='Category20',
        edge_color=dim('source').str(),
        node_color=dim('index').str(),
        labels='name',
    )
)

# render chord on internet browser
show(hv.render(chord))
