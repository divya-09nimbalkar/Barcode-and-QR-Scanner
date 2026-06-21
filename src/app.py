import streamlit as st
from scanner import scan_image

st.title("📷 Barcode & QR Scanner")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    with open("temp.png", "wb") as f:
        f.write(uploaded_file.getbuffer())
    result = scan_image("temp.png")
    st.success(result)
