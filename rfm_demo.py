
import pandas as pd 
import streamlit as st
import time
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from rfm import RFM
dataframe = pd.read_csv('updated_synthetic_consumer_data.csv', parse_dates=['invoice_date'])


st.title("Segmentation ❄️ App")

st.write('Upload your .csv file of consumers!!!')
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file, parse_dates=['invoice_date'])
    dataframe = dataframe.dropna()
    
    if uploaded_file is None:
        g =dataframe
    
    
rfm=st.checkbox(label="Run RFM Analysis")

if rfm:
            
        with st.spinner('We are not programs, Gerty. We are people'):
            time.sleep(5)
            st.success("Done!")
             
        r = RFM(dataframe, customer_id='cust_id', transaction_date='invoice_date', amount='amount')
        fig=r.plot_segment_distribution()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot(fig)
        
    
    
st.write("Generate a downloadable table of your results")
table=st.checkbox(label="Create Table", key='button2')

if table:

    r = RFM(dataframe, customer_id='cust_id', transaction_date='invoice_date', amount='amount')
    st.dataframe(r.rfm_table)

    csv=r.rfm_table.to_csv(index=False).encode('utf-8')

    
    st.download_button(
        "Press to Download",
        csv,
        "file.csv",
        "text/csv",
        key='download-csv'
            )
                
          
                
      