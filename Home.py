import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="💊",
)

st.write("# Welcome to TRxNLATE! 💊")


st.markdown(
    """
    ### TRxNSLATE is a Webapp that helps you read doctor's writings quickly and precisely.
    - Choose a way to read doctor's writings
    - Input your image!
    - Wait a second... 
    - Voila, we read them for you!
"""
)
st.write('## Are you ready?')
if st.button('Ready!'):
    st.write("Let's goo!!! 👍")
