import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import os
from dotenv import load_dotenv

load_dotenv()

data=os.getenv("REGRESSION_DATASET")
df=pd.read_csv(data)

X =df.drop("Exam_Score", axis=1)
y =df["Exam_Score"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#oob_score uses average for classification. and r2 score for regression by default.
model=RandomForestRegressor(n_estimators=100,bootstrap=True,oob_score=True,random_state=42)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
oob = model.oob_score_

print("\nRandom Forest Regression Evaluation")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)
print("OOB R2 Score:", oob)



