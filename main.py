import streamlit as st
import pandas as pd
import os

# Import profilling capability
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report






with st.sidebar:
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("Data Analysis")
    choice = st.radio("Navigation", ["Upload", "Profiling",])
    st.info("Created by- Hemant Kumar   roll_number--  300012721001 ..........step1- upload file, step2- profilling")

if os.path.exists("sourcedata.csv"):
    df = pd.read_csv("sourcedata.csv", index_col=None)

if choice == "Upload":
    st.title("Upload your data for Modelling!")
    file = st.file_uploader("Upload your Dataset Here")
    if file:
        df = pd.read_csv(file, index_col=None)
        df.to_csv("sourcedata.csv", index=None)

        st.dataframe(df)


if choice == "Profiling":
    st.title("Automated Exploratory Data Analysis")
    profile_report = df.profile_report()
    st_profile_report(profile_report)


