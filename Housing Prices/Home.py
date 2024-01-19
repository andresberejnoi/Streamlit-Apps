import streamlit as st
import pandas as pd 

df = pd.read_csv('datasets/housing.csv')
df = df[:len(df)//10]  #using only a fraction of the dataset

st.markdown("# Raw Housing Data")
st.data_editor(
    df, 
    num_rows='dynamic', #allows deleting entire rows
)

#display a simple map
st.map(
    df, 
    longitude='longitude', 
    latitude='latitude', 
    size='population',
    #color='population',
    
)
