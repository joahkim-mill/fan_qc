import pandas as pd
import plotly.graph_objects as go
import numpy as np
from scipy.fft import fft, fftfreq

col = ["Freq(Hz)", "SPL(dB)"] 
good = f"./piezo_data/good_fan_1_sample-data.txt"
data_good = pd.read_csv(good, sep='\t', header=None, skiprows=5, engine='python')
data_good.columns = ["Time", "Left", "Time_", "Right"]

bad = f"./piezo_data/bad fan 5.txt"
data_bad = pd.read_csv(bad, sep='\t', header=None, skiprows=1, engine='python')
data_bad.columns = col 
 
ground = "./piezo_data/ground truth.txt"
groundtruth = pd.read_csv(ground, sep='\t', header=None, skiprows=1, engine='python')
groundtruth.columns = col
# print(data)

tL = np.asarray(data_good["Time"])
left = np.asarray(data_good["Left"])
tR = np.asarray(data_good["Time_"])
right = np.asarray(data_good["Right"])

N = len(tL)
sample_rate = 44100 # Hz 
T = 1/sample_rate 

yf_L = fft(left)
xf_L = fftfreq(N, T)[:N//2]
y_L = 2.0/N * abs(yf_L[0:N//2])

yf_R = fft(right)
xf_R = fftfreq(N, T)[:N//2]
y_R = 2.0/N * abs(yf_R[0:N//2])

fig = go.Figure()
fig.add_trace(go.Scatter(x=xf_L, y=y_L, line_shape='linear', name=f"left")) 
fig.add_trace(go.Scatter(x=xf_R, y=y_R, line_shape='linear', name=f"right")) 
fig.show()
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=data_good["Time"], y=data_good["Left"], name="Left",
#                          line=dict(width=1.25)))
# fig.add_trace(go.Scatter(x=data_good["Time_"], y=data_good["Right"], name="Right",
#                          line=dict(width=1.25)))
# # fig.add_trace(go.Scatter(x=groundtruth["Freq(Hz)"], y=groundtruth["SPL(dB)"], name="Ground Truth",
# #                          line=dict(width=1.25)))
# # fig.add_trace(go.Scatter(x=data_good["Freq(Hz)"], y=data_good["SPL(dB)"], name="Good Data", 
# #                          line=dict(width=1.25)))
# # fig.add_trace(go.Scatter(x=data_bad["Freq(Hz)"], y=data_bad["SPL(dB)"], name="Bad Data",
# #                          line=dict(width=1.25)))

# fig.show()