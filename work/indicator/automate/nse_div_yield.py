# -------------------------------
# IMPORT LIBRARIES
# -------------------------------
from datetime import date
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
from scipy import stats

warnings.filterwarnings("ignore")


# -------------------------------
# LOAD DATA
# -------------------------------
data = pd.read_csv(
    "https://raw.githubusercontent.com/anirbanghoshsbi/.github.io/master/work/ml/data_fundamental.csv"
)

# Use only recent history
data = data.tail(750)

# Set date index
data.set_index("Date", inplace=True)


# -------------------------------
# BASIC MARKET FEATURES
# -------------------------------

# Dividend yield rolling average
data["div_yield_ma"] = data["feat_Div_Yield"].rolling(18).mean()

# Price 50 day moving average
data["price_50dma"] = data["Close"].rolling(50).mean()

# PE 50 day moving average
data["pe_50dma"] = data["feat_PE"].rolling(50).mean()

# PE spread (valuation deviation)
data["pe_spread"] = data["feat_PE"] - data["pe_50dma"]

# Dividend yield percentile
data["dy_pct"] = data["feat_Div_Yield"].rank(pct=True)


# -------------------------------
# PE DISTRIBUTION ANALYSIS
# -------------------------------

pe_ratios = data["feat_Div_Yield"]

# Median and MAD
median_pe = pe_ratios.median()
mad_pe = (pe_ratios - median_pe).abs().mean()

# Percentiles
percentiles = pe_ratios.quantile([0.1, 0.25, 0.5, 0.75, 0.9])



# -------------------------------
# CURRENT VALUATION SCORE
# -------------------------------

current_pe = data["feat_Div_Yield"].iloc[-1]

mad_score = (current_pe - median_pe) / mad_pe
percentile_score = sum(pe_ratios < current_pe) / len(pe_ratios) * 100

print("Current PE:", current_pe)
print("MAD Score:", mad_score)
print("Percentile Score:", percentile_score)


# -------------------------------
# PE PERCENTILE TIME SERIES
# -------------------------------

data["pe_percentile"] = stats.percentileofscore(
    data["feat_Div_Yield"], data["feat_Div_Yield"], kind="weak"
)

data["pe_pct_roc"] = data["pe_percentile"] - data["pe_percentile"].shift(10)


# -------------------------------
# FUTURE RETURNS
# -------------------------------

data["future_return"] = data["Close"].shift(-20) / data["Close"] - 1

data["target"] = (
    data["Close"].shift(-20) > data["Close"]
).astype(int)


# -------------------------------
# DIVIDEND YIELD BUCKET ANALYSIS
# -------------------------------

data["pe_bucket"] = pd.qcut(data["feat_Div_Yield"], 5)

print(
    "20 Day Return",
    data.groupby("pe_bucket")["future_return"].mean() * 100
)

print(
    "Probability of price increase",
    data.groupby("pe_bucket")["target"].mean()
)


# -------------------------------
# VOLATILITY (ATR)
# -------------------------------

high_low = data["High"] - data["Low"]
high_close = (data["High"] - data["Close"].shift()).abs()
low_close = (data["Low"] - data["Close"].shift()).abs()

data["TR"] = pd.concat(
    [high_low, high_close, low_close], axis=1
).max(axis=1)

data["ATR"] = data["TR"].rolling(14).mean()


# -------------------------------
# ELDER IMPULSE SYSTEM
# -------------------------------

# EMA
data["ema13"] = data["Close"].ewm(span=13).mean()
data["ema13_slope"] = data["ema13"].diff()

# MACD
ema12 = data["Close"].ewm(span=12).mean()
ema26 = data["Close"].ewm(span=26).mean()

data["macd"] = ema12 - ema26
data["macd_signal"] = data["macd"].ewm(span=9).mean()
data["macd_hist"] = data["macd"] - data["macd_signal"]
data["macd_hist_slope"] = data["macd_hist"].diff()


# Impulse conditions
conditions = [
    (data["ema13_slope"] > 0) &
    (data["macd_hist_slope"] > 0) &
    (data["Close"] > data["price_50dma"]),

    (data["ema13_slope"] < 0) &
    (data["macd_hist_slope"] < 0) &
    (data["Close"] < data["price_50dma"])
]

choices = [1, -1]

data["elder_impulse"] = np.select(conditions, choices, 0)


# -------------------------------
# RETURN ANALYSIS
# -------------------------------

data["future_return_10"] = data["Close"].shift(-20) / data["Close"] - 1

bins = [0,20,40,60,80,100]

labels = [
    "20 Percentile",
    "40 Percentile",
    "60 Percentile",
    "80 Percentile",
    "100 Percentile"
]

data["pe_pct_bucket"] = pd.cut(
    data["pe_percentile"],
    bins=bins,
    labels=labels
)

result = (
    data
    .groupby(["pe_pct_bucket","elder_impulse"])["future_return_10"]
    .agg(["mean","median","count"])
)

print(result * 100)


# -------------------------------
# VOLATILITY ADJUSTED RETURNS
# -------------------------------

data["atr_pct"] = data["ATR"] / data["Close"]

data["vol_adj_return_10"] = (
    data["future_return_10"] /
    data["atr_pct"]
)

result = (
    data
    .groupby(["pe_pct_bucket","elder_impulse"])["vol_adj_return_10"]
    .agg(["mean","median","count"])
)

print(result)


# -------------------------------
# TRADING EXPECTANCY
# -------------------------------

expectancy = data.groupby("elder_impulse")[
    "future_return_10"
].agg(["mean","median","count"])

expectancy["mean"] = expectancy["mean"] * 100
expectancy["median"] = expectancy["median"] * 100

print(expectancy)


# -------------------------------
# VALUATION REGIME CLASSIFICATION
# -------------------------------

conditions = [

    (data["dy_pct"] > 0.85) &
    (data["pe_spread"] < -0.4),

    (data["dy_pct"] > 0.75) &
    (data["pe_spread"] < -0.4) &
    (data["elder_impulse"] == -1),

    (data["dy_pct"].between(0.25,0.75)) &
    (data["pe_spread"].diff(5) > 0),

    (data["dy_pct"].between(0.25,0.75)) &
    (data["pe_spread"].diff(5) < 0),

    (data["dy_pct"] < 0.25) &
    (data["pe_spread"] > 0.35)

]

choices = [
    "deep_value",
    "value",
    "uptrend",
    "downtrend",
    "expensive"
]

data["valuation_regime"] = np.select(
    conditions,
    choices,
    "neutral"
)


# -------------------------------
# REGIME PERFORMANCE
# -------------------------------

print(
    data.groupby("valuation_regime")["future_return"]
    .mean() * 100
)

h=data['valuation_regime'].iloc[-1]
text = "Last 10 Valuation Regimes \n \n "
text += data["valuation_regime"].tail(10).to_string()
last_date=data.index[-1]
current_div_yld = data['feat_Div_Yield'].iloc[-1]

from telegram_sender import send_telegram_message

message = f"""
        NIFTY DIV YIELD PERCENTILE REPORT
-------------------------------------------
Date of Data : {last_date}
-------------------------------------------
Div Yld: {current_div_yld}
Percentile Score: {percentile_score}
Lattest  Regime : {h}
last 10 Days Regime : {text}

-------------------------------------------
"""

send_telegram_message(message)
