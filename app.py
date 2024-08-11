import streamlit as st
import pandas as pd
import numpy as np
import time

email = st.text_input("Enter email")
password = st.text_input("Enter password")
btn = st.button("Login")

# If button is clicked
if btn: # Meaning button press hua hai
    if email == 'salmangtr@hotmail.com' and password == '1234':
        st.success("Login Successful")
        st.balloons() # Cringe shit
    else:
        st.error("Login Failed")

# Dropdown Menus 
# User selecting his Gender

gender = st.selectbox('Select gender', ['Male', 'Female', 'Others'])

# How to use a file uploader
file = st.file_uploader('Upload a csv file')

if file is not None: # Meaning file upload hui hai
    df = pd.read_csv(file)
    st.dataframe(df.describe())