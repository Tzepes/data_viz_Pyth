import streamlit as st
import pandas as pd

# Load data
@st.cache
def load_data(file):
    return pd.read_parquet(file)

# Display table for selected categories
def display_table(data, selected_categories):
    st.subheader("Data Preview")
    if selected_categories:
        st.write(data[selected_categories].head())
    else:
        st.write(data.head())

# Main function
def main():
    st.title("Data Visualization App")

    # File upload
    st.sidebar.title("Upload File")
    file = st.sidebar.file_uploader("Upload Parquet File", type=["parquet"])

    if file is not None:
        data = load_data(file)
        st.success("Data loaded successfully!")

        # Select categories for display
        st.sidebar.title("Select Categories")
        categories = st.sidebar.multiselect("Select Categories to Display", data.columns)

        # Display data
        display_table(data, categories)

if __name__ == "__main__":
    main()
