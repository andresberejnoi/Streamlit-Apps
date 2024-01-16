import streamlit as st
import pandas as pd 


df = pd.read_csv('datasets/housing.csv')

st.markdown("# Raw Housing Data")
df