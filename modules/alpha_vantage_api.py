import requests
import pandas as pd
import os

def preprocess_df(symbol):

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "full",
        "apikey": os.getenv("API_KEY_ALPHA")
    }
    
    URL_BASE = 'https://www.alphavantage.co/'
    ENDPOINT = 'query'
    
    url = URL_BASE + ENDPOINT
    
    res = requests.get(url=url, params=params)
    data = res.json()
    
    df = pd.DataFrame(data['Time Series (Daily)']).T
    df.columns = df.columns.str.replace(r'\d\. ', '', regex=True)
    
    df.index = pd.to_datetime(df.index)
    df = df.astype(float).sort_index()
    
    return df