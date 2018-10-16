# Data Preprocessing

# Importing the libraries

import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
#from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
#from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split


# Importing the dataset
data = pd.read_csv('Data.csv')
featureSet = data.drop('Purchased', axis=1).values
outcomeVector = data['Purchased'].values

# Taking care of missing data

simpleImputer = SimpleImputer(missing_values = np.NaN, strategy = 'mean')
simpleImputer.fit(featureSet[:, 1:3])
featureSet[:, 1:3] = simpleImputer.transform(featureSet[:, 1:3])

# Encoding categorical data
    #Attempt to use Pipelines and ColumnTransformer to apply Encoding to the dataset. However, the featureSet or outcomeVector is updated
        #categoricalFeatures = ['Country', 'Purchased']
        #categoricalTransformer = Pipeline(steps = 
        #    [ ('imputer', SimpleImputer(strategy = 'constant', fill_value = 'missing')),
        #     ('oneHot', OneHotEncoder(handle_unknown='ignore'))
        #     
        #     ])
        #
        #numericalFeatures = ['Age', 'Salary']
        #numericalTransformer = Pipeline(steps=[
        #        ('imputer', SimpleImputer(missing_values = np.NaN, strategy = 'mean')),
        #        ('oneHot', OneHotEncoder())
        #        ])
        #
        #preprocessor = ColumnTransformer(
        #        transformers = [
        #                ('categorical', categoricalTransformer, categoricalFeatures),
        #                ('numerical', numericalTransformer, numericalFeatures)        
        #        ])
        #
        #process = Pipeline(
        #        steps = [
        #                ('preprocessor', preprocessor)
        #        ])
        #
        #process.fit
        #process.transform

    # Encoding the Independent Variables
labelEncoder_featureSet = LabelEncoder()
featureSet[:, 0] = labelEncoder_featureSet.fit_transform(featureSet[:, 0])
    
oneHotEncoder = OneHotEncoder( categorical_features = [0])
featureSet = oneHotEncoder.fit_transform(featureSet).toarray()
    

# Encoding the Dependent Variable
labelEncoder_outcomeVector = LabelEncoder()
outcomeVector = labelEncoder_outcomeVector.fit_transform(outcomeVector)

        
#Splitting the data into Training and Test Sets
X_Train, X_Test, Y_Train, Y_Test = train_test_split(featureSet, outcomeVector, test_size = 0.2,random_state = 0)
