import streamlit as st
import pandas as pd
import numpy as np
import time



# To run the website, i use the following command:
# streamlit run app.py

# How to add title to my website ?
st.title("Startup Dashboard")

# How to add a header and subheader ?
st.header("I am learning Streamlit")
st.subheader("And I am loving it!")

# "write" function that is used the most out of all 
# Used to print something normal on the screen
st.write("This is a normal text")

# Markdown is like html but easier, same as jupyter notebook
# I can refer to this website: https://www.markdownguide.org/

st.markdown("""
### My favorite movies
- Race 3
- Humshakals
- Dhoom 3
"""
)


# How to display code on our webpage ? 
st.code('''
def foo(input)
        return foo**2

x = foo(2)
        '''
)


# Latex <- Quite Powerful
# Mathematical symbols
st.latex('x^2 + y^2 + 2 = 0') # <- Wow

# ******* Display Elements ********
# Can read DF instantly 

df = pd.DataFrame({
    'name' : ['Nitish','Ankit','Anupam'],
    'marks' : [50,60,70],
    'package' : [10,12,14]
})

st.dataframe(df)


# Metrics
st.metric('Revenue', 'Rs 3L', '3%') # <- Wowzer

# Json

st.json({
    'name' : ['Nitish','Ankit','Anupam'],
    'marks' : [50,60,70],
    'package' : [10,12,14]
})


# ******** Displaying Media ************

# Images - Computer Vision related tasks
st.image('servser logo.png')
# st.video


# ******** Creating Layouts *************

# Sidebar -> Like a side bar options or contents on the side
st.sidebar.title('Sidebar ka Title')

# What if i want to add stuff side by side
col1, col2 = st.columns(2)

with col1:
    st.image('servser logo.png')

with col2:
    st.image('servser logo.png')


# Showing Status
# I executed something, i can give user the information about that 
# Telling user if his login was okay or not

st.error('Login Failed')
st.success('Login Success')
st.info('This is information')
st.warning('This is warning information')

# User is doing a task that will take time
# i can guide him with a progress bar
# Eg: User is uploading file

bar = st.progress(0)

for i in range(1,20):
    time.sleep(0.1)
    bar.progress(i)



# ******* MOST IMPORTANT ***********
# HOW TO TAKE USER INPUT ?

# Text input 
email = st.text_input('Enter email')

# Number input
num = st.number_input("Enter Age")

# Date
st.date_input("Enter regis date:")


# Buttons <------ SABSE IMPORTANT
# Let's make a login application

