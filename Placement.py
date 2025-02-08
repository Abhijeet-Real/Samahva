import streamlit as st
from Graph import plot_sankey_diagram, plot_treemap, plot_funnel_chart, plot_waterfall_chart, plot_sunburst_chart, plot_parallel_coordinates, plot_radial_bar_chart, plot_3d_scatter

# Remove extra space from left and right
def set_page_config():
    st.set_page_config(layout="wide")

set_page_config()

def fraud_dashboard(df):
    st.title("Fraud Detection Dashboard")
    
    # Layout structure with 3 columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sankey Diagram - Fraud Flow")
        try:
            plot_sankey_diagram(df)
        except NameError:
            st.write("[Sankey Diagram Placeholder]")
        
        st.subheader("Treemap - Fraud Distribution")
        try:
            plot_treemap(df)
        except NameError:
            st.write("[Treemap Placeholder]")

        st.subheader("Funnel Chart - Fraud Detection Stages")
        try:
            plot_funnel_chart(df)
        except NameError:
            st.write("[Funnel Chart Placeholder]")
        
        st.subheader("Waterfall Chart - Fraud Impact")
        try:
            plot_waterfall_chart(df)
        except NameError:
            st.write("[Waterfall Chart Placeholder]")

    with col2:
        st.subheader("Sunburst Chart - Fraud Hierarchy")
        try:
            plot_sunburst_chart(df)
        except NameError:
            st.write("[Sunburst Chart Placeholder]")
        
        st.subheader("Parallel Coordinates - Fraud Patterns")
        try:
            plot_parallel_coordinates(df)
        except NameError:
            st.write("[Parallel Coordinates Placeholder]")
    
        st.subheader("Radial Bar Chart - Model Performance")
        try:
            plot_radial_bar_chart(df)
        except NameError:
            st.write("[Radial Bar Chart Placeholder]")
        
        st.subheader("3D Scatter Plot - Fraud Clustering")
        try:
            plot_3d_scatter(df)
        except NameError:
            st.write("[3D Scatter Plot Placeholder]")