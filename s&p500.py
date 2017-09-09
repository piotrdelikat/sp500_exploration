import pandas as pd
import matplotlib.pyplot as plt
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
industries = info.index.drop_duplicates().tolist()


time_format = '%Y-%m-%d'
prices.index = pd.to_datetime(prices.index, format=time_format)
# Monthly
prices_monthly = prices.resample('M').mean()
# Industries tickers
industry = info.loc['Information Technology',['Ticker symbol']]
tickers = industry['Ticker symbol'].tolist()

prices_of_industry = prices[tickers]

data = pd.DataFrame()
data['min'] = prices_of_industry.min(axis=1)
data['max'] = prices_of_industry.max(axis=1)
data['mean'] = prices_of_industry.mean(axis=1)

# Plot
data.plot()
plt.show()
