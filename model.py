import pickle
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

def train_logistic_regression(df, target_column):
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    smote = SMOTE(random_state=90)
    X_train_res, y_train_res = smote.fit_resample(X_train, y_train)
    
    scaler = StandardScaler()
    X_train_res = scaler.fit_transform(X_train_res)
    X_test = scaler.transform(X_test)
    
    log_reg = LogisticRegression(max_iter=1000)
    log_reg.fit(X_train_res, y_train_res)
    
    # Save the model using pickle
    with open('logistic_regression_model.pkl', 'wb') as model_file:
        pickle.dump(log_reg, model_file)
    
    return log_reg
