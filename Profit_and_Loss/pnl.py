import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'close': [98, 101, 106, 107, 110, 111, 120, 123, 124, 123, 122, 123, 120, 121, 125],
    'entry_prices': [np.nan, 101.0, 101.0, 101.0, 101.0, 101.0, np.nan, np.nan, np.nan, 123.0, 123.0, 123.0, 123.0, np.nan, np.nan],
}

df = pd.DataFrame(data)

# Calculate the difference
df['difference'] = df['close'] - df['entry_prices']

# Initialize variables
prv_day = 0
results = []

for i, row in df.iterrows():
    if pd.isna(row['entry_prices']):
        results.append(np.nan)
    else:
        if row['difference'] > 0:
            results.append(row['difference'])
            prv_day = row['difference']
        else:
            if prv_day + row['difference'] > 0:
                results.append(prv_day + row['difference'])
                prv_day += row['difference']
            else:
                results.append(0)
                prv_day = 0

df['result'] = results
print(df)