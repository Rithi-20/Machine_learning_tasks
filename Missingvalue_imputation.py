import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.compose import make_column_selector
from sklearn.preprocessing import OneHotEncoder

load_dotenv()
data = os.getenv("MISSING_VALUES_DATASET")
read=pd.read_csv(data)
df=pd.DataFrame(read)

print(df.head())
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

X = df.drop("Exam_Score", axis=1)
y = df["Exam_Score"]



numerical_features = make_column_selector(dtype_include="number")
categorical_features = make_column_selector(dtype_include="object")

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
print("\nTraining Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)


numerical_imputer = SimpleImputer(strategy="median")
categorical_imputer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder",OneHotEncoder(handle_unknown="ignore"))
])
preprocessor = ColumnTransformer(transformers=[
        ("num", numerical_imputer, numerical_features),
        ("cat", categorical_imputer, categorical_features)
    ])


model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(
            n_estimators=100,
            bootstrap=True,
            random_state=42
        ))
    ]
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test) 

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nRandom Forest Regression Results")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)