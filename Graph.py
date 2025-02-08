import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


# Define consistent color theme
color_theme = [
    'rgba(31, 119, 180, 0.8)', 'rgba(255, 127, 14, 0.8)', 'rgba(44, 160, 44, 0.8)',
    'rgba(214, 39, 40, 0.8)', 'rgba(148, 103, 189, 0.8)', 'rgba(140, 86, 75, 0.8)',
    'rgba(227, 119, 194, 0.8)', 'rgba(127, 127, 127, 0.8)', 'rgba(188, 189, 34, 0.8)',
    'rgba(23, 190, 207, 0.8)'
]

# Function to create Sankey Diagram
def plot_sankey_diagram(df):
    fraud_threshold = 0.7  # Threshold for fraud detection
    df['Fraud_Label'] = df['Fraud_Score'].apply(lambda x: 'Fraud' if x > fraud_threshold else 'Legit')
    grouped_data = df.groupby(['Merchant_Category', 'Transaction_Type', 'Fraud_Label']).size().reset_index(name='Count')
    merchants = grouped_data['Merchant_Category'].unique().tolist()
    transactions = grouped_data['Transaction_Type'].unique().tolist()
    fraud_labels = ['Fraud', 'Legit']
    all_labels = merchants + transactions + fraud_labels
    label_to_index = {label: i for i, label in enumerate(all_labels)}
    source = grouped_data['Merchant_Category'].map(label_to_index).tolist() + grouped_data['Transaction_Type'].map(label_to_index).tolist()
    target = grouped_data['Transaction_Type'].map(label_to_index).tolist() + grouped_data['Fraud_Label'].map(label_to_index).tolist()
    values = grouped_data['Count'].tolist() * 2
    fig = go.Figure(go.Sankey(node=dict(pad=20, thickness=25, label=all_labels, color=color_theme[:len(all_labels)]), link=dict(source=source, target=target, value=values, color='rgba(100, 149, 237, 0.4)')))
    fig.update_layout(title_text="Fraud Transaction Flow", font_size=12, paper_bgcolor='rgba(240, 240, 240, 1)', plot_bgcolor='rgba(240, 240, 240, 1)')
    st.plotly_chart(fig)

# Function to create Sunburst Chart
def plot_sunburst_chart(df):
    fig = px.sunburst(df, path=['Transaction_Location', 'Merchant_Category', 'Fraud_Label'], values='Transaction_Amount', color='Fraud_Score', color_continuous_scale='blues', title="Fraud Hierarchy")
    st.plotly_chart(fig)

# Function to create Parallel Coordinates Plot
def plot_parallel_coordinates(df):
    fig = px.parallel_coordinates(df, dimensions=['Transaction_Amount', 'Fraud_Score', 'IP_Reputation_Score'], color='Fraud_Score', color_continuous_scale='viridis', title="Fraud Patterns")
    st.plotly_chart(fig)

# Function to create Treemap
def plot_treemap(df):
    fig = px.treemap(df, path=['Merchant_Category', 'Transaction_Type'], values='Transaction_Amount', color='Fraud_Score', color_continuous_scale='reds', title="Fraud Distribution")
    st.plotly_chart(fig)

# Function to create Funnel Chart
def plot_funnel_chart(df):
    stages = df.groupby('Fraud_Label').size().reset_index(name='Count')
    fig = px.funnel(stages, x='Fraud_Label', y='Count', color='Fraud_Label', color_discrete_sequence=color_theme[:len(stages)], title="Fraud Detection Stages")
    st.plotly_chart(fig)

# Function to create Radial Bar Chart
def plot_radial_bar_chart(df):
    metrics = pd.DataFrame({'Metric': ['Precision', 'Recall', 'F1-Score'], 'Value': [0.85, 0.78, 0.81]})
    fig = px.line_polar(metrics, r='Value', theta='Metric', line_close=True, color_discrete_sequence=['orange'], title="Model Performance")
    st.plotly_chart(fig)

# Function to create Waterfall Chart
def plot_waterfall_chart(df):
    fraud_effects = {'Factors': ['Chargebacks', 'High Transaction Value', 'Multiple Devices'], 'Impact': [30, 50, 20]}
    fig = px.bar(fraud_effects, x='Factors', y='Impact', color='Impact', color_continuous_scale='plasma', title="Fraud Impact", text_auto=True)
    st.plotly_chart(fig)

# Function to create 3D Scatter Plot
def plot_3d_scatter(df):
    fig = px.scatter_3d(df, x='Transaction_Amount', y='Fraud_Score', z='Anomaly_Score', color='Fraud_Score', color_continuous_scale='magma', title="Fraud Clustering")
    st.plotly_chart(fig)
