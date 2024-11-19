import streamlit as st
import pandas as pd 

st.title("hello")
st.image("./img/bigboss.jpg")
st.subheader("Jaturapat Polrob")
st.header("hello")
st.subheader("hello")

dt=pd.read_csv('./data/iris.csv')
st.header()
st.write(dt.head(10))

