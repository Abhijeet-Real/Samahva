import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
file_path = "fraud_data_with_skewness_kurtosis_outliers.csv"
df = pd.read_csv(file_path)

# Title
st.title("Fraud Detection Dashboard")

# Summary Statistics
st.subheader("Summary Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Transactions", len(df))
col2.metric("Fraudulent Transactions", df[df["Fraud_Score"] > 0.7].shape[0])
col3.metric("Average Fraud Score", round(df["Fraud_Score"].mean(), 2))

# Fraud Alerts Table
st.subheader("Real-Time Fraud Alerts")
st.dataframe(df[df["Fraud_Score"] > 0.7][["Transaction_ID", "User_ID", "Transaction_Amount", "Fraud_Score"]].sort_values(by="Fraud_Score", ascending=False))

# Fraud Risk Heatmap
st.subheader("Fraud Risk Heatmap")
fig = px.scatter_geo(df, locations="Transaction_Location", color="Fraud_Score",
                     title="Geospatial Fraud Risk", projection="natural earth")
st.plotly_chart(fig)

# Fraud Score Distribution
st.subheader("Fraud Score Distribution")
fig_hist = px.histogram(df, x="Fraud_Score", nbins=50, title="Fraud Score Distribution")
st.plotly_chart(fig_hist)