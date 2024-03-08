import pandas as pd
import numpy as np
from plotly import graph_objects as go
from plotly.subplots import make_subplots
from scipy.fft import fft, fftfreq

dataname = '68 with spring 45pwm.txt'
data = pd.read_csv(f'./{dataname}', sep=',', skiprows=12)
data.columns = ['time[ms]', 'x', 'y', 'z']
# print(data)

# fig = go.Figure()
fig = make_subplots(rows=3, cols=1,
                    subplot_titles=("X", "Y", "Z"), 
                    vertical_spacing=0.05
                    )

# acceleration in x
fig.add_trace(
    go.Scatter(x=data['time[ms]'], y=data['x'], name='x accel', line=dict(color="#aa81f0")),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=data['time[ms]'], y=data['y'], name='y accel', line=dict(color="#aa81f0")),
    row=2, col=1
)
fig.add_trace(
    go.Scatter(x=data['time[ms]'], y=data['z'], name='z accel', line=dict(color="#aa81f0")),
    row=3, col=1
)

# fig.add_trace(go.Scatter())
# fig.add_trace(go.Scatter(x=data['time[ms]'], y=data['y'], name='y accel'))
# fig.add_trace(go.Scatter(x=data['time[ms]'], y=data['z'], name='z accel'))

data2 = 'bad fan test.txt'
data = pd.read_csv(f'./{data2}', sep=',', skiprows=12)
data.columns = ['time[ms]', 'x', 'y', 'z']
# print(data)

fig.add_trace(
    go.Scatter(x=data['time[ms]'], y=data['x'], name='bad fan x accel', line=dict(color="#41adf0")),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=data['time[ms]'], y=data['y'], name='bad fan y accel', line=dict(color="#41adf0")),
    row=2, col=1
)
fig.add_trace(
    go.Scatter(x=data['time[ms]'], y=data['z'], name='bad fan z accel', line=dict(color="#41adf0")),
    row=3, col=1
)

data3 = '28 with spring 45pwm.txt'
data = pd.read_csv(f'./{data3}', sep=',', skiprows=12)
data.columns = ['time[ms]', 'x', 'y', 'z']
# print(data)

fig.add_trace(
    go.Scatter(x=data['time[ms]'], y=data['x'], name='28 x accel', line=dict(color="#40b892")),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=data['time[ms]'], y=data['y'], name='28 y accel', line=dict(color="#40b892")),
    row=2, col=1
)
fig.add_trace(
    go.Scatter(x=data['time[ms]'], y=data['z'], name='28 z accel', line=dict(color="#40b892")),
    row=3, col=1
)

# fig.add_trace(go.Scatter(x=data['time[ms]'], y=data['x'], name='bad fan x accel'))
# fig.add_trace(go.Scatter(x=data['time[ms]'], y=data['y'], name='bad fan y accel'))
# fig.add_trace(go.Scatter(x=data['time[ms]'], y=data['z'], name='bad fan z accel'))

fig.show()


# fig = go.Figure()

# t = np.asarray(data["time[ms]"])
# ax = np.asarray(data["x"])
# ay = np.asarray(data["y"])
# az = np.asarray(data["z"])
# a = np.hstack((ax.reshape((-1,1)), ay.reshape((-1,1)), az.reshape((-1,1))))  # [ax , ay, az] columnwise

# N = len(t)
# sample_rate = 333 # Hz 
# T = 1/sample_rate 
# yf_x = fft(ax)
# xf_x = fftfreq(N, T)[:N//2]
# y_x = 2.0/N * abs(yf_x[0:N//2])
# fig.add_trace(go.Scatter(x=xf_x, y=y_x, line_shape='linear', name=f"ax")) 

# yf_y = fft(ay)
# xf_y = fftfreq(N, T)[:N//2]
# y_y = 2.0/N * abs(yf_y[0:N//2])
# fig.add_trace(go.Scatter(x=xf_y, y=y_y, line_shape='linear', name=f"ay")) 

# yf_z = fft(az)
# xf_z = fftfreq(N, T)[:N//2]
# y_z = 2.0/N * abs(yf_z[0:N//2])
# fig.add_trace(go.Scatter(x=xf_z, y=y_z, line_shape='linear', name=f"az")) 

# fig.update_layout(title=f"Fan FFT of {dataname}", 
#                 xaxis_title="Frequency [Hz]", 
#               #   yaxis_title="SPL [dB]",
#                 height=600,
#                 width=800)
# fig.update_yaxes(range=[0, 1])
# fig.show()