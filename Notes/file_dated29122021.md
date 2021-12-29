# Trading Strategies Based on K-means Clustering and Regression Models

A commonly used k-means clustering algorithm is used to partition stock price time series data. After data partition, linear regression is used to analyse
the trend within each cluster. The results of the linear regression are then used for trend prediction for windowed time series data.

 Although the proposed approach is designed for stock trading, it can be applied to the trend analysis of any time series,
such as the time series of economic indicators

# Support and Resistance based on Closing Price using k-means

import yfinance
df = yfinance.download('AAPL','2013-1-1','2020-1-1')
X = np.array(df['Close'])
from sklearn.cluster import KMeans
import numpy as np
from kneed import DataGenerator, KneeLocator
    
sum_of_squared_distances = []
K = range(1,15)
for k in K:
    km = KMeans(n_clusters=k)
    km = km.fit(X.reshape(-1,1))
    sum_of_squared_distances.append(km.inertia_)
kn = KneeLocator(K, sum_of_squared_distances,S=1.0, curve="convex", direction="decreasing")
kn.plot_knee()
plt.plot(sum_of_squared_distances)

kmeans = KMeans(n_clusters= kn.knee).fit(X.reshape(-1,1))
c = kmeans.predict(X.reshape(-1,1))
minmax = []
for i in range(kn.knee):
    minmax.append([-np.inf,np.inf])
for i in range(len(X)):
    cluster = c[i]
    if X[i] > minmax[cluster][0]:
        minmax[cluster][0] = X[i]
    if X[i] < minmax[cluster][1]:
        minmax[cluster][1] = X[i]
from matplotlib import pyplot as plt
for i in range(len(X)):
    colors = ['b','g','r','c','m','y','k','w']
    c = kmeans.predict(X[i].reshape(-1,1))[0]
    color = colors[c]
    plt.scatter(i,X[i],c = color,s = 1)
for i in range(len(minmax)):
    plt.hlines(minmax[i][0],xmin = 0,xmax = len(X),colors = 'g')
    plt.hlines(minmax[i][1],xmin = 0,xmax = len(X),colors = 'r')        
[site]!https://towardsdatascience.com/using-k-means-clustering-to-create-support-and-resistance-b13fdeeba12)
