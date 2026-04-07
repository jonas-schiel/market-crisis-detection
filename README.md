# Predicting Market Crises using Market Data

## Research Question:

Can market crises be predicted before they happen?

## Project Specs

**Target Label:** Crisis Day (1), Normal Day (0)

**Target Definition:** Crisis days are defined as days where the Volatility Index (VIX), closes at a value above 30. When looking at historical market data, a VIX close above 30 considerably unusual, and tends to align with significant global events, such as the 2008 housing market collapse, the 2010 flash crash, and the 2020 COVID-19 pandemic

**Data:** 
- yfinance data ranging from 2005-2024
- Tickers used: SPY, QQQ, IWM, GLD, TLT, and ^VIX
- See the data folder for more info

**ML Methods Used:** Logistic Regression, Random Forest, Gradient Boosting, Isolation Forest

## Results

Gradient Boosting produced the best results, with a test accuracy of 97.8% (inflated due to class imbalance), and a minority class f1-score of 0.88, with 91% precision, 84% recall, and a support of 88. Random forest produced similar results with a test accuracy of 97.2% (imbalanced), and a minority class f1-score of 0.85, with 89% precision, 81% recall, and a support of 88.

## Repo Structure

project/
├── analysis/
│   ├── models/
│   └── visualizations/
│       ├── EDA/
│       ├── GB_ML/
│       ├── LR_ML/
│       └── RF_ML/
├── data/
│   ├── README.md
│   ├── data_preprocessing.py
│   └── marketdata.csv
└── progress/
    ├── 01_proposal.md
    ├── 02_eda.md
    └── 03_supervised.md
