import numpy as np
import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show, output_file

sp500 = pd.read_csv('sp500_industries_mean.csv',  index_col=0)

time_format = '%Y-%m-%d'
sp500.index = pd.to_datetime(sp500.index, format=time_format)

all = sp500['S&P500']

data = dict(
    sp500 = all
)

# for industry in sp500.columns.values[1:]:
#     data['{}'.format(industry)] = sp500[industry]


source = ColumnDataSource(data=data)

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


p.line(datetime(sp500.index), all, color='#A6CEE3', legend='S&P500 mean stock price')
p.legend.location = "top_left"

# output_file("sp500_mean.html", title="")

show(p)  # open a browser