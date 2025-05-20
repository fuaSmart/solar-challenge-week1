import pandas as pd

def load_data():
    """Load and merge cleaned country data."""
    pass

def filter_data(df, countries):
    """Filter DataFrame by selected countries."""
    return df[df["country"].isin(countries)]