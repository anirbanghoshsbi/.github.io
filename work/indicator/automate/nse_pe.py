from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import warnings
warnings.filterwarnings("ignore")

data= pd.read_csv("https://raw.githubusercontent.com/anirbanghoshsbi/.github.io/master/work/ml/data_fundamental.csv")

data=data.tail(750)

data.set_index('Date',inplace=True)

#data.set_index('Date',inplace=True)
data['mov50']= data['feat_Div_Yield'].rolling(window=18).mean()
data['price_above_50dma']=data['Close'].rolling(window=50).mean()

last_date= data.index[-1]

#data[['feat_Div_Yield','feat_PB','feat_PE','Open','High','Low','Close']].to_csv('data_fundamental.csv')

# Assume 'pe_ratios' is your time series of P/E ratios
pe_ratios = data['feat_PE']

# Calculate mean and MAD
mean_pe = pe_ratios.median()
mad_pe = (pe_ratios - mean_pe).abs().mean()

# Calculate percentiles
percentiles = pe_ratios.quantile([0.1, 0.25, 0.5, 0.75, 0.9])
data['percentile']=percentiles
# Plot
plt.figure(figsize=(12, 6))
plt.hist(pe_ratios, bins=50, alpha=0.7)
plt.axvline(mean_pe, color='r', linestyle='dashed', label='Mean')
plt.axvline(mean_pe + mad_pe, color='g', linestyle='dashed', label='Mean + MAD')
plt.axvline(mean_pe - mad_pe, color='g', linestyle='dashed', label='Mean - MAD')

for p, v in percentiles.items():
    plt.axvline(v, color='orange', linestyle=':', label=f'{p*100}th percentile')

plt.title('P/E Ratio Distribution with MAD and Percentile Markers')
plt.xlabel('P/E Ratio')
plt.ylabel('Frequency')
plt.legend()
plt.show()

print(f"Mean P/E: {mean_pe:.2f}")
print(f"MAD: {mad_pe:.2f}")
print("Percentiles:")
print(percentiles)

# Evaluate current P/E
current_pe = data['feat_PE'].iloc[-1]  # Example current P/E
mad_score = (current_pe - mean_pe) / mad_pe
percentile_score = sum(pe_ratios < current_pe) / len(pe_ratios) * 100

data["future_return"] = data["Close"].shift(-20) / data["Close"] - 1
data["target"] = (data["Close"].shift(-20) > data["Close"]).astype(int)
data["pe_bucket"] = pd.qcut(data["feat_PE"], 5)

print('20 Days Return \n ' ,round(data.groupby("pe_bucket")["future_return"].mean()*100,2))
print('How often the price is higher than 20 days back :\n' ,data.groupby("pe_bucket")["target"].mean())



print(f"\nCurrent P/E: {current_pe}")
print(f"MAD Score: {mad_score:.2f} MADs from mean")
print(f"Percentile Score: {percentile_score:.2f}th percentile")

from telegram_sender import send_telegram_message

message = f"""
        NIFTY PE PERCENTILE REPORT
-------------------------------------------
Date of Data : {last_date}
-------------------------------------------
PE: {current_pe}
Percentile Score: {percentile_score}
Percentile Score Distribution:{percentiles}
---PE------ BUCKET--------RETURN (20 T Days)---Target achieved % 
PE BUCKET [19.62 ,21.48] :          3.37%   		78%
PE BUCKET [21.48, 22.06] :          1.78%   		81%
PE BUCKET [22.06 , 22.49]:          1.12%   		64%
PE BUCKET [22.49 , 22.83]:          0.03%   		55%
PE BUCKET [22.83 , 24.38]:         -0.75%   		42%

-------------------------------------------
"""

send_telegram_message(message)
