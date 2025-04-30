# File: app.py
import streamlit as st
import pandas as pd

# Page configuration and theming
st.set_page_config(
    page_title="RSG Fuel System Configurator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark mode toggle with CSS injection
def apply_dark_mode():
    st.markdown(
        """
        <style>
        body {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        .css-1d391kg, .css-1siy2j7 {
            background-color: #0E1117 !important;
            color: #FAFAFA !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Sidebar elements
with st.sidebar:
    st.image("assets/cummins_logo.png", use_column_width=True)
    dark_mode = st.checkbox("Enable Dark Mode")
    st.markdown("---")
    st.title("Data Upload & Filters")
    uploaded_file = st.file_uploader(
        "Upload your spreadsheet (CSV or Excel)", type=["csv", "xlsx"]
    )

if dark_mode:
    apply_dark_mode()

# Main application logic
if uploaded_file:
    # Read data
    if uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file, engine='openpyxl')
    else:
        df = pd.read_csv(uploaded_file)

    # Create dynamic filters
    filter_columns = df.select_dtypes(include=[object, 'category', bool, 'int64']).columns.tolist()
    with st.sidebar.expander("Filters", expanded=True):
        for col in filter_columns:
            options = ["Please select"] + sorted(df[col].dropna().unique().tolist())
            choice = st.selectbox(f"Filter by {col}", options, key=col)
            if choice and choice != "Please select":
                df = df[df[col] == choice]

    # Display filtered data
    st.dataframe(df, use_container_width=True)

    # Download button for filtered results
    def convert_df_to_csv(dataframe):
        return dataframe.to_csv(index=False).encode('utf-8')

    csv_data = convert_df_to_csv(df)
    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv_data,
        file_name="filtered_data.csv",
        mime="text/csv"
    )

else:
    st.info("Upload a file to get started with filtering and exporting your data.")


# File: requirements.txt
# ----------------------
# Framework and data libraries
streamlit>=1.15.0
pandas>=1.3.0
openpyxl>=3.0.0


# File: .streamlit/config.toml
# ----------------------------
[theme]
primaryColor = "#E6131A"  # Cummins red
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F5F5F5"
font = "sans serif"


# File: README.md
# ---------------
# RSG Fuel System Configurator

This Streamlit app allows you to upload a dataset (CSV or Excel), apply dynamic filters based on your data columns, and download the filtered results.

## Features
- **Dynamic Filters**: Automatically generates filter controls for any column in your dataset.
- **Data Download**: Export filtered data as a CSV file.
- **Branding**: Includes Cummins logo and theme colors.
- **Dark Mode**: Toggle dark mode for UI comfort.

## Getting Started
1. Clone this repository:
   ```bash
   git clone https://github.com/Angela-McPherren/RSG_Fuel_System_Configurator.git
   cd RSG_Fuel_System_Configurator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```
4. Deploy to Streamlit Cloud by connecting your GitHub repository.

## File Structure
```
├── app.py
├── requirements.txt
├── .streamlit
│   └── config.toml
└── assets
    └── cummins_logo.png  
