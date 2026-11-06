import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
import os
from dotenv import load_dotenv

load_dotenv()

data=os.getenv("CLASSIFICATION_DATASET")
df=pd.read_csv(data)


X = df.drop("Result", axis=1)
y = df["Result"]

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=42,stratify=y)


weak_learner = DecisionTreeClassifier(max_depth=1,random_state=42)
model = AdaBoostClassifier(estimator=weak_learner,n_estimators=50,learning_rate=1.0,random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nAmount of Say (Alpha) for Each Tree:")
print(model.estimator_weights_)
