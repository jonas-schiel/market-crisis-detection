# Data

## Primary Data Source: Yahoo Finance (yfinance)

**Description:** Python package containing Open, High, Low, 
Close, and Volume data for U.S. ETFs and the VIX volatility index

**Date range:** 2005-01-01 to 2024-01-01

**License/Terms:** Publicly available market data via Yahoo Finance.
No personal or sensitive information. Used for academic,
non-commercial purposes.

**Ethical considerations:** No PII or sensitive data involved.
No terms of service restrictions apply to academic use.

## Retrieval Instructions

Install the required library:
```bash
pip install yfinance
```

Run the data retrieval script:
```bash
python src/fetch_data.py
```

This will download all required data and save it to `data/raw/market_data.csv`.

Alternatively, retrieve manually in Python:
```python
import yfinance as yf

tickers = ["SPY", "^VIX", "QQQ", "IWM", "GLD", "TLT"]
df = yf.download(tickers, start="2005-01-01", end="2024-01-01")
df.to_csv("data/raw/market_data.csv")
```

