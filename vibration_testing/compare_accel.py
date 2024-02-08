import pandas as pd 
import numpy as np 
from plotly import graph_objects as go 
from plotly.subplots import make_subplots

## ------- GOOD FAN DATA -------- ##
# read in csv to access data 
good7 = pd.read_csv("./accel_data/good_7.csv")

# make them into columns
t_g7 = np.asarray(good7["time"])
ax_g7 = np.asarray(good7["x_accel"])
ay_g7 = np.asarray(good7["y_accel"])
az_g7 = np.asarray(good7["z_accel"])

## ------- BAD FAN DATA -------- ##
bad1 = pd.read_csv("./accel_data/bad_1.csv")

# make them into columns
t_b1 = np.asarray(bad1["time"])
ax_b1 = np.asarray(bad1["x_accel"])
ay_b1 = np.asarray(bad1["y_accel"])
az_b1 = np.asarray(bad1["z_accel"])

## ------- BAD FAN DATA -------- ##
bad2 = pd.read_csv("./accel_data/bad_2.csv")

# make them into columns
t_b2 = np.asarray(bad2["time"])
ax_b2 = np.asarray(bad2["x_accel"])
ay_b2 = np.asarray(bad2["y_accel"])
az_b2 = np.asarray(bad2["z_accel"])

## ------- BAD FAN DATA -------- ##
bad3 = pd.read_csv("./accel_data/bad_3.csv")

# make them into columns
t_b3 = np.asarray(bad3["time"])
ax_b3 = np.asarray(bad3["x_accel"])
ay_b3 = np.asarray(bad3["y_accel"])
az_b3 = np.asarray(bad3["z_accel"])

"""
#### --------- CREATE PLOTS --------- ####
fig = make_subplots(rows=3, cols=1,
                    subplot_titles=("X", "Y", "Z"), 
                    vertical_spacing=0.05
                    )

# acceleration in x
fig.add_trace(
    go.Scatter(x=t_b1, y=ax_b1, name="ax_b1", line=dict(color="#aa81f0")),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=t_b2, y=ax_b2, name="ax_b2", line=dict(color="#41adf0")),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=t_b3, y=ax_b3, name="ax_b3", line=dict(color="#40b892")),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=t_g, y=ax_g, name="ax_g", line=dict(color="#f5bad4")),
    row=1, col=1
)

# acceleration in y
fig.add_trace(
    go.Scatter(x=t_b1, y=ay_b1, name="ay_b1", line=dict(color="#aa81f0")),
    row=2, col=1
)
fig.add_trace(
    go.Scatter(x=t_b2, y=ay_b2, name="ay_b2", line=dict(color="#41adf0")),
    row=2, col=1
)
fig.add_trace(
    go.Scatter(x=t_b3, y=ay_b3, name="ay_b3", line=dict(color="#40b892")),
    row=2, col=1
)
fig.add_trace(
    go.Scatter(x=t_g, y=ay_g, name="ay_g", line=dict(color="#f5bad4")),
    row=2, col=1
)

# acceleration in z
fig.add_trace(
    go.Scatter(x=t_b1, y=az_b1, name="az_b1", line=dict(color="#aa81f0")),
    row=3, col=1
)
fig.add_trace(
    go.Scatter(x=t_b2, y=az_b2, name="az_b2", line=dict(color="#41adf0")),
    row=3, col=1
)
fig.add_trace(
    go.Scatter(x=t_b3, y=az_b3, name="az_b3", line=dict(color="#40b892")),
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

#### ------ END PLOTS -------- ####

"""

#### ------ CALCULATE STATS ------- ####

print(good.mean(axis=0))
print(good)
print(bad1.mean(axis=0))
print(bad2.mean(axis=0))
print(bad3.mean(axis=0))
