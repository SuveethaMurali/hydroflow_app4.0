import streamlit as st

# Initialize session
if "page" not in st.session_state:
    st.session_state.page = "home"

st.title("🌧️ HydroFlow — Runoff Estimation App")
st.write("Choose your method to estimate surface runoff using SCN or Strangers Method.")

if st.button("Proceed to Method Selection ➡️"):
    st.session_state.page = "method"
    st.experimental_rerun()

# Navigation logic
if st.session_state.page == "method":
    st.experimental_set_query_params(page="method")
    st.switch_page("pages/1_Method_Selection.py")
