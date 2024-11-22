# -*- coding: utf-8 -*-
"""Gold-price.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z-qk7ITG4oGmOkQbU1JsEpQimDyE8rRS
"""

import pandas as pd

df = pd.read_csv('gold prices.csv')

df['Date'] = pd.to_datetime(df['Date'])

df.set_index('Date', inplace=True)

df.head()

df.dropna(inplace=True)

df = df.iloc[::-1]
df.head()

df["Close/Last"].plot(figsize=(12,8), legend=True)

df.tail()

import sklearn
from sklearn import svm, preprocessing

df = sklearn.utils.shuffle(df)

X = df.drop('Close/Last', axis=1).values
X = preprocessing.scale(X)
y = df['Close/Last'].values

test_size = 100
X_train = X[:-test_size]
y_train = y[:-test_size]

X_test = X[-test_size:]
y_test = y[-test_size:]

clf = svm.SVR(kernel='linear')
clf.fit(X_train, y_train)

clf.score(X_test, y_test)

for X,y in zip(X_test, y_test):
    print(f"Model: {clf.predict([X])[0]}, Actual: {y}")