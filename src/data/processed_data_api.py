import json
from datetime import datetime
import pandas as pd

# Učitavanje svežih podataka
with open('data/raw/svezi_podatki.json', 'r', encoding='utf-8') as file:
    svezi_podaci = json.load(file)

# Filtriranje podataka za GOSPOSVETSKA C. - TURNERJEVA UL.
filtrirani_podaci = [station for station in svezi_podaci if station['name'] == "GOSPOSVETSKA C. - TURNERJEVA UL."]

# Kreiranje DataFrame-a
df = pd.DataFrame(filtrirani_podaci)

# Konverzija vremena iz UNIX timestamp-a u čitljiv format
df['last_update'] = pd.to_datetime(df['last_update'], unit='ms', utc=True)

# Postavljanje 'last_update' kao indeksa
df.set_index('last_update', inplace=True)

# Selektovanje kolone 'available_bikes' i primena agregacije na urni interval
df_bikes = df[['available_bikes']].resample('H').mean()

# Sačuvati obrađene podatke
df_bikes.to_csv('data/processed/agregirani_svezi_podatki.csv')
