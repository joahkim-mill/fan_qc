import pandas as pd 
import numpy as np 
from scipy.fft import fft, fftfreq
import streamlit as st 
import plotly.graph_objects as go 

i=5
url = f"https://github.com/joahkim-mill/fan_qc/raw/main/prebaked_delta/Fan%20{i}.txt"
data = pd.read_csv(url, sep=" ", header=None, skiprows=14, engine='python')
data.columns = ["Freq(Hz)", "SPL(dB)", "Phase(degrees)"] 

N = len(data["Freq(Hz)"])
# print("N: ", N)
sample_rate = 48000 # Hz 
T = 1/sample_rate 
yf = fft(data)
xf = fftfreq(N, T)[:N//2]
y = 2.0/N * abs(yf[0:N//2])

fig = go.Figure()
fig.add_trace(go.Scatter(x=xf, y=y[:,1], line_shape='linear')) 

fig.update_layout(title=f"Pre-Baked Fan #{i}", 
                  xaxis_title="Frequency [Hz]", 
                #   yaxis_title="SPL [dB]",
                  height=600,
                  width=800)

st.title(f"Fan FFT Analysis")
st.plotly_chart(fig)

