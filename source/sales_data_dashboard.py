"""
Data Visualization Dashboard
-----------------------------
This Streamlit app loads a CSV dataset and displays interactive charts
and summary metrics based on user-selected filters (e.g., region, product).

How to run this app:
1. Make sure you have Python and Streamlit installed.

2. Run the app from the terminal with:
       streamlit run source/sales_data_dashboard.py

3. The dashboard will open in your default web browser.
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("data/sales.csv", parse_dates=["Date"])

df = load_data()

# Sidebar filters
st.sidebar.title("Filters")
region = st.sidebar.selectbox("Select Region", df["Region"].unique())
product = st.sidebar.selectbox("Select Product", df["Product"].unique())

# Filter data
filtered = df[(df["Region"] == region) & (df["Product"] == product)]

# Main dashboard
st.title("📊 Sales Dashboard")
st.write(f"Showing data for **{product}** in **{region}**")

# Summary stats
st.metric("Total Units", filtered["Units"].sum())
st.metric("Total Revenue", f"${filtered['Revenue'].sum():,.2f}")

# Chart
fig = px.line(filtered, x="Date", y="Revenue", title="Revenue Over Time")
st.plotly_chart(fig, use_container_width=True)
