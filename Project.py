import streamlit as st

#Sidebar for navigation
sidebar = st.sidebar.selectbox(
    "Choose a page:",
    ["Home", "Questionnaire", "Visualization of the data"]
)
