#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 21:08:56 2024

@author: dennisirwanto
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# set data
features, rows = map(int, input().split())
X, Y = [], []

# get the parameters X and Y for discovery the variables a and b
for i in range(rows):
    x = [0]
    elements = list(map(float, input().split()))
    X.append(elements[:features])
    Y.append(elements[features])
        
# set polynomial features 
poly = PolynomialFeatures(degree=3)
poly_X = poly.fit_transform(np.array(X))

# set the model LinearRegression
model = linear_model.LinearRegression()
model.fit(poly_X, Y)

# get the parameters X for discovery the Y
new_rows = int(input())
new_X = []
for i in range(new_rows):
    x = [0]
    elements = list(map(float, input().split()))
    new_X.append(elements[:features])
    
poly_newX = poly.fit_transform(np.array(new_X))
    
# Gets the results and show on the screen 
result = model.predict(poly_newX)
for i in range(len(result)):
    print(round(result[i], 2))
