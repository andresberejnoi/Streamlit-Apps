import streamlit as st
import pandas as pd 

df = pd.read_csv('datasets/housing.csv')
df = df[:len(df)//10]  #using only a fraction of the dataset

st.markdown("# Raw Housing Data")
st.markdown("""This web application uses the Californian housing data from the third edition of the book ["Hands-On Machine Learning With Scikit-Learn, Keras, And Tensorflow"](https://amzn.to/3pC2A5b) by Aurélien Géron. I can't recommend this book enough for those looking to build a solid foundation on machine learning and machine learning frameworks (the link is a referral link).""")
st.data_editor(
    df, 
    num_rows='dynamic', #allows deleting entire rows
)

#display a simple map
st.markdown("## Map of Population Clusters In Dataset")
st.map(
    df, 
    longitude='longitude', 
    latitude='latitude', 
    size='population',
    #color='population',
    
)
