import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import confusion_matrix,f1_score,classification_report,recall_score
from sklearn.model_selection import train_test_split
import os
from dotenv import load_dotenv

load_dotenv()

data=os.getenv("CLASSIFICATION_DATASET")
df=pd.read_csv(data)

print(df.head())
print("*"*50)

X = df.drop("Result", axis=1)
y = df["Result"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,stratify=y,random_state=42)

model=DecisionTreeClassifier(criterion="gini", random_state=42,max_depth=3,min_samples_split=5,min_samples_leaf=2)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)

path = model.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas = path.ccp_alphas
print("Alpha values:")
print(ccp_alphas)
print("Model Evaluation: ")

print("Confusion Matrix:",confusion_matrix(y_test,y_pred))
print("*"*50)
print("Classification report:",classification_report(y_test,y_pred))
print("*"*50)

sensitivity = recall_score(y_test, y_pred, pos_label="Fail")
print("Sensitivity:",sensitivity)
specificity = recall_score(y_test, y_pred, pos_label="Pass")
print("Specificity:",specificity)

# Visualization
plt.figure(figsize=(20, 10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=model.classes_,
    filled=True,
    rounded=True,
    fontsize=9,
    max_depth=3
)
plt.title("Student Pass/Fail Decision Tree")
plt.show()