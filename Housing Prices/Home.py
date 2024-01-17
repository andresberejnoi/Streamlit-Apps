import streamlit as st
import pandas as pd 
from matplotlib import colormaps


df = pd.read_csv('datasets/housing.csv')
df = df[:len(df)//2]  #reducing the dataframe in half

st.markdown("# Raw Housing Data")
st.dataframe(df)

#display a simple map
st.map(
    df, 
    longitude='longitude', 
    latitude='latitude', 
    size='population',
    #color='population',
    
)
