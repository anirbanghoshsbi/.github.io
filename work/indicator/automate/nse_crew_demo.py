from datetime import date
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import warnings
warnings.filterwarnings("ignore")

# =========================
# CREWAI IMPORTS
# =========================

from crewai import Agent, Task, Crew, LLM

# Use OpenAI model
llm = LLM(model="openai/gpt-4o-mini")

# =========================
# LOAD DATA
# =========================

data= pd.read_csv("https://raw.githubusercontent.com/anirbanghoshsbi/.github.io/master/work/ml/data_fundamental.csv")

data=data.tail(750)

data.set_index('Date',inplace=True)

data['mov50']= data['feat_Div_Yield'].rolling(window=18).mean()
data['price_above_50dma']=data['Close'].rolling(window=50).mean()

last_date= data.index[-1]

# =========================
# PE ANALYSIS
# =========================

pe_ratios = data['feat_PE']

mean_pe = pe_ratios.median()
mad_pe = (pe_ratios - mean_pe).abs().mean()

percentiles = pe_ratios.quantile([0.1, 0.25, 0.5, 0.75, 0.9])
data['percentile']=percentiles

# =========================
# PLOT
# =========================

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

# =========================
# CURRENT METRICS
# =========================

current_pe = data['feat_PE'].iloc[-1]

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

# =========================
# CREWAI MARKET ANALYSIS
# =========================

market_analyst = Agent(
    role="Indian Equity Market Strategist",
    goal="Interpret Nifty valuation metrics",
    backstory="Expert in Indian equity valuation models and market regimes.",
    verbose=True,
    llm=llm
)

analysis_task = Task(
    description=f"""
    Analyze the following Nifty valuation metrics.

    Current PE: {current_pe}
    PE Percentile: {percentile_score}
    Median PE: {mean_pe}
    MAD: {mad_pe}

    Explain whether the Nifty market appears:
    - undervalued
    - fairly valued
    - overvalued

    Also briefly describe expected 20-day return tendencies from the bucket analysis.
    """,
    expected_output="Concise market valuation interpretation",
    agent=market_analyst
)

crew = Crew(
    agents=[market_analyst],
    tasks=[analysis_task]
)

analysis = crew.kickoff()

print("\nAI MARKET ANALYSIS:\n")
print(analysis)

# =========================
# TELEGRAM MESSAGE
# =========================

from telegram_sender import send_telegram_message

message = f"""
NIFTY PE PERCENTILE REPORT
-------------------------------------------
Date of Data : {last_date}
-------------------------------------------
PE: {current_pe}
Percentile Score: {percentile_score}

Median PE: {mean_pe}
MAD: {mad_pe}

-------------------------------------------
AI MARKET INTERPRETATION
-------------------------------------------
{analysis}

-------------------------------------------
"""

send_telegram_message(message)
