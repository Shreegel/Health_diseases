# import streamlit as st

# import pandas as pd

# st.write("# 10 Year Heart Disease Prediction")
# gender = st.selectbox("Enter yout gender",["Male","Female"])


# col1, col2, col3 = st.columns(3)

# # getting user inputgender = col1.selectbox("Enter your gender",["Male", "Female"])

# age = col2.number_input("Enter your age")
# education = col3.selectbox("Highest academic qualification",["High school diploma", "Undergraduate degree", "Postgraduate degree", "PhD"])

# isSmoker = col1.selectbox("Are you currently a smoker?",["Yes","No"])

# yearsSmoking = col2.number_input("Number of daily cigarettes")

# BPMeds = col3.selectbox("Are you currently on BP medication?",["Yes","No"])

# stroke = col1.selectbox("Have you ever experienced a stroke?",["Yes","No"])

# hyp = col2.selectbox("Do you have hypertension?",["Yes","No"])

# diabetes = col3.selectbox("Do you have diabetes?",["Yes","No"])

# chol = col1.number_input("Enter your cholesterol level")

# sys_bp = col2.number_input("Enter your systolic blood pressure")

# dia_bp = col3.number_input("Enter your diastolic blood pressure")

# bmi = col1.number_input("Enter your BMI")

# heart_rate = col2.number_input("Enter your resting heart rate")

# glucose = col3.number_input("Enter your glucose level")

# st.button('Predict')


# df_pred = pd.DataFrame([[gender,age,education,isSmoker,yearsSmoking,BPMeds,stroke,hyp,diabetes,chol,sys_bp,dia_bp,bmi,heart_rate,glucose]],

# columns= ['gender','age','education','currentSmoker','cigsPerDay','BPMeds','prevalentStroke','prevalentHyp','diabetes','totChol','sysBP','diaBP','BMI','heartRate','glucose'])

# df_pred['gender'] = df_pred['gender'].apply(lambda x: 1 if x == 'Male' else 0)

# df_pred['prevalentHyp'] = df_pred['prevalentHyp'].apply(lambda x: 1 if x == 'Yes' else 0)

# df_pred['prevalentStroke'] = df_pred['prevalentStroke'].apply(lambda x: 1 if x == 'Yes' else 0)

# df_pred['diabetes'] = df_pred['diabetes'].apply(lambda x: 1 if x == 'Yes' else 0)

# df_pred['BPMeds'] = df_pred['BPMeds'].apply(lambda x: 1 if x == 'Yes' else 0)

# df_pred['currentSmoker'] = df_pred['currentSmoker'].apply(lambda x: 1 if x == 'Yes' else 0)
# def transform(data):
#     result = 3
#     if(data=='High school diploma'):
#         result = 0
#     elif(data=='Undergraduate degree'):
#         result = 1
#     elif(data=='Postgraduate degree'):
#         result = 2
#     return(result)
# df_pred['education'] = df_pred['education'].apply(transform)


# model = joblib.load('fhs_rf_model.pkl')
# prediction = model.predict(df_pred)

# if st.button('Predict'):

#     if(prediction[0]==0):
#         st.write('<p class="big-font">You likely will not develop heart disease in 10 years.</p>',unsafe_allow_html=True)

#     else:
#         st.write('<p class="big-font">You are likely to develop heart disease in 10 years.</p>',unsafe_allow_html=True)
 

import streamlit as st
import pandas as pd
import pickle


st.write("# 10 Year Heart Disease Prediction")

gender = st.selectbox("Enter your gender", ["Male", "Female"])

col1, col2, col3 = st.columns(3)

# Getting user input
age = col2.number_input("Enter your age")
education = col3.selectbox("Highest academic qualification", ["High school diploma", "Undergraduate degree", "Postgraduate degree", "PhD"])

isSmoker = col1.selectbox("Are you currently a smoker?", ["Yes", "No"])
yearsSmoking = col2.number_input("Number of daily cigarettes")
BPMeds = col3.selectbox("Are you currently on BP medication?", ["Yes", "No"])
stroke = col1.selectbox("Have you ever experienced a stroke?", ["Yes", "No"])
hyp = col2.selectbox("Do you have hypertension?", ["Yes", "No"])
diabetes = col3.selectbox("Do you have diabetes?", ["Yes", "No"])

chol = col1.number_input("Enter your cholesterol level")
sys_bp = col2.number_input("Enter your systolic blood pressure")
dia_bp = col3.number_input("Enter your diastolic blood pressure")
bmi = col1.number_input("Enter your BMI")
heart_rate = col2.number_input("Enter your resting heart rate")
glucose = col3.number_input("Enter your glucose level")

if st.button('Predict'):
    df_pred = pd.DataFrame([[gender, age, education, isSmoker, yearsSmoking, BPMeds, stroke, hyp, diabetes, chol, sys_bp, dia_bp, bmi, heart_rate, glucose]], 
                           columns=['gender', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose'])

    df_pred['gender'] = df_pred['gender'].apply(lambda x: 1 if x == 'Male' else 0)
    df_pred['prevalentHyp'] = df_pred['prevalentHyp'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_pred['prevalentStroke'] = df_pred['prevalentStroke'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_pred['diabetes'] = df_pred['diabetes'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_pred['BPMeds'] = df_pred['BPMeds'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_pred['currentSmoker'] = df_pred['currentSmoker'].apply(lambda x: 1 if x == 'Yes' else 0)
    
    def transform(data):
        result = 3
        if data == 'High school diploma':
            result = 0
        elif data == 'Undergraduate degree':
            result = 1
        elif data == 'Postgraduate degree':
            result = 2
        return result
    
    df_pred['education'] = df_pred['education'].apply(transform)

    model = pickle.load(open('fhs_rf_model.pkl','rb'))
    prediction = model.predict(df_pred)

    if prediction[0] == 0:
        st.write('<p class="big-font">You likely will not develop heart disease in 10 years.</p>', unsafe_allow_html=True)
    else:
        st.write('<p class="big-font">You are likely to develop heart disease in 10 years.</p>', unsafe_allow_html=True)
