import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os
from dotenv import load_dotenv

load_dotenv()

data = os.getenv("REGRESSION_DATASET")
df=pd.read_csv(data)
X = df.drop("Exam_Score", axis=1)
y = df["Exam_Score"]

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=42)

model = GradientBoostingRegressor(n_estimators=100,learning_rate=0.1,max_depth=3,loss="squared_error",random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("Gradient Boosting Regression Results")
print("------------------------------------")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)

# 8. Number of trees
print("\nNumber of estimators:", model.n_estimators_)
