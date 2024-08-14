import pandas as pd
import os

def download_omie(date, path=None):
    
    url = f'https://www.omip.pt/es/market-data/spot?date={date}&commodity=EL&zone=ES'
    dfs = pd.read_html(url)
    df = dfs[1]

    if path:
        filename = f'{date}.csv'
        pathfile = os.path.join(path, filename)
        df.to_csv(pathfile, index=False)
    
    return df


def preprocess(path):
    
    df = pd.read_csv(path)
    date = path.split('/')[-1].split('.')[0]
    
    df.columns = ['hour', 'price', 'volume']
    df['date'] = date
    
    s = df['hour'].str.extract(r'(\d+)')[0]
    s = df['date'] + ' ' + s
    s = pd.to_datetime(s)
    df['datetime'] = s
    
    df = df.drop(columns=['hour', 'date']) 
    df = df.set_index('datetime')
    
    return df