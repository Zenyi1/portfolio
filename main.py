import streamlit as st

st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/zenyi2.jpg")

with col2:
    st.title("Zenyi Gomez")
    content="""
    Hi, I am Zenyi! I am a software developer and entrepreneur currently researching machine learning models at the
    Alan Turing Institute. I am passionate about emerging technologies like blockchain and quantum computing. I am currently studying CS at the
    University fo Aberdeen, I have worked in multiple projects from Remote Sensing with Zephyrus Aerolabs to AI for healthcare at Unividoc. I love to read 
    and play chess in my free time and I am currently learning pentesting. 
    """
    st.info(content)