import pandas as pd 
import plotly.graph_objects as go 
from scipy.signal import find_peaks
import streamlit as st

"""
Once noise recordings from REW have been exported as .txt files, can be read in here and extrapolated for 
peak frequencies above a specified dB threshold. The peaks and corresponding dB/Hz values will be printed.
Can optionally plot the data as well.
"""

filename = "Fan 1"
data = pd.read_csv(f"prebaked_delta\{filename}.txt", sep=" ", header=None, skiprows=14)
data.columns = ["Freq(Hz)", "SPL(dB)", "Phase(degrees)"] 
# print(data)
# data.to_csv(f"C:/fan_qc/{filename}.csv")  ## to write the csv file --> not necessary

dB_threshold = 45  # dB threshold at which we want to find which frequencies are peaks
peaks, _ = find_peaks(data["SPL(dB)"], height=dB_threshold) # find the peaks in the dB

# print("        Peaks     ")
# for p in peaks:
#     print(f"{data["SPL(dB)"][p]} dB      {data["Freq(Hz)"][p]} Hz")


 ## plot data ##

fig = go.Figure()

fig.add_trace(go.Scatter(x=data["Freq(Hz)"], y=data["SPL(dB)"], name="Noise Recording"))
fig.add_trace(go.Scatter(mode='markers', x=data["Freq(Hz)"][peaks], y=data["SPL(dB)"][peaks], name="Peak Frequencies", marker=dict(color='red')))
fig.update_layout(title=f"{filename} Noise Recording", 
                  xaxis_title="Frequency Spectrum [Hz]", 
                  yaxis_title="SPL[dB]",
                  height=600,
                  width=800
                  )
fig.update_xaxes(title_font_color="black")
fig.update_yaxes(title_font_color="black")
# fig.show()
st.plotly_chart(fig)

# print out the peak data points
st.text("        Peaks        ")
for p in peaks:
    st.text(f"{data["SPL(dB)"][p]} dB      {data["Freq(Hz)"][p]} Hz \n")

