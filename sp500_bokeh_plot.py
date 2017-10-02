import numpy as np
import pandas as pd
from bokeh.models import Legend
from bokeh.layouts import layout
from bokeh.plotting import figure, show, output_file

colors=['#0f0f0a', '#ff9966','#ba2a20', '#275597', '#8e43df', '#67d3b4', '#663300', '#006600','#a9d3d8','#e6e600','#b69cb4']
legend_items = []
sp500 = pd.read_csv('sp500_industries_mean.csv',  index_col=0)

time_format = '%Y-%m-%d'
sp500.index = pd.to_datetime(sp500.index, format=time_format)
industries = sp500.columns.values[1:]

def datetime(x):
    return np.array(x, dtype=np.datetime64)

p = figure(
    plot_width=1100,
    plot_height=600,
    responsive=True,
    x_axis_type="datetime",
    title="Mean price of stocks from all sectors in S&P500 index",
    toolbar_location="below",
    toolbar_sticky=False
)

p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Price'

for name, color in zip(industries, colors):
    plot = p.line(datetime(sp500.index), sp500[name], line_width=3, line_color=color)
    legend_items.append((name, [plot]))

index = p.line(datetime(sp500.index), sp500['S&P500'], line_width=5, line_color='red')
legend_items.append(('S&P500', [index]))

legend = Legend(items=legend_items, location=(0, -30))
p.add_layout(legend, 'right')

# output_file("sp500_sectors_mean.html")

show(p)  # open a browser