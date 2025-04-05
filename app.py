import streamlit as st
import pandas as pd

# Load the provided data
df = pd.read_excel('/mnt/data/rsg dynamic filter.xlsx')

# Streamlit UI for dynamic filtering
st.title("Dynamic Filter for System Configuration")

# Filter categories
application = st.selectbox('Select APPLICATION', df['Application'].unique())
body_mfg = st.selectbox('Select BODY MFG', df['BODY MFG INPUTS'].unique())
body_model = st.selectbox('Select BODY MODEL', df['BODY MODEL INPUTS'].unique())
chassis_manuf = st.selectbox('Select CHASSIS MANUFACTURE', df['CHASSIS MANUFACTURE INPUTS'].unique())
chassis_model = st.selectbox('Select CHASSIS MODEL', df['CHASSIS MODEL INPUTS'].unique())
chassis_type = st.selectbox('Select CHASSIS TYPE', df['Chassis Type'].unique())
chassis_cab = st.selectbox('Select CHASSIS CAB', df['CHASSIS CAB'].unique())
cng_mounting = st.selectbox('Select CNG MOUNTING', df['CNG MOUNTING INPUTS'].unique())
system_type = st.selectbox('Select SYSTEM TYPE', df['System Type'].unique())
system_dge = st.selectbox('Select SYSTEM DGE', df['System DGE'].unique())

# Apply filters to the DataFrame
filtered_df = df[
    (df['Application'] == application) &
    (df['BODY MFG INPUTS'] == body_mfg) &
    (df['BODY MODEL INPUTS'] == body_model) &
    (df['CHASSIS MANUFACTURE INPUTS'] == chassis_manuf) &
    (df['CHASSIS MODEL INPUTS'] == chassis_model) &
    (df['Chassis Type'] == chassis_type) &
    (df['CHASSIS CAB'] == chassis_cab) &
    (df['CNG MOUNTING INPUTS'] == cng_mounting) &
    (df['System Type'] == system_type) &
    (df['System DGE'] == system_dge)
]

# Display filtered results
if not filtered_df.empty:
    st.write(filtered_df[['SYSTEM PART #', 'Additional Kits Needed 1', 'Additional Kits Needed 2', 'Additional Kits Needed 3', 
                          'Additional Kits Needed 4', 'Additional Kits Needed 5', 'Additional Kits Needed 6', 'System Cost', 
                          'FET', 'Install', 'Total']])
else:
    st.write("No data matches your selection.")
