print("Hello world")

import streamlit as st
import pandas as pd 

st.title("My First Streamlit Website")
st.write("Halo semua Ini website Streamlit Pertamaku")

# Data frame example
data = pd.DataFrame({
    "Name": ["Dylan", "Kim", "Jos", "Axel", "William"],
    "Nilai": [85, 90, 78, 70, 80]
})

st.subheader("Data Student Club")
st.dataframe(data)

# Interaktif example
nilai = st.slider("Pilih nilai", 0,100,50)
st.write("Nilai yang kamu pilih", nilai)