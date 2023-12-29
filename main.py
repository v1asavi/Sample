
import streamlit as st
import numpy as np

st.set_page_config(layout ="wide")
st.title("Student Management System")
st.sidebar.title("Fee Management System")

st.sidebar.subheader("Add Student")
rollnumber=st.sidebar.number_input("Roll Number")
name=st.sidebar.text_input("Name")
fees=st.sidebar.number_input("Fees")
add=st.sidebar.button("Add")
