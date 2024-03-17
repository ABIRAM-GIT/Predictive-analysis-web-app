import streamlit as st
import pandas as pd
st.title('Predicitive Analysis')
st.header('Section 1')
uploaded_file = 'E:\STUDY AND INTERN DOCS\DATA ANALYTICS INTERN\internshala\AssignmentData.xlsx'
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.header('Data Description')    
    st.write(df.describe())
    st.header('Data Types')    
    st.write(df.dtypes)
    st.header('Data Peek')
    st.write(df.head())
    st.header('Productivity Acheived?')
    sample_image = "E:\STUDY AND INTERN DOCS\DATA ANALYTICS INTERN\internshala\output.png"  # Replace with the URL of your image
    st.image(sample_image, use_column_width=True)
    st.header('Average Porductivity for Next four quarters') 
    st.text('Using ARIMA')
    pred =  pd.read_excel('E:\STUDY AND INTERN DOCS\DATA ANALYTICS INTERN\internshala\ForecastedProductivity.xlsx')
    st.write(pred.head())
    st.text('Using Rolling Average')
    st.header('0.538642361')
    st.header('Performance (lower is better)')
    st.text('''ARIMA Model:MAPE: 0.20694439728283937 MSE: 0.016943962068724786     
Rolling Averages Model: MAPE: 0.7150864927609806 MSE: 0.13281076690501914''')
st.header('Section 2')
st.header('Timeseries visualization with Date (on x-axis) and Total Number of Clicks (on y-axis)')
sample_image2 = "E:\STUDY AND INTERN DOCS\DATA ANALYTICS INTERN\internshala\output2.png"  # Replace with the URL of your image
st.image(sample_image2, use_column_width=True)
st.header('Sufficient Sample Size')
st.text('''Control Group Visitors: 7977808
Control Group Clicks: 874767
Experiment Group Visitors: 989983
Experiment Group Clicks: 258231        
Result of the hypothesis test: Reject(for confidence - 90)''')
st.text('''Control Group Conversion Rate: 10.96500442226737
Experiment Group Conversion Rate: 26.08438730766084
Sample Size Required: 1169''')
st.text('Sufficent Sample Size is acheived')

