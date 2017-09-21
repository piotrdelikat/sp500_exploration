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

#Filternig missing tickers
data_present = prices.columns.tolist()
tickers = info[info['Ticker symbol'].isin(data_present)]

time_format = '%Y-%m-%d'
prices.index = pd.to_datetime(prices.index, format=time_format)
# Monthly
prices_monthly = prices.resample('M').mean()

sp500_mean = prices_monthly.mean(axis=1).to_frame(name="S&P500")

def output_data():
    data = pd.DataFrame()
    for industry in industries:
        global tickers
        ticks = tickers.loc[industry, ['Ticker symbol']]
        ticks = ticks['Ticker symbol'].tolist()

        prices_of_industry = prices_monthly[ticks]
        # data['min'] = prices_of_industry.min(axis=1)
        # data['max'] = prices_of_industry.max(axis=1)
        data['{}'.format(industry)] = prices_of_industry.mean(axis=1)

    return data
        #output = df with min max, mean, of every industry and sp500



data = output_data()


# To one DataFrame
# full_data = pd.concat([sp500_mean, data], axis='columns')
# full_data.to_csv('sp500_industries_mean.csv')


# Matplotlib Plot

for industry in data.columns.values:
    plt.plot(data[industry], label=industry)
plt.plot(sp500_mean, linewidth=3.0, color='r', label='S&P500')
plt.title('S&P500 mean vs. mean of Industries')
plt.legend()
plt.show()
