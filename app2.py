import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout = 'wide', page_title = 'StartUp Analysis')

# Import the Data using Pandas
df = pd.read_csv('startup_clean.csv')
df['date'] = pd.to_datetime(df['date'], errors = 'coerce')
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month


def load_inevstor_details(investor):
    st.title(investor)
    
    # Load the recent 5 investments of the investors
    last5_df = df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    # Biggest Investments
    col1, col2 = st.columns(2)
    with col1:
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending = False).head()
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots() # Plotting a graph instead of displaying a table
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)

    # Sectors invested in
    with col2:
        vertical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors invested in')
        fig1, ax1 = plt.subplots() # Plotting a graph instead of displaying a table
        ax1.pie(vertical_series, labels=vertical_series.index, autopct="%0.01f")
        st.pyplot(fig1)

    # Stage at which they invested 
    col3, col4 = st.columns(2)
    with col3:
        stage_series = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum()
        st.subheader( 'Stage Invested in')
        fig2, ax2 = plt.subplots()
        ax2.pie(stage_series, labels = stage_series.index)
        st.pyplot(fig2)

    # City they invested in
    with col4:
        city_invested = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
        st.subheader( 'City Invested in')
        fig3, ax3 = plt.subplots()
        ax3.pie(city_invested, labels = city_invested.index)
        st.pyplot(fig3)

    # YoY investment
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    st.subheader('YoY Investments')
    fig4, ax4 = plt.subplots()
    ax4.plot(year_series.index, year_series.values)
    st.pyplot(fig4)


def load_overall_analysis():
    st.title('Overall Analysis')

    col5, col6, col7, col8 = st.columns(4)

    # Total capital Invested
    with col5:
        total_capital = round(df['amount'].sum())
        st.metric("Total Capital: ", str(total_capital) + 'Cr')

    # Maximum Capital Invested in a Startup
    with col6:
        max_funding = df.groupby('startup')['amount'].max().sort_values(ascending = False).head(1).values[0]
        st.metric("Max Capital Invested: ", str(max_funding) + 'Cr')

    # Average ticket size
    with col7:
        avg_funding = df.groupby('startup')['amount'].sum().mean()
        st.metric('Average Funding: ', str(round(avg_funding)) + 'Cr')

    # Total funded Startups
    with col8:
        num_startups = df['startup'].nunique()
        st.metric('Total startups: ', num_startups)

    # Month on Month Graph
    st.header('Month on Month Graph')
    # Dropdown to select an option and store it in a variable to see what the user selected
    selected_option = st.selectbox('Select Type', ['Total', 'Count'])

    if selected_option == 'Total':
        temp_df = df.groupby(['year','month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year','month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str') 
    st.subheader('MoM Graph')
    fig5, ax5 = plt.subplots()
    ax5.plot(temp_df['x_axis'], temp_df['amount'])
    st.pyplot(fig5)


st.sidebar.title("Startup Funding Analysis")
option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Startup', 'Investor'])

if option == 'Overall Analysis':
    # btn0 = st.sidebar.button('Show Overall Analysis')
    # if btn0:
        load_overall_analysis()

elif option == 'Startup':
    st.sidebar.selectbox('Select Startup', sorted(df['startup'].unique().tolist()))
    st.title("Startup Analysis")
    btn1 = st.sidebar.button('Find Startup Details')

else:
    selected_investor = st.sidebar.selectbox('Select Startup', sorted(set(df['investors'].str.split(',').sum())))
    st.title('Investor Analysis')
    btn2 = st.sidebar.button('Find Investor Details')

    if btn2:
        load_inevstor_details(selected_investor)
