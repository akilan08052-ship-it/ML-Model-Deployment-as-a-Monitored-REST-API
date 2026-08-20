import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import pickle
import os


df=pd.read_csv("ml/Iris.csv")




#Test $$ Traget

x=df[["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]]
y=df["Species"]


#test and train model
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)


#standardizing the model
scaler=StandardScaler()
x_train=scaler.fit_transform(X_train)
x_test=scaler.transform(X_test)

#model 
model=LogisticRegression()
model.fit(x_train,y_train)



with open("ml/saved_model/model.pkl","w+b")as f:
    pickle.dump(model,f)
with open("ml/saved_model/scaler.pkl","w+b")as f:
    pickle.dump(scaler,f)











