import pandas as pd
import requests

def get_stock_data(symbol='IBM', apikey='EMZ0M6J3MBBCMTWG'):

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "full",
        "apikey": apikey
    }

    url = 'https://www.alphavantage.co/query'

    res = requests.get(url=url, params=params)
    data = res.json()
    df = pd.DataFrame(data['Time Series (Daily)'])
    df = df.T.astype(float)
    df.columns = ['open', 'high', 'low', 'close', 'volume']
    
    return df