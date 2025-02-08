import streamlit as st
import pandas as pd
from Filter import slicer
from Placement import fraud_dashboard


# Load the dataset
file_path = "fraud_data_with_skewness_kurtosis_outliers.csv"
df = pd.read_csv(file_path)

# Apply slicers
df = slicer(df)

# Run the dashboard
try:
    fraud_dashboard(df)
except Exception as e:
    st.write("[Oops! Everything got filtered out!]")