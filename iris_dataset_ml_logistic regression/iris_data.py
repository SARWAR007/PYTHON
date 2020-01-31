# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 23:01:47 2020

@author: faisa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

dataset_iris = pd.read_csv(r"IRIS.csv")

dataset_iris['species'].unique()

dataset_iris.isnull().sum()

sns.countplot(x="sepal_length",hue = "species",data=dataset_iris)


data = dataset_iris[(dataset_iris['petal_width'] < 1)]
data.to_frame()

#preparing training and test data set

#selecting the feature values
y = dataset_iris['species']
x = dataset_iris.drop(['species'],axis =1)

from sklearn.cross_validation import train_test_split

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size =0.3,random_state=0)

from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()

logreg.fit(x_train,y_train)

predict = logreg.predict(x_test)

print(predict)

from sklearn.metrics import confusion_matrix

confusion_matrix(y_test,predict)


from sklearn.metrics import accuracy_score

accuracy_score(y_test,predict)

from sklearn.metrics import classification_report
classification_report(y_test,predict)