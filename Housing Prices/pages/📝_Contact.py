"""
This page is an example use of st.map here: 
https://docs.streamlit.io/library/api-reference/control-flow/st.form
"""
import streamlit as st 


with st.form("contact_form"):
    #st.write("Leave a message below:")
    txt = st.text_area("Leave a message below:")

    submitted = st.form_submit_button("Submit")   #every form must contain st.form_submit_button
    if submitted:  #do something with the data entered

        st.write("You pressed the `Submit` button.")
        st.write(f"Your text has {len(txt.split())} words")