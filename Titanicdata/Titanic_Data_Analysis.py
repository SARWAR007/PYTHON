# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 18:27:12 2020

@author: faisa
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

dataset =pd.read_csv(r"train.csv")

dataset['Embarked'].count()


 #Analuze the data
 
survived_people = dataset.groupby(['Survived','Sex']).count()

sns.countplot(x = "Survived", data = dataset)    

sns.countplot(x = "Sex", data =dataset)

sns.countplot(x = "Survived" , hue = "Sex", data = dataset)

sns.countplot(x = "Survived", hue = "Pclass", data = dataset)

#Data Wrangling

dataset.isnull().sum()

sns.heatmap(dataset.isnull(),yticklabels = False )

sns.boxplot(x = 'Pclass', y ='Age', data = dataset)


dataset.drop("Cabin",axis = 1 , inplace = True)

dataset['Age'].fillna((dataset['Age'].mean()), inplace=True)

dataset.dropna(axis =0 ,inplace = True)

sns.heatmap(dataset.isnull(),yticklabels =False)

dataset.isnull().sum()
# converting data to a dummy variable

sex = pd.get_dummies(dataset['Sex'],drop_first =True)

embarked = pd.get_dummies(dataset['Embarked'] ,drop_first = True)

pclass = pd.get_dummies(dataset['Pclass'] ,drop_first = True)

dataset = pd.concat([dataset, pclass,sex,embarked],axis =1)


#dropping the unwanted columns

dataset.drop(['PassengerId','Name','Ticket','Embarked','Sex'],axis = 1 ,inplace = True)
dataset.drop(['Pclass'],axis =1 ,inplace = True)

# Train and Test data

y = dataset['Survived']

x = dataset.drop(['Survived'],axis = 1)

from sklearn.cross_validation import train_test_split

x_train ,x_test,y_train,y_test = train_test_split(x,y,test_size =0.2,random_state = 0)


from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()

logreg.fit(x_train,y_train)


pred = logreg.predict(x_test)

from sklearn.metrics import confusion_matrix 

confusion_matrix(y_test,pred)

from sklearn.metrics import accuracy_score

accuracy_score(y_test,pred)



