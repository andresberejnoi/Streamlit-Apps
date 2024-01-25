"""
This page is an example use of st.form here: 
https://docs.streamlit.io/library/api-reference/control-flow/st.form
"""
import streamlit as st 
from collections import Counter


with st.form("counter_form"):
    st.title("Word Counter Form")
    txt = st.text_area("Leave a message below:")

    submitted = st.form_submit_button("Submit")   #every form must contain st.form_submit_button
    if submitted:  #do something with the data entered
        num_words = len(txt.split())
        st.write("You pressed the `Submit` button.")
        st.write(f"Your text has {num_words} words.")

        if num_words > 0:
            st.write(f"Here is a frequency count of the top 15 words:")
            words = txt.split()
            word_frequency = Counter(words)
            top_15_words = word_frequency.most_common()[:15]

            st.bar_chart(dict(top_15_words))