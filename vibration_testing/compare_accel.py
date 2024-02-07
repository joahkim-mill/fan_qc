import pandas as pd 
import numpy as np 
from plotly import graph_objects as go 
from plotly.subplots import make_subplots

## ------- GOOD FAN DATA -------- ##
# read in csv to access data 
good = pd.read_csv("good_fan_1_accel.csv")

# make them into columns
t_g = np.asarray(good["time"])
ax_g = np.asarray(good["x_accel"])
ay_g = np.asarray(good["y_accel"])
az_g = np.asarray(good["z_accel"])

## ------- BAD FAN DATA -------- ##
bad = pd.read_csv("bad_fan_4_accel.csv")

# make them into columns
t_b = np.asarray(bad["time"])
ax_b = np.asarray(bad["x_accel"])
ay_b = np.asarray(bad["y_accel"])
az_b = np.asarray(bad["z_accel"])

## --------- CREATE PLOTS --------- ##
fig = make_subplots(rows=3, cols=1,
                    subplot_titles=("X", "Y", "Z"), 
                    vertical_spacing=0.05
                    )

# acceleration in x
fig.add_trace(
    go.Scatter(x=t_b, y=ax_b, name="ax_b", line=dict(color="#aa81f0")),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=t_g, y=ax_g, name="ax_g", line=dict(color="#f5bad4")),
    row=1, col=1
)

# acceleration in y
fig.add_trace(
    go.Scatter(x=t_b, y=ay_b, name="ay_b", line=dict(color="#aa81f0")),
    row=2, col=1
)
fig.add_trace(
    go.Scatter(x=t_g, y=ay_g, name="ay_g", line=dict(color="#f5bad4")),
    row=2, col=1
)

# acceleration in z
fig.add_trace(
    go.Scatter(x=t_b, y=az_b, name="az_b", line=dict(color="#aa81f0")),
    row=3, col=1
)
fig.add_trace(
    go.Scatter(x=t_g, y=az_g, name="az_g", line=dict(color="#f5bad4")),
    row=3, col=1
)

fig.update_layout(title="Comparison of Acceleration Data between Fans", 
                  height = 1200,
                  width = 1100)
fig.show()