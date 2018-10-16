# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Importing the dataset
data = pd.read_csv('Data.csv')
featureSet = pd.DataFrame(data = data.iloc[0:, 0:-1])
outcomeVector = pd.DataFrame(data = data.iloc[:, -1])

#Splitting the data into Training and Test Sets
X_Train, X_Test, Y_Train, Y_Test = train_test_split(featureSet, outcomeVector, test_size = 0.2,random_state = 0)

#Feature Scaling
scaleFeatureSet = StandardScaler()
X_Train = scaleFeatureSet.fit_transform(X_Train)
X_Test = scaleFeatureSet.transform(X_Test)
