import streamlit as st

st.set_page_config(page_title="HydroFlow", page_icon="💧", layout="centered")

st.title("💧 HydroFlow - Runoff Estimation System")

st.markdown("""
### Welcome to **HydroFlow**
An interactive web app to estimate **surface runoff** using two hydrological methods:
- 🌿 **SCS Curve Number (CN) Method**
- 🌊 **Stranger’s Method**

This project helps visualize runoff through **hydrographs**, **tables**, and stored history.
""")

st.divider()

st.markdown("#### 👇 Click below to begin your estimation:")

if st.button("🚀 Start Calculation"):
    st.switch_page("pages/1_Method_Selection.py")

st.divider()
st.caption("Developed by: Your Name | Institution: Your College | Department: Civil Engineering")
