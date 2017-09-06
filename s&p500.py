import pandas as pd

def table_to_pickle():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url,skiprows=0 ,header=0, index_col=3)
    df = pd.DataFrame(html[0])
    df.to_pickle('sp500_companies.pickle')

#Call function if you need reload data to pickle
# table_to_pickle()

#print(df.head())
# names_categories = sector.loc[['Information Technology']]

df = pd.read_pickle('sp500_companies.pickle')

data = df[['GICS Sub Industry', 'Ticker symbol', 'Security']]
print(df.head())
# print(df.loc['Information Technology', ['Ticker symbol', 'Security', 'GICS Sub Industry']])
# print(data.loc['Information Technology'])


#print(df.loc['Information Technology',["Ticker symbol"]])

