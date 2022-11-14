#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import metrics
from sklearn import linear_model
from sklearn import ensemble
from sklearn import tree
from sklearn import svm



# In[4]:


data=pd.read_csv("D:\weatherAUS.csv")
data.head()


# In[5]:


data_cat=data[['RainToday','WindGustDir','WindDir9am','WindDir3pm']] 
data.drop(columns=['Evaporation','Sunshine','Cloud9am','Cloud3pm'], axis=1) 
data.drop(['RainToday','WindGustDir','WindDir9am','WindDir3pm'], axis=1 )


# In[6]:


data[ 'MinTemp'].fillna(data['MinTemp'].mean(), inplace=True) 
data['MaxTemp'].fillna(data['MaxTemp'].mean(), inplace=True) 
data['Rainfall'].fillna(data['Rainfall'].mean(), inplace=True) 
data['WindGustSpeed'].fillna(data['WindGustSpeed'].mean(), inplace=True) 
data['WindSpeed9am'].fillna(data['WindSpeed9am'].mean(), inplace=True) 
data['WindSpeed3pm'].fillna(data['WindSpeed3pm'].mean(), inplace=True) 
data['Humidity9am'].fillna(data['Humidity9am'].mean(), inplace=True) 
data['Humidity3pm'].fillna(data['Humidity3pm'].mean(), inplace=True) 
data['Pressure9am'].fillna(data['Pressure9am'].mean(), inplace=True) 
data['Pressure3pm'].fillna (data['Pressure3pm'].mean(), inplace=True) 
data['Temp9am'].fillna(data['Temp9am'].mean(), inplace=True) 
data['Temp3pm'].fillna(data['Temp3pm' ].mean(), inplace=True)


# In[7]:



X = data.iloc[:,[1,2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]].values
Y = data.iloc[:,22].values


# In[8]:


print(X)


# In[21]:
