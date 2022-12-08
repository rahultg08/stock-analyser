# Import the necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import datetime

# set title and logo for the web page
st.set_page_config(page_title="Microsoft Stock Prices", page_icon="https://cdn.cdnlogo.com/logos/m/95/microsoft.svg")

# Adding social media links and tags to the web page

"[![Star](https://img.shields.io/badge/Rahul-TG-blue)](https://github.com/rahultg08/)"
"""
[![Follow](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rahultg08)
[![Follow](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/rahultg08)

# Microsoft's Stock Analysis

"""

# Sidebar to the webApp
st.markdown('---')
# Sidebar Configuration
st.sidebar.image('https://cdn.cdnlogo.com/logos/m/6/microsoft.svg', width=200)
st.sidebar.markdown(' # Microsoft Stock Price Analysis')
st.sidebar.markdown('Microsoft is a leading global vendor of computer software, hardware for computer, mobile and gaming systems, and cloud services.')
st.sidebar.markdown('Stock data from 2015 to 2021')
st.sidebar.markdown('Visualization of Microsoft \'s Stock Price Trends and Patterns over a given time span')

st.markdown('---')
st.sidebar.write('Developed by Rahul TG')
st.sidebar.write('Contact @ rahultg741@gmail.com')

# Import the dataset into a dataframe
df = pd.read_csv("Microsoft_Stock.csv")

# Convert series object to datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Reset the index to the Date column
df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')
df.reset_index(drop=True, inplace=True)
df.set_index('Date', inplace=True)

# Displaying data in App
st.subheader('Look through the Data')
st.dataframe(df.head())

# Displaying statistical info
st.subheader('Statistical Info about the Data')
st.write(df.describe())

# Selection for specific time frame
st.subheader('Select the Date Interval for analysis')
df_select = df

# Adding 2 columns
col1, col2 = st.columns(2)

# col1 for start date
with col1:
  st.write('Select Start Date')
  start_date = st.date_input('Start Date', min_value = datetime.date(2015,4,1), max_value=datetime.date(2021,3,31), value=datetime.date(2015,4,1))

with col2:
  st.write('Select End Date')
  end_date = st.date_input('End Date', min_value=datetime.date(2014,4,1), max_value=datetime.date(2021,3,31), value=datetime.date(2021,3,31))

if(start_date != None or end_date != None):
  if(start_date < end_date):
    df_select = df[start_date:end_date]
  else:
    st.warning('Invalid Range - Re-enter the dates')

# Open and Close Prices
st.subheader("Open & Close Prices for Microsoft Stock")
st.markdown("\n\n")
st.line_chart(df_select[['Open', 'Close']])

# High and Low Prices
st.subheader("High & Low Prices for Microsoft Stock")
st.markdown("\n\n")
st.line_chart(df_select[['High', 'Low']])

# Volume of Stock Traded
st.subheader("Volume of Microsoft Stock Traded")
st.markdown('\n\n')
st.bar_chart(df_select['Volume'])

# Moving average from 50 days to 250 days
st.subheader('Moving Averages of Open & Close Stock Prices')
moveavg_len = st.slider('Select the number of days for Moving Averages', min_value = 0, max_value = 250, value = 50)
moveavg_oc = df_select[['Open', 'Close']].rolling(50).mean()
st.line_chart(moveavg_oc)
