import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file

colors=['#1a3309', '#2153bd','#ba2a20', '#275597', '#8e43df', '#67d3b4', '#b3f2c7', '#9faa92','#a9d3d8','#3b7624','#b69cb4','#c8cf46']

sp500 = pd.read_csv('sp500_industries_mean.csv',  index_col=0)

time_format = '%Y-%m-%d'
sp500.index = pd.to_datetime(sp500.index, format=time_format)


def datetime(x):
    return np.array(x, dtype=np.datetime64)


p = figure(
    plot_width=1100,
    plot_height=700,
    responsive=True,
    x_axis_type="datetime",
    title="S&P500 mean vs. mean of Industries")


p.xaxis.axis_label = 'Date'
p.yaxis.axis_label = 'Price'


for i, industry in enumerate(sp500.columns.values[1:]):
    p.line(datetime(sp500.index), sp500['{}'.format(industry)], color=colors[i], legend='{}'.format(industry))
    # data['{}'.format(industry)] = sp500[industry]

p.legend.location = "top_left"

# output_file("sp500_mean.html", title="")

show(p)  # open a browser