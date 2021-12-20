# -*- coding: utf-8 -*-
"""
Created on Sat May 15 14:15:19 2021

@author: AlexandrosCMitronikas
"""

#importing libraries
from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
%matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso


#Define the attribute names
names = df_wPolicies.columns


X = np.array(df_wPolicies)  # get input values
y = np.array(df_all['rr+1'])


#Using Pearson Correlation
plt.figure(figsize=(15,15))
cor = df.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()

#Correlation with output variable
cor_target = abs(cor["rr+1"])
#Selecting highly correlated features
relevant_features = cor_target[cor_target>0.35]
relevant_features

#Features correlated to rr+1

#New deaths / million    0.363552
#Reproduction rate       0.994617
#New vaccinations        0.512880
#% Total vaccinations    0.321295
#% People vaccinated     0.342379
#stringency_index        0.512583

print(df[["New deaths","People vaccinated", "Reproduction rate"]].corr())
print(df[["stringency_index","New vaccinations", "Reproduction rate"]].corr())


#Correlation with output variable
cor_target = abs(cor["rr+5"])
#Selecting highly correlated features
relevant_features = cor_target[cor_target>0.35]
relevant_features

#Features correlated to rr+5

#New deaths / million        0.405073
#Reproduction rate           0.897832
#% People fully vaccinated     0.612354
#New vaccinations            0.368406
#stringency_index            0.549212

print(df[["New deaths","People vaccinated", "Reproduction rate"]].corr())
print(df[["stringency_index","New vaccinations", "Reproduction rate"]].corr())
