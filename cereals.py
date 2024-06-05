# -*- coding: utf-8 -*-
"""cereals.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FihSfabXXQC3ms2MkLQnFWJOeN7oe-nu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("/content/cereal.csv")
df

df.head()

df.shape

df.isnull().sum()

df.describe()

x=df.iloc[:,3:15]
x

y=df['rating']
y

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train,y_train)

y_pred=lr.predict(x_test)
y_pred

from sklearn.metrics import (r2_score, mean_absolute_error, mean_squared_error)
score=r2_score(y_pred,y_test)
score

me=mean_absolute_error(y_test,y_pred)
me

msq=mean_squared_error(y_test,y_pred)
msq

plt.figure(figsize=(8,5))
sns.histplot(df)