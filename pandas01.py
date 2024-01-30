# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:13:01 2024

@author: HP
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)
print(file.info())
print(file.describe())
"""

file = pandas.read_csv("iris.csv")

print(file)

file = pandas.read_csv("insurance_data.csv",skiprows=5)

print(file)

file = pandas.read_csv("housing_data.csv")

print(file)
"""