import streamlit as st
import matplotlib.pyplot as plt
import datetime
import plotly.graph_objs as go

import appdirs as ad
ad.user_cache_dir = lambda *args: "/tmp"
import yfinance as yf

# Specify title and logo for the webpage.
# Set up your web app
st.set_page_config(layout="wide", page_title="WebApp_Demo")

# Sidebar
st.sidebar.title("Input Ticker")
symbol = st.sidebar.text_input('Please enter the stock symbol: ', 'NVDA').upper()
# Selection for a specific time frame.
col1, col2 = st.sidebar.columns(2, gap="medium")
with col1:
    sdate = st.date_input('Start Date',value=datetime.date(2024,1,1))
with col2:
    edate = st.date_input('End Date',value=datetime.date.today())

st.title(f"{symbol}")

stock = yf.Ticker(symbol)
if stock is not None:
  # Display company's basics
  st.subheader("Company Basics")  # Add a subheader for better organization

  col1, col2, col3 = st.columns(3)  # Create three columns for layout # Indented here

  with col1:  # Indented here
    st.write(f"**Sector:** {stock.info['sector']}")
    st.write(f"**Industry:** {stock.info['industry']}") 
    st.write(f"**Website:** {stock.info['website']}")

  with col2:  # Indented here
    st.write(f"**Beta:** {stock.info['beta']}")
    st.write(f"**Market Cap:** {stock.info['marketCap']}")  
    st.write(f"**Trailing P/E:** {stock.info['trailingPE']}") 

  with col3: # Indented here
    st.write(f"**Dividend Yield:** {stock.info['dividendYield']}")
    st.write(f"**52-Week High:** {stock.info['fiftyTwoWeekHigh']}")
    st.write(f"**52-Week Low:** {stock.info['fiftyTwoWeekLow']}")
  
  data = yf.download(symbol, start=sdate, end=edate)  # Moved inside the 'if' block
  if data is not None:
    st.write(data.describe())
    st.line_chart(data['Close'],x_label="Date",y_label="Close")
  else:
    st.error("Failed to fetch historical data.") 

else:
  st.error("Failed to fetch company information.")  # More specific error message
