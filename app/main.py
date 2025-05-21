import pandas as pd
import streamlit as st
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(page_title="Cross-Country Solar Potential Analysis", layout="wide")

# Sidebar filters
st.sidebar.header("Filters")
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=["Benin", "Sierra Leone", "Togo"],
    default=["Benin", "Sierra Leone", "Togo"]
)

SCRIPT_DIR = Path(__file__).parent

@st.cache_data
def load_data():
    try:
        # Correct paths based on your file structure
        benin_path = SCRIPT_DIR / "../data/benin-malanville.csv"
        sierra_path = SCRIPT_DIR / "../data/sierraleone-bumbuna.csv"
        togo_path = SCRIPT_DIR / "../data/togo-dapaong_qc.csv"
        
        # Load each country's data
        benin = pd.read_csv(benin_path.resolve())
        benin['country'] = 'Benin'
        
        sierra_leone = pd.read_csv(sierra_path.resolve())
        sierra_leone['country'] = 'Sierra Leone'
        
        togo = pd.read_csv(togo_path.resolve())
        togo['country'] = 'Togo'
        
        # Combine all data
        combined_df = pd.concat([benin, sierra_leone, togo], ignore_index=True)
        return combined_df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Load the data
df = load_data()

if df is not None:
    # Filter the data
    filtered_df = df[df["country"].isin(selected_countries)]
    
    # Create tabs
    tab1, tab2 = st.tabs(["Solar Metrics", "Top Regions"])
    
    with tab1:
        st.subheader("Global Horizontal Irradiance (GHI) Comparison")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.boxplot(data=filtered_df, x="country", y="GHI", ax=ax)
        st.pyplot(fig)
    
    with tab2:
        st.subheader("Top 5 Regions by Average GHI")
        if 'region' in filtered_df.columns:
            top_regions = filtered_df.groupby("region")["GHI"].mean().nlargest(5).reset_index()
            st.dataframe(top_regions, hide_index=True)
        else:
            st.warning("Region data not available in the dataset")
else:
    st.error("Failed to load data. Please check the data files.")

# Footer
st.markdown("---")
st.caption("MoonLight Energy Solutions | Data Source: Energy Data Info")