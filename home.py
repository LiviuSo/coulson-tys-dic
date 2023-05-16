import streamlit as st
from PIL import Image

st.title("Michael Coulson's 'TYS' dictionary")

col1, empty_col, col2 = st.columns([1.5, 0.25, 1.5])

with col1:
    st.header("Sanskrit-English")
    st.text_input(label="Enter a Sanskrit work (IAST):")

with col2:
    result_container = st.empty()
    image = Image.open("dic/001-a-aṅgur-310.png")
    result_container.image(image)
