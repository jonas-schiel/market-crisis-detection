import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pickle
from datetime import datetime, timedelta


with open("models/best_model.pkl", "rb") as f:
    model = pickle.load(f)


tickers = ["SPY", "^VIX", "QQQ", "IWM", "GLD", "TLT"]
data = yf.download(tickers, start="2004-01-01", end=datetime.today().strftime("%Y-%m-%d"))

#Creating Features

close = data['Close']
vol = data['Volume']
feature_df = pd.DataFrame(index=close.index)

## Volatility Features
feature_df['Vix'] = close['^VIX']
feature_df['VIX_roll_10'] = close['^VIX'].rolling(window=10, min_periods=1).mean()
feature_df['VIX_roll_20'] = close['^VIX'].rolling(window=20, min_periods=1).mean()
feature_df['VIX_day_change'] = close['^VIX'].diff()
feature_df['VIX_sd'] = close['^VIX'].rolling(window=30).std()
feature_df['SPY_roll_10'] = close['SPY'].rolling(window=10, min_periods=1).std()
feature_df['SPY_roll_20'] = close['SPY'].rolling(window=20, min_periods=1).std()
feature_df['SPY_roll_60'] = close['SPY'].rolling(window=60, min_periods=1).std()

## Returns
feature_df['SPY_day_return'] = close['SPY'].pct_change(1)
feature_df['SPY_5_day_return'] = close['SPY'].pct_change(5)
feature_df['SPY_20_day_return'] = close['SPY'].pct_change(20)
feature_df['QQQ_day_return'] = close['QQQ'].pct_change(1)
feature_df['IWM_day_return'] = close['IWM'].pct_change(1)
feature_df['TLT_day_return'] = close['TLT'].pct_change(1)
feature_df['GLD_day_return'] = close['GLD'].pct_change(1)


## Drawdowns
SPY_rolling_max = close["SPY"].rolling(window=252, min_periods=1).max()
feature_df['SPY_drawdown'] = (close["SPY"] - SPY_rolling_max) / SPY_rolling_max * 100  
QQQ_rolling_max = close["QQQ"].rolling(window=252, min_periods=1).max()
feature_df['QQQ_drawdown'] = (close["QQQ"] - QQQ_rolling_max) / QQQ_rolling_max * 100  
IWM_rolling_max = close["IWM"].rolling(window=252, min_periods=1).max()
feature_df['IWM_drawdown'] = (close["IWM"] - IWM_rolling_max) / IWM_rolling_max * 100  

## Correlations
spy_return = close['SPY'].pct_change()
tlt_return = close['TLT'].pct_change()
gld_return = close['GLD'].pct_change()
vix_change = close['^VIX'].diff()

feature_df['SPY_TLT_corr_20'] = spy_return.rolling(window=20).corr(tlt_return)
feature_df['SPY_TLT_corr_60'] = spy_return.rolling(window=60).corr(tlt_return)
feature_df['SPY_GLD_corr_20'] = spy_return.rolling(window=20).corr(gld_return)
feature_df['SPY_VIX_corr_20'] = spy_return.rolling(window=20).corr(vix_change)

## Volume
feature_df['SPY_vol_ratio'] = vol['SPY'] / vol['SPY'].rolling(window=20).mean()
feature_df['QQQ_vol_ratio'] = vol['QQQ'] / vol['QQQ'].rolling(window=20).mean()
feature_df['IWM_vol_ratio'] = vol['IWM'] / vol['IWM'].rolling(window=20).mean()


## Trends
spy_moving_avg = close['SPY'].rolling(window=200).mean()
feature_df['spy_above_avg'] =  (close['SPY'] > spy_moving_avg).astype(int)

## Target
crisis = (close['^VIX'] > 30)
feature_df['market_crisis'] = crisis.shift(-20).astype(int)


feature_df.dropna()

recent_data = feature_df.tail(60)
predictions = model.predict_proba(recent_data)[:, 1]


fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(recent_data.index, predictions, color="steelblue", linewidth=1.5, label="Crisis Probability")
ax.axhline(y=0.5, color="red", linestyle="--", linewidth=1, label="Crisis Threshold")
ax.fill_between(recent_data.index, predictions, 0.5, 
                where=(predictions > 0.5), color="red", alpha=0.3, label="Crisis Signal")
ax.set_title(f"20-Day Forward Market Crisis Probability — Updated {datetime.today().strftime('%Y-%m-%d')}")
ax.set_xlabel("Date")
ax.set_ylabel("Crisis Probability")
ax.set_ylim(0, 1)
ax.legend()
plt.tight_layout()
plt.savefig("visualizations/forecast.png", dpi=150, bbox_inches="tight")