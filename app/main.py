import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data  # Hypothetical utility function


st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")


st.title("🌍 Cross-Country Solar Potential Analysis")


st.sidebar.header("Filters")
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=["Benin", "Sierra Leone", "Togo"],
    default=["Benin", "Sierra Leone", "Togo"]
)


@st.cache_data
def load_data():
    benin = pd.read_csv("../data/raw/benin-malanville.csv")
    sierra_leone = pd.read_csv("../data/raw/sierra_leone_clean.csv")
    togo = pd.read_csv("../data/raw/togo_clean.csv")
    return pd.concat([benin, sierra_leone, togo])

df = load_data()
filtered_df = df[df["country"].isin(selected_countries)]


tab1, tab2 = st.tabs([" Solar Metrics", " Top Regions"])

with tab1:

    st.subheader("Global Horizontal Irradiance (GHI) Comparison")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(data=filtered_df, x="country", y="GHI", ax=ax)
    st.pyplot(fig)

with tab2:

    st.subheader("Top 5 Regions by Average GHI")
    top_regions = filtered_df.groupby("region")["GHI"].mean().nlargest(5).reset_index()
    st.dataframe(top_regions, hide_index=True)

# Footer
st.markdown("---")
st.caption("MoonLight Energy Solutions | Data Source: Energy Data Info")