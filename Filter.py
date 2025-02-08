import streamlit as st
import pandas as pd

# Function to create slicers
def slicer(df):
    st.sidebar.header("Filters")
    categorical_filters = []
    numeric_filters = []

    columns_to_filter = [
        "Transaction_Amount", "Transaction_Type", "Currency", "Merchant_Category", "Device_Used",
        "Transaction_Location", "Payment_Method", "Avg_Transaction_Amount",
        "Transaction_Frequency", "Login_Frequency", "Multiple_Devices_Used", "Transaction_Velocity", "Fraud_Score",
        "Anomaly_Score", "Historical_Fraud_Prob", "Chargeback_History", "Geolocation_Mismatch", "IP_Reputation_Score",
        "Card_Usage_Pattern"
    ]

    # Ensure Account_Age is considered continuous
    numeric_filters.append("Account_Age")

    for col in columns_to_filter:
        if df[col].nunique() > 1 and df[col].nunique() < len(df) * 0.9:  # Exclude near-unique categorical values
            categorical_filters.append(col)
        elif df[col].dtype in ['int64', 'float64'] and df[col].nunique() > 1:  # Ensure column is numeric and not unique
            numeric_filters.append(col)

    # Display categorical filters first using dropdown
    for col in categorical_filters:
        selected_values = st.sidebar.multiselect(f"Filter {col}", df[col].dropna().unique())
        if selected_values:
            df = df[df[col].isin(selected_values)]

    # Display numeric filters below
    for col in numeric_filters:
        min_val, max_val = df[col].min(), df[col].max()
        if pd.notna(min_val) and pd.notna(max_val):  # Ensure no NaN values
            st.sidebar.slider(f"Filter {col}", float(min_val), float(max_val), (float(min_val), float(max_val)))
    
    return df