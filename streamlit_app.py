import streamlit as st 
import pandas as pd



st.write("hi, this is rakesh")




def read_excel(file):
    return pd.read_excel(file)



uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file is not None:
   
    df = read_excel(uploaded_file)
    

    st.write("### input example")
    st.dataframe(df)

   
  




