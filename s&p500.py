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


def output_data():
    data = pd.DataFrame()
    for industry in industries[:1]:
        tickers = info.loc[industry, ['Ticker symbol']]
        tickers = tickers['Ticker symbol'].tolist()
        prices_of_industry = prices[tickers]

        data['min'] = prices_of_industry.min(axis=1)
        data['max'] = prices_of_industry.max(axis=1)
        data['mean'] = prices_of_industry.mean(axis=1)

    return data
        #output = df with min max, mean, of every industry and sp500


print(output_data())

# Plot
data = output_data()

data.plot()
plt.show()
