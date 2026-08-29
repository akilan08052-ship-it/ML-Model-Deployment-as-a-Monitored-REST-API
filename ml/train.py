import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
import joblib



df=pd.read_csv("ml/Iris.csv")

x=df[["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]]
y=df["Species"]

X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

pipline=Pipeline([
    ("scaler",StandardScaler()),
    ("model",LogisticRegression()),
    
])

pipline.fit(X_train,y_train)
y_pred=pipline.predict(X_test)
accuracy=accuracy_score(y_pred,y_test)


joblib.dump(pipline,"ml/saved_model/iris_pipeline.pkl")
joblib.dump(accuracy,"ml/saved_model/accuracy.pkl")











