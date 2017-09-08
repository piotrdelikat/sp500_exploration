import pandas as pd

def table_to_pickle():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url,skiprows=0 ,header=0, index_col=3)
    df = pd.DataFrame(html[0])
    df.to_pickle('sp500_companies.pickle')

#Call function if you need reload data to pickle
# table_to_pickle()

#Preparing data
info = pd.read_pickle('sp500_companies.pickle')
prices = pd.read_csv('sp500_joined_closes.csv', index_col=0)

time_format = '%Y-%m-%d'
prices.index = pd.to_datetime(prices.index, format=time_format)
# Monthly
prices_monthly = prices.resample('M').mean()
# Industries tickers
industry = info.loc['Information Technology',['Ticker symbol']]
tickers = industry['Ticker symbol'].tolist()

prices_of_industry = prices[tickers]

# max and min for visualisation
data = pd.DataFrame()
# data[max] =
# data[min] =


