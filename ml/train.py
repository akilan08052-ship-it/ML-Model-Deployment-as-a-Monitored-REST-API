import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

df=pd.read_csv("ml/Iris.csv")
df["SepalLengthCm"].fillna(df["SepalLengthCm"]).mean()
df["SepalWidthCm"].fillna(df["SepalWidthCm"]).mean()
df["PetalLengthCm"].fillna(df["PetalLengthCm"]).mean()
df["PetalWidthCm"].fillna(df["PetalWidthCm"]).mean()


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

sample =[[6.2, 2.8, 4.8, 1.8]]
y_pred=model.predict(scaler.transform(sample))
#print(y_pred)

#accuracy score
joblib.dump(model,"ml/saved_model/iris.pkl")

mj=joblib.load("ml/saved_model/iris.pkl")
p=mj.predict(sample)
print(p)




