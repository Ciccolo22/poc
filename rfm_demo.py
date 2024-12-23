import pandas as pd
import altair as alt 
import streamlit as st
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from pandasai import Agent
from rfm import RFM
import os
import time

dataframe = pd.read_csv('updated_synthetic_consumer_data.csv', parse_dates=['invoice_date'])

load_dotenv()

os.environ["PANDASAI_API_KEY"] = "PANDASAI_API_KEY"

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
            
       if rfm:
            
        with st.spinner('We are not programs, Gerty. We are people'):
            time.sleep(5)
            st.success("Done!")
             
        r = RFM(dataframe, customer_id='cust_id', transaction_date='invoice_date', amount='amount')
        fig=r.rfm_table
        chart= alt.Chart(fig).mark_bar().encode(
        y=alt.Y('segment:N', title='Segment'),
        x=alt.X('count()', title='Count'),
        color=alt.Color('segment:N', scale=alt.Scale(scheme='tableau10'), legend=None)
    ).properties(
        title='Counts by Segment'
    ).configure_axis(grid=False)

        st.altair_chart(chart, use_container_width=True)
    
    
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
                
            
prompt = st.text_area("Ask some questions about your data???")
if prompt:
       with st.spinner("the world has turned and left me here... generating a response.."):
        agent=Agent(r.rfm_table)
        response=agent.chat(prompt)
        st.write(response)
          
                
      
