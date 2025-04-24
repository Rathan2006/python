import pandas as pd

asking_prices = pd.Series([15000, 18000, 12000, 22000, 17000])
fair_prices = pd.Series([16000, 17500, 13000, 21000, 18000])

ans = asking_prices < fair_prices
print(ans[ans].index)