# Import Modul
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import streamlit as st

@st.cache()
def load_data():
    
    #Load Data
    df = pd.read_csv('vehicle_maintenance_datatransform.csv')

    x = df[["Vehicle_Model","Mileage","Maintenance_History","Reported_Issues","Vehicle_Age","Fuel_Type","Transmission_Type","Engine_Size","Odometer_Reading","Last_Service_Date","Warranty_Expiry_Date","Owner_Type","Insurance_Premium","Service_History","Accident_History","Fuel_Efficiency","Tire_Condition","Brake_Condition","Battery_Status"]]
    y = df[['Need_Maintenance']]

    return df, x, y

#Algoritma Decision Tree
@st.cache()
def train_model(x,y):
    model = DecisionTreeClassifier(
            ccp_alpha=0.0, class_weight=None, criterion='entropy',
            max_depth=4, max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            random_state=42, splitter='best'
        )
    
    model.fit(x,y)

    score = model.score(x,y)

    return model, score

def predict(x,y, features):
    model, score = train_model(x,y)

    prediction = model.predict(np.array(features).reshape(1,-1))

    return prediction, score