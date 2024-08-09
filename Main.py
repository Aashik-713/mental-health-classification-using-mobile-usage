import mysql.connector
import pandas as pd
from data_processing import preprocessing, encoding  
from model import train_logistic_regression
import subprocess
import os
import pickle

# Connect to MySQL and fetch data
mydb = mysql.connector.connect(host='localhost', user='root', password='Aashik_713', database="student")
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Impact_of_Mobile_Phone_on_Students_Health")
results = mycursor.fetchall()
columns = [desc[0] for desc in mycursor.description]

df = pd.DataFrame(results, columns=columns)
mycursor.close()
mydb.close()

# Preprocess and encode data
df_preprocessed = preprocessing(df)
df_encoded = encoding(df_preprocessed)

# Path to the model file
model_path = 'logistic_regression_model.pkl'

# Check if the model file exists
if os.path.exists(model_path):
    # Load the model if it exists
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
else:
    # Train and save the model if it doesn't exist
    model = train_logistic_regression(df_encoded, 'Health rating')  # Ensure 'Health rating' is the correct target column

    # Save the model
    with open(model_path, 'wb') as model_file:
        pickle.dump(model, model_file)

# Run the Streamlit app
subprocess.run(["streamlit", "run", "streamlit_app.py"])
