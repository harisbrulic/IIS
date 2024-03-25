import pandas as pd

df = pd.read_csv('C:/Users/bruli/Desktop/IIS/data/raw/mbajk_dataset.csv')

df['date'] = pd.to_datetime(df['date'])

df.set_index('date', inplace=True)
df_resampled = df.resample('H').mean()

df_resampled.fillna(method='ffill', inplace=True)

df_resampled.to_csv('C:/Users/bruli/Desktop/IIS/data/mbajk_processed.csv')
