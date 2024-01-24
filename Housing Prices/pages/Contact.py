import streamlit as st 


with st.form("contact_form"):
    #st.write("Leave a message below:")
    txt = st.text_area("Leave a message below:")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("You pressed the `Submit` button")