import streamlit as st
import pandas as pd

# 제목 표시
st.title("DataFrame Viewer")

# Pickle 파일에서 데이터 읽기
@st.cache_data
def load_data(file_path):
    return pd.read_pickle(file_path)

# 데이터 로드
file_path = "data.pkl"  # Pickle 파일 경로
try:
    data = load_data(file_path)
    st.success("Data loaded successfully!")
    st.write("### Data Preview", data)
except FileNotFoundError:
    st.error(f"Pickle file '{file_path}' not found. Please upload the file.")

# 파일 업로드 기능
uploaded_file = st.file_uploader("Upload your Pickle file", type="pkl")
if uploaded_file:
    data = pd.read_pickle(uploaded_file)
    st.write("### Uploaded Data Preview", data)
