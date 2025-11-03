import streamlit as st
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

st.title("📜 Calculation History")

history_file = os.path.join(os.getcwd(), "history.csv")
if not os.path.exists(history_file):
    st.info("No history found. Perform a calculation to create history.")
else:
    df = pd.read_csv(history_file)
    # show table of records
    st.dataframe(df[["timestamp","method","inputs","Q_mm"]].sort_values(by="timestamp", ascending=False))
    st.markdown("---")
    st.subheader("View hydrograph from a saved record")
    idx = st.selectbox("Choose record (most recent first):", df.index[::-1].tolist())
    rec = df.loc[idx]
    st.write(f"**Timestamp:** {rec['timestamp']}  \n**Method:** {rec['method']}  \n**Inputs:** {rec['inputs']}  \n**Q (mm):** {rec['Q_mm']}")
    # parse time_series
    ts = str(rec["time_series"]).split(";")
    runoff = np.array([float(x) for x in ts if x.strip()!=''])
    time = np.linspace(0, 10, len(runoff))
    fig, ax = plt.subplots()
    ax.plot(time, runoff, linewidth=2)
    ax.set_xlabel("Time (hr)")
    ax.set_ylabel("Runoff (mm)")
    ax.set_title("Saved Hydrograph")
    ax.grid(True)
    st.pyplot(fig)
    if st.button("Clear History File"):
        os.remove(history_file)
        st.success("History cleared. Rerun calculations to repopulate history.")