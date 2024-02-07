import pandas as pd 
import numpy as np 
from plotly import graph_objects as go 

# read in csv to access data 
filename = "good_fan_1_accel_500hz.csv" # depends on which folder you're in
accelerations = pd.read_csv(filename)
# make them into columns
t = np.asarray(accelerations["time"]).reshape((-1,1))
a_x = np.asarray(accelerations["x_accel"]).reshape((-1,1))
a_y = np.asarray(accelerations["y_accel"]).reshape((-1,1))
a_z = np.asarray(accelerations["z_accel"]).reshape((-1,1))
a = np.hstack((a_x, a_y, a_z))

num_samples = t.shape[0]
# print(a_x[:2], a_y[:2], a_z[:2])
# print(a[:2, :])
dt = t[1:] - t[:-1] 
# print(dt[:5], dt[-5:])  # as a check if it aligns with ~100Hz

# integrate twice to get position 
v_x = np.zeros((num_samples, 1))
p_x = np.zeros((num_samples, 1))
for i in range(1, num_samples):
    v_x[i] = a_x[i-1] * dt[i-1] + v_x[i-1]
    p_x[i] = 0.5 * a_x[i-1] * dt[i-1] * dt[i-1] + v_x[i-1] * dt[i-1] + p_x[i-1]


# plot --> based on plot, if very off, apply some smoothing/interpolation/calibration/re-zeroing ?
fig_x = go.Figure()
fig_x.add_trace(go.Scatter(x=t.ravel(), y=a_x.ravel(), name="accel_x"))
fig_x.add_trace(go.Scatter(x=t.ravel(), y=v_x.ravel(), name="vel_x"))
fig_x.add_trace(go.Scatter(x=t.ravel(), y=p_x.ravel(), name="pos_x"))
fig_x.update_layout(title="Plot of Vibrating Fan")
fig_x.show()
# fft for frequencies

