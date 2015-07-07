%matplotlib inline
import pandas as pd
import numpy as np
import pandas.io.data as web
import matplotlib.pyplot as plt
import datetime
import scipy.stats as stats
import pandas.tools.plotting as pdplot
import statsmodels.tsa.stattools as ts

symbols = ['CSIQ', 'DRYS', 'FNSR', 'HIMX', 'JASO', 'SPY']

portfolio = web.get_data_yahoo(symbols, start=datetime.datetime(2010, 1, 1), end=datetime.datetime(2015, 7, 6))['Adj Close']

portfolio.head()

portfolio.plot()

plt.rcParams['figure.figsize'] = 11, 7

portfolio.plot()

portfolio.corr()
