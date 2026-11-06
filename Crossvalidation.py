import numpy as np 
import pandas as pd 
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold , cross_val_score , GridSearchCV
from sklearn.metrics import f1_score, confusion_matrix, classification_report , recall_score
import os
from dotenv import load_dotenv

load_dotenv()

data=os.getenv("CLASSIFICATION_DATASET")
df=pd.read_csv(data)
print(df.head())
print("*"*50)
print(df.shape)
print("*"*50)
print(df.info())
print("*"*50)
print("Missing values:",df.isnull().sum())
print("*"*50)
print("Duplicates:",df.duplicated().sum())
print("*"*50)




X=df.drop('Result', axis=1)
y = df['Result']
X_train, X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
print(len(X_train))
print(len(X_test))
p=0
f=0
for i in y_train:
    if i=='Pass':
        p+=1
    else:
        f+=1
print(p)
print(f)




# Creating a pipeline 
models={
    'Logistic Regression':make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=1000)
        ),
    'Decision Tree':make_pipeline(
        DecisionTreeClassifier(random_state=42)
        ),
    'Random Forest':make_pipeline(
        RandomForestClassifier(random_state=42)
        ),
    'KNN':make_pipeline(
        StandardScaler(),
        KNeighborsClassifier()
        )
}

param ={
    'Logistic Regression':{
        'logisticregression__C': [0.01, 0.1, 1, 10]
    },

    'Decision Tree': {
        'decisiontreeclassifier__max_depth': [3, 5, 10, None],
        'decisiontreeclassifier__min_samples_split': [2, 5, 10]
    },

    'Random Forest': {
        'randomforestclassifier__n_estimators': [50, 100, 200],
        'randomforestclassifier__max_depth': [5, 10, None]
    },

    'KNN': {
        'kneighborsclassifier__n_neighbors': [3, 5, 7, 9],
        'kneighborsclassifier__weights': ['uniform', 'distance']
    }


}

cv=StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)


results=[]
best_models={}
for i in models:
    print("Training: ",i)

    grid=GridSearchCV(
        estimator=models[i],
        param_grid=param[i],
        cv=cv,
        scoring='f1_macro',  # Gives equal weights to all classes 
        n_jobs=-1,   # It splits the work into processor and perform task 
        refit=True  # Chooses the best parameter and model 
        )

    grid.fit(X_train, y_train)

    # to store the best model
    best_models[i] = grid.best_estimator_
    results.append(
        {
            'Model':i,
            'Best CV Score':grid.best_score_,
            'Best Params':grid.best_params_ 
        })


# To compare different models
results_df=pd.DataFrame(results)
results_df = results_df.sort_values(
    by='Best CV Score',
    ascending=False
)
print(results_df)
print("*"*50)


# To select best model 
best_model=results_df.iloc[0]['Model']
final_model=best_models[best_model]
print("Selected model: " , best_model)
print("*"*50)

# prediction 
y_pred =final_model.predict(X_test)


# evaluation metrics
print("Model Evaluation: ")
print("\nF1 Score:", f1_score(
    y_test, y_pred, average='macro'
))
print("*"*50)
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred, labels=['Fail', 'Pass']))
print("*"*50)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("*"*50)

# Sensitivity and Specificity
Sensitivity= recall_score(
    y_test,y_pred,pos_label='Fail'
)
print("Sensitivity: ", Sensitivity)
print("*"*50)

Specificity= recall_score(
    y_test,y_pred,pos_label='Pass'
)
print("Specificity: ", Specificity)




