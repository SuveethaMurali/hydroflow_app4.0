import streamlit as st

st.title("🧩 Select Method and Enter Inputs")

method = st.radio("Choose the Method:", ["SCS-CN Method", "Stranger’s Method"])

if method == "SCS-CN Method":
    st.subheader("🌿 SCS Curve Number (CN) Method")
    st.latex(r"Q = \frac{(P - 0.2S)^2}{(P + 0.8S)}, \quad S = \frac{25400}{CN} - 254")

    P = st.number_input("Rainfall (P) in mm", min_value=0.0, step=0.1, format="%.2f")
    CN = st.number_input("Curve Number (CN)", min_value=30.0, max_value=99.9, step=0.1, format="%.2f")

    if st.button("Calculate Runoff"):
        st.session_state["method"] = "SCS-CN"
        st.session_state["P"] = float(P)
        st.session_state["CN"] = float(CN)
        st.switch_page("pages/2_Runoff_Output.py")

elif method == "Stranger’s Method":
    st.subheader("🌊 Stranger’s Method")
    st.latex(r"Q = C \times P")

    P = st.number_input("Rainfall (P) in mm", min_value=0.0, step=0.1, format="%.2f")
    C = st.number_input("Runoff Coefficient (C)", min_value=0.0, max_value=1.0, step=0.01, format="%.2f")

    if st.button("Calculate Runoff"):
        st.session_state["method"] = "Stranger’s"
        st.session_state["P"] = float(P)
        st.session_state["C"] = float(C)
        st.switch_page("pages/2_Runoff_Output.py")

st.divider()
st.caption("⬅️ Use the Start Calculation button on Home to return anytime.")
