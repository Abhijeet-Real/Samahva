# Fraud Detection Dashboard 📊

## Overview 🚀
This project is a **Fraud Detection Dashboard** built using **Streamlit and Plotly**, designed to help analyze fraudulent transactions with **interactive visualizations and dynamic filtering**. The dashboard allows users to:
- Apply **real-time filters** to refine fraud analysis.
- Visualize fraud trends with **Sankey diagrams, Sunburst charts, Parallel Coordinates, and more**.
- Monitor fraud risk using **AI-driven analytics**.

---

## Features ✨
- 🔍 **Dynamic Filtering:** Use sidebar filters to refine transaction data.
- 📊 **Interactive Visualizations:** Includes 8 advanced fraud detection charts.
- ⚡ **Fast Performance:** Optimized for real-time fraud analysis.
- 🎨 **Consistent Color Theme:** Aesthetically appealing and easy to interpret.
- 🌍 **Geospatial Analysis:** Identify fraud hotspots with location-based insights.

---

## Installation 🛠
### Prerequisites:
Make sure you have **Python 3.8+** installed. Install dependencies using:
```bash
pip install -r requirements.txt
```

### Run the Dashboard:
```bash
streamlit run Streamlit.py
```

---

## Project Structure 📂
```
📦 Fraud_Detection_Dashboard
├── 📄 Streamlit.py  # Main Streamlit app
├── 📄 Graph.py      # Contains visualization functions
├── 📄 Filter.py     # Handles dynamic filters
├── 📄 Placement.py  # Manages UI layout
├── 📄 requirements.txt  # Required dependencies
└── 📊 fraud_data_with_skewness_kurtosis_outliers.csv  # Transaction dataset
```

---

## Usage Guide 🏗️
1. **Start the Streamlit App:** Run `streamlit run Streamlit.py`.
2. **Apply Filters:** Use the sidebar to filter by transaction type, fraud score, etc.
3. **Analyze Results:** View fraud patterns with advanced visualizations.

---

## Visualizations 📈
The dashboard includes **8 interactive fraud detection charts**:
- ✅ **Sankey Diagram** → Visualizes fraud transaction flow.
- ✅ **Sunburst Chart** → Shows fraud distribution across categories.
- ✅ **Parallel Coordinates** → Highlights fraud score patterns.
- ✅ **Treemap** → Displays fraud risk by merchant category.
- ✅ **Funnel Chart** → Tracks fraud detection process stages.
- ✅ **Radial Bar Chart** → Evaluates AI fraud model performance.
- ✅ **Waterfall Chart** → Shows fraud impact by various factors.
- ✅ **3D Scatter Plot** → Clusters fraud trends in a 3D view.

---

## Troubleshooting & Common Issues ❓
- **Issue: `ModuleNotFoundError: No module named 'streamlit'`**
  - 🔹 Run `pip install streamlit` to install Streamlit.
- **Issue: App shows blank space on the sides**
  - 🔹 Ensure `st.set_page_config(layout="wide")` is set in `Streamlit.py`.
- **Issue: Data not loading properly**
  - 🔹 Verify `fraud_data_with_skewness_kurtosis_outliers.csv` is present in the directory.

---

## Contribution Guidelines 🤝
We welcome contributions! To contribute:
1. **Fork this repository** 🍴.
2. **Create a new branch** (`git checkout -b feature-branch`).
3. **Commit your changes** (`git commit -m "Added new feature"`).
4. **Push to your branch** (`git push origin feature-branch`).
5. **Open a Pull Request**.

---

## License 📜
This project is licensed under the **MIT License**.

---

## Contact 📬
For queries or support, reach out via:
- 📧 **Email:** your-email@example.com
- 🐙 **GitHub Issues:** [Open an Issue](https://github.com/yourusername/Fraud_Detection_Dashboard/issues)

---

**Made with ❤️ using Streamlit & Plotly!** 🚀