import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os

st.title("📈 Runoff Calculation Results")

# Ensure input values exist
if "method" not in st.session_state:
    st.error("⚠️ Please start from the home page and select a method.")
    st.stop()

method = st.session_state["method"]
st.subheader(f"Method Used: {method}")

# compute runoff and hydrograph
if method == "SCS-CN":
    P = float(st.session_state["P"])
    CN = float(st.session_state["CN"])
    S = (25400.0 / CN) - 254.0
    Q = ((P - 0.2 * S) ** 2) / (P + 0.8 * S) if P > 0.2 * S else 0.0
    inputs = {"P": P, "CN": CN}

elif method == "Stranger’s":
    P = float(st.session_state["P"])
    C = float(st.session_state["C"])
    Q = C * P
    inputs = {"P": P, "C": C}

st.success(f"💧 Estimated Runoff (Q): **{Q:.3f} mm**")

# hydrograph generation (simple symmetric triangular approximated by exponential decay for display)
time = np.linspace(0, 10, 50)
runoff = np.maximum(0, Q * np.exp(-0.35 * time))

fig, ax = plt.subplots(figsize=(8,4))
ax.plot(time, runoff, marker='', color='tab:blue', linewidth=2)
ax.set_xlabel("Time (hr)")
ax.set_ylabel("Runoff (mm)")
ax.set_title("Hydrograph")
ax.grid(True)
st.pyplot(fig)

# show table
df = pd.DataFrame({"Time (hr)": np.round(time,3), "Runoff (mm)": np.round(runoff,6)})
st.dataframe(df.head(20))

# save to history.csv
history_file = os.path.join(os.getcwd(), "history.csv")
record = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "method": method,
    "inputs": str(inputs),
    "Q_mm": float(np.round(Q,6)),
    "time_series": ";".join([str(round(x,6)) for x in runoff.tolist()])
}
# append to CSV
import csv, os
fieldnames = ["timestamp","method","inputs","Q_mm","time_series"]
file_exists = os.path.exists(history_file)
with open(history_file, "a", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    if not file_exists:
        writer.writeheader()
    writer.writerow(record)

st.download_button(
    "📥 Download Runoff Data as CSV",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name="runoff_results.csv",
    mime="text/csv"
)

st.info("✅ Result saved to history. Use the History page to view past calculations.")