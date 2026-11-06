import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import os
from dotenv import load_dotenv

load_dotenv()
data=os.getenv("REGRESSION_DATASET")
df=pd.read_csv(data)
print(df.head())
print(df.info())
print(df.describe())


print("Missing Values:")
print(df.isnull().sum())

print("Duplicate Rows:")
print(df.duplicated().sum())


X =df.drop("Exam_Score", axis=1)
y =df["Exam_Score"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = DecisionTreeRegressor(criterion="squared_error",max_depth=4,min_samples_split=5,min_samples_leaf=2,random_state=42)
model.fit(X_train, y_train)
y_pred =model.predict(X_test)


mae =mean_absolute_error(y_test, y_pred)
mse =mean_squared_error(y_test, y_pred)
rmse =np.sqrt(mse)
r2 =r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)



