import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file

colors=['#0f0f0a', '#ff9966','#ba2a20', '#275597', '#8e43df', '#67d3b4', '#663300', '#006600','#a9d3d8','#e6e600','#b69cb4']
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
    title="Mean price of stocks from all sectors in S&P500 index")

p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Price'

for name, color in zip(industries, colors):
    p.line(datetime(sp500.index), sp500[name], alpha=0.8, color=color, line_width=3, legend=name)

p.line(datetime(sp500.index), sp500['S&P500'], line_width=5, color='red', legend='S&P500')

p.legend.location = "top_left"

# output_file("sp500_sectors_mean.html")

show(p)  # open a browser