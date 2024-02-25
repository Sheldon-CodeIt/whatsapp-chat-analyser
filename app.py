import streamlit as st
from preprocessor import preprocess

st.sidebar.title('Whatsapp Chat Analyzer')

label = "Upload a file"

uploaded_file = st.sidebar.file_uploader(label)

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode('utf-8')
    df = preprocess(data)

    st.dataframe(df)