import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data  # Hypothetical utility function

# Page config
st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")

# Title
st.title("🌍 Cross-Country Solar Potential Analysis")

# Sidebar widgets
st.sidebar.header("Filters")
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=["Benin", "Sierra Leone", "Togo"],
    default=["Benin", "Sierra Leone", "Togo"]
)

# Load data (placeholder - replace with actual data loading)
@st.cache_data
def load_data():
    # Assuming cleaned CSVs are in data/processed/
    benin = pd.read_csv("data/processed/benin_clean.csv")
    sierra_leone = pd.read_csv("data/processed/sierra_leone_clean.csv")
    togo = pd.read_csv("data/processed/togo_clean.csv")
    return pd.concat([benin, sierra_leone, togo])

df = load_data()
filtered_df = df[df["country"].isin(selected_countries)]

# Key Visualizations
tab1, tab2 = st.tabs(["📊 Solar Metrics", "🏆 Top Regions"])

with tab1:
    # Boxplot for GHI
    st.subheader("Global Horizontal Irradiance (GHI) Comparison")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(data=filtered_df, x="country", y="GHI", ax=ax)
    st.pyplot(fig)

with tab2:
    # Top regions table
    st.subheader("Top 5 Regions by Average GHI")
    top_regions = filtered_df.groupby("region")["GHI"].mean().nlargest(5).reset_index()
    st.dataframe(top_regions, hide_index=True)

# Footer
st.markdown("---")
st.caption("MoonLight Energy Solutions | Data Source: Energy Data Info")