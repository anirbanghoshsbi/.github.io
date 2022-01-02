Regime Change Detection Using Directional Change Indicators.
Classification of Normal and abnormal regimes in financial markets.
Tracking Regime change using directional Change Indicators and trading using those indicators.

What is regime change ?
Aregime change is a significant change in the collective trading behaviour in a financial market.

(Uses HMM).


# Naive Bayes Classifier

## Training Phase

Input: Training Data (x, C)

Output: Parameters of the Model

1. Calculate the prior probability of class, p(Ck).
2. Calculate the mean μk and the standard deviation σk of the input feature
of each class.
3. Estimate the Gaussian distribution of each class p(x|Ck).
4. Calculate prior probability of the input feature, p(x).
Testing Phase

Input: Test Data (v)

## Output: The probability p(Ck|x = v)

1. For each observation in v, plugging it into the Gaussian distribution
parametrized by μk and σk.
2. Calculate the probability p(x = v|Ck).
3. Calculate the probability p(Ck|x = v).
