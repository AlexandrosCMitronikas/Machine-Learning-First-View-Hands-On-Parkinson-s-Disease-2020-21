# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:23:06 2019

@author: AlexandrosCMitronikas
"""

import pandas as pd
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

# Load the Diabetes dataset
columns = "age sex bmi map tc ldl hdl tch ltg glu".split() # Declare the columns names
diabetes = datasets.load_diabetes() # Call the diabetes dataset from sklearn
df = pd.DataFrame(diabetes.data, columns=columns) # load the dataset as a pandas data frame
y = diabetes.target # define the target variable (dependent variable) as y

# create training and testing vars
X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2)
print (X_train.shape, y_train.shape)
print (X_test.shape, y_test.shape)

# fit a model
lm = linear_model.LinearRegression()
model = lm.fit(X_train, y_train)
predictions = lm.predict(X_test)

print (np.around(y_test[0:10], decimals=2))
print (np.around(predictions[0:10], decimals=2))

## The line / model
plt.scatter(y_test[0:10], predictions[0:10])
plt.xlabel("True Values")
plt.ylabel("Predictions")

plt.scatter(y_test, predictions)
plt.xlabel("True Values")
plt.ylabel("Predictions")

print ("Score:", model.score(X_test, y_test))
print ("Score (rounded):", round(model.score(X_test, y_test),2))
