# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
featureSet = pd.DataFrame(data = data.iloc[0:, 0:-1])
outcomeVector = pd.DataFrame(data = data.iloc[:, -1])

# Taking care of missing data
from sklearn.impute import SimpleImputer
simpleImputer = SimpleImputer(missing_values = np.NaN, strategy = 'mean')
simpleImputer.fit(featureSet.iloc[:, 1:3])
featureSet.iloc[:, 1:3] = simpleImputer.transform(featureSet.iloc[:, 1:3])


