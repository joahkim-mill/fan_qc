import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from scipy.fft import fft, fftfreq
import streamlit as st

# """
# ### plotting the piezomic data after performing fft for a single dataset --> may take a little bit if the data is large

# col = ["Freq(Hz)", "SPL(dB)"] 
# good = f"./piezo_data/good_fan_1_sample-data.txt"
# data_good = pd.read_csv(good, sep='\t', header=None, skiprows=5, engine='python')
# data_good.columns = ["Time", "Left", "Time_", "Right"]

# for x in data_good.index:
#   if data_good.loc[x, "Right"] == "[-inf]":
#     data_good.loc[x, "Right"] = -999

# bad = f"./piezo_data/bad fan 5.txt"
# data_bad = pd.read_csv(bad, sep='\t', header=None, skiprows=1, engine='python')
# data_bad.columns = col 
 
# ground = "./piezo_data/ground truth.txt"
# groundtruth = pd.read_csv(ground, sep='\t', header=None, skiprows=1, engine='python')
# groundtruth.columns = col
# # print(data)

# tL = np.asarray(data_good["Time"])
# left = np.asarray(data_good["Left"])
# tR = np.asarray(data_good["Time_"])
# right = np.asarray(data_good["Right"])

# N = len(tL)
# sample_rate = 44100 # Hz 
# T = 1/sample_rate 

# # yf_L = fft(left)
# # xf_L = fftfreq(N, T)[:N//2]
# # y_L = 2.0/N * abs(yf_L[0:N//2])

# yf_R = fft(right)
# xf_R = fftfreq(N, T)[:N//2]
# y_R = 2.0/N * abs(yf_R[0:N//2])

# fig = go.Figure()
# # fig.add_trace(go.Scatter(x=xf_L, y=y_L, line_shape='linear', name=f"left")) 
# fig.add_trace(go.Scatter(x=xf_R, y=y_R, line_shape='linear', name=f"right")) 
# fig.show()
# # fig = go.Figure()
# # fig.add_trace(go.Scatter(x=data_good["Time"], y=data_good["Left"], name="Left",
# #                          line=dict(width=1.25)))
# # fig.add_trace(go.Scatter(x=data_good["Time_"], y=data_good["Right"], name="Right",
# #                          line=dict(width=1.25)))
# # # fig.add_trace(go.Scatter(x=groundtruth["Freq(Hz)"], y=groundtruth["SPL(dB)"], name="Ground Truth",
# # #                          line=dict(width=1.25)))
# # # fig.add_trace(go.Scatter(x=data_good["Freq(Hz)"], y=data_good["SPL(dB)"], name="Good Data", 
# # #                          line=dict(width=1.25)))
# # # fig.add_trace(go.Scatter(x=data_bad["Freq(Hz)"], y=data_bad["SPL(dB)"], name="Bad Data",
# # #                          line=dict(width=1.25)))

# # fig.show()

# """
data = ["good fan 1", "bad fan 4", "bad fan 5"]
spectrum = []
fig = make_subplots(rows=2, cols=1, subplot_titles=["Fan Spectrum Data", "Differences between Levels"], vertical_spacing=0.15)
for d in data:
  spectrum.append(pd.read_csv(f"./piezo_data/{d} spectrum.txt", sep='\t'))
  # print(spectrum["Level (dB)"][:745].mean())
  # fig.add_trace(go.Scatter(x=spectrum["Frequency (Hz)"], y=spectrum["Level (dB)"], name=d, line=dict(width=1)))
  # fig.add_trace(go.Scatter(x=[spectrum["Frequency (Hz)"][0], spectrum["Frequency (Hz)"][spectrum["Frequency (Hz)"].last_valid_index()]], y=[spectrum["Level (dB)"][:745].mean(), spectrum["Level (dB)"][:745].mean()], name=f"Avg {d}"))

# for i in range(3):
#   fig.add_trace(go.Scatter(x=spectrum[i]["Frequency (Hz)"], y=spectrum[i]["Level (dB)"], name=data[i], line=dict(width=1)))
# fig.show()
  
difference = spectrum[1]["Level (dB)"] - spectrum[0]["Level (dB)"]
diff2 = spectrum[2]["Level (dB)"] - spectrum[0]["Level (dB)"]
fig.add_trace(go.Scatter(x=spectrum[0]["Frequency (Hz)"], y=difference, name="Bad 4 - Good 1", line=dict(color="#a042db", width=1)),
              row=2, col=1)
fig.add_trace(go.Scatter(x=spectrum[0]["Frequency (Hz)"], y=diff2, name="Bad 5 - Good 1", line=dict(color="#ed8058", width=1)),
              row=2, col=1)
fig.add_trace(go.Scatter(x=spectrum[0]["Frequency (Hz)"], y=spectrum[0]["Level (dB)"], name=data[0], line=dict(color="#fa509c", width=1)),
              row=1, col=1)
fig.add_trace(go.Scatter(x=spectrum[1]["Frequency (Hz)"], y=spectrum[1]["Level (dB)"], name=data[1], line=dict(color="#a042db", width=1)),
              row=1, col=1)
fig.add_trace(go.Scatter(x=spectrum[2]["Frequency (Hz)"], y=spectrum[2]["Level (dB)"], name=data[2], line=dict(color="#ed8058", width=1)),
              row=1, col=1)
fig.update_layout(title="Fan Spectrum Differences", xaxis_title="Frequency [Hz]", yaxis_title="Level [dB]",
                  width=800, height=900)

fig.update_xaxes(title_text="Frequency [Hz]", row=1, col=1)
fig.update_yaxes(title_text="Level [dB]", row=1, col=1)

fig.update_xaxes(title_text="Frequency [Hz]", row=2, col=1)
fig.update_yaxes(title_text="Level [dB]", row=2, col=1)
st.plotly_chart(fig)