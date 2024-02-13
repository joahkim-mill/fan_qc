import pandas as pd 
import numpy as np 
from scipy.fft import fft, fftfreq
import streamlit as st 
import plotly.graph_objects as go 


filepath = f"./accel_data/good_8.csv"
data = pd.read_csv(filepath)
 
fig = go.Figure()

t = np.asarray(data["time"])
ax = np.asarray(data["x_accel"])
ay = np.asarray(data["y_accel"])
az = np.asarray(data["z_accel"])
a = np.hstack((ax.reshape((-1,1)), ay.reshape((-1,1)), az.reshape((-1,1))))  # [ax , ay, az] columnwise

N = len(t)
sample_rate = 338 # Hz 
T = 1/sample_rate 
yf_x = fft(ax)
xf_x = fftfreq(N, T)[:N//2]
y_x = 2.0/N * abs(yf_x[0:N//2])
fig.add_trace(go.Scatter(x=xf_x, y=y_x, line_shape='linear', name=f"ax")) 

yf_y = fft(ay)
xf_y = fftfreq(N, T)[:N//2]
y_y = 2.0/N * abs(yf_y[0:N//2])
fig.add_trace(go.Scatter(x=xf_y, y=y_y, line_shape='linear', name=f"ay")) 

yf_z = fft(az)
xf_z = fftfreq(N, T)[:N//2]
y_z = 2.0/N * abs(yf_z[0:N//2])
fig.add_trace(go.Scatter(x=xf_z, y=y_z, line_shape='linear', name=f"az")) 

fig.update_layout(title=f"Good Fan (8) FFT", 
                xaxis_title="Frequency [Hz]", 
              #   yaxis_title="SPL [dB]",
                height=600,
                width=800)
fig.update_yaxes(range=[0, 1])
st.plotly_chart(fig)

filepath = f"./accel_data/bad_3.csv"
data = pd.read_csv(filepath)
 
fig2 = go.Figure()

t = np.asarray(data["time"])
ax = np.asarray(data["x_accel"])
ay = np.asarray(data["y_accel"])
az = np.asarray(data["z_accel"])
a = np.hstack((ax.reshape((-1,1)), ay.reshape((-1,1)), az.reshape((-1,1))))  # [ax , ay, az] columnwise

N = len(t)
sample_rate = 361 # Hz 
T = 1/sample_rate 
yf_x = fft(ax)
xf_x = fftfreq(N, T)[:N//2]
y_x = 2.0/N * abs(yf_x[0:N//2])
fig2.add_trace(go.Scatter(x=xf_x, y=y_x, line_shape='linear', name=f"ax")) 

yf_y = fft(ay)
xf_y = fftfreq(N, T)[:N//2]
y_y = 2.0/N * abs(yf_y[0:N//2])
fig2.add_trace(go.Scatter(x=xf_y, y=y_y, line_shape='linear', name=f"ay")) 

yf_z = fft(az)
xf_z = fftfreq(N, T)[:N//2]
y_z = 2.0/N * abs(yf_z[0:N//2])
fig2.add_trace(go.Scatter(x=xf_z, y=y_z, line_shape='linear', name=f"az")) 

fig2.update_layout(title=f"Bad Fan (3) FFT", 
                xaxis_title="Frequency [Hz]", 
              #   yaxis_title="SPL [dB]",
                height=600,
                width=800)
fig2.update_yaxes(range=[0, 1])

st.plotly_chart(fig2)



# fig = go.Figure()
# fig2 = go.Figure()

# sample_rates = [360, 336, 338]
# sample_rates2 = [360, 336, 361]
# for g in range(7,10):
#   filepath = f"./accel_data/good_{g}.csv"
#   data = pd.read_csv(filepath)

#   t = np.asarray(data["time"])
#   ax = np.asarray(data["x_accel"])
#   ay = np.asarray(data["y_accel"])
#   az = np.asarray(data["z_accel"])
#   a = np.hstack((ax.reshape((-1,1)), ay.reshape((-1,1)), az.reshape((-1,1))))  # [ax , ay, az] columnwise

#   N = len(t)
#   sample_rate = sample_rates[g-7] # Hz 
#   T = 1/sample_rate 
#   yf = fft(ax)
#   xf = fftfreq(N, T)[:N//2]
#   y_x = 2.0/N * abs(yf[0:N//2])

  
#   fig.add_trace(go.Scatter(x=xf, y=y_x, line_shape='linear', name=f"Good Fan {g}")) 

# fig.update_layout(title=f"Good Fan FFT", 
#                   xaxis_title="Frequency [Hz]", 
#                 #   yaxis_title="SPL [dB]",
#                   height=600,
#                   width=800)

# for b in range(1,4):
#   filepath = f"./accel_data/bad_{b}.csv"
#   data = pd.read_csv(filepath)

#   t = np.asarray(data["time"])
#   ax = np.asarray(data["x_accel"])
#   ay = np.asarray(data["y_accel"])
#   az = np.asarray(data["z_accel"])
#   a = np.hstack((ax.reshape((-1,1)), ay.reshape((-1,1)), az.reshape((-1,1))))  # [ax , ay, az] columnwise

#   N = len(t)
#   sample_rate = sample_rates2[b-1] # Hz 
#   T = 1/sample_rate 
#   yf = fft(ax)
#   xf = fftfreq(N, T)[:N//2]
#   y_x = 2.0/N * abs(yf[0:N//2])

#   fig2.add_trace(go.Scatter(x=xf, y=y_x, line_shape='linear', name=f"Bad Fan {b}")) 

# fig2.update_layout(title=f"Bad Fan FFT", 
#                   xaxis_title="Frequency [Hz]", 
#                 #   yaxis_title="SPL [dB]",
#                   height=600,
#                   width=800)

# st.title(f"Fan FFT Analysis of Accelerometer Data")
# st.plotly_chart(fig)
# st.plotly_chart(fig2)
