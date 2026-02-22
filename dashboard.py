import streamlit as st
import pandas as pd
import func_filter_dataframe as fd


# Hide the "Deploy" button
st.markdown(
    """
    <style>
    .stAppDeployButton {
        display:none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# (Optional) Hide the hamburger menu (upper right)
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

##########



st.header("RAAM Dashboard")
st.set_page_config(layout="wide") 

df = pd.read_csv("dashboard.csv")

df.index=pd.RangeIndex(start=1, stop=len(df) + 1, step=1)
df.index.name = "ID"
filtered_df = fd.filter_dataframe(df)
st.dataframe(filtered_df, use_container_width=True, column_config={
        "URL": st.column_config.LinkColumn(
            "URL",      # The label shown at the top of the column
        )
    })