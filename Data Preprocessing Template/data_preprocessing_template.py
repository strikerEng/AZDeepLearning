# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
featureSet = pd.DataFrame(data = data.iloc[0:, 0:-1])
outcomeVector = pd.DataFrame(data = data.iloc[:, -1])
