import pandas as pd 
import numpy as np 
from plotly import graph_objects as go 
from plotly.subplots import make_subplots
from scipy.signal import find_peaks 


#region -- good fan data
#### --------- GOOD FAN DATA --------- ####
# -- GOOD 7 -- #
# read in csv to access data 
good7 = pd.read_csv("./accel_data/good_7.csv")

# make them into columns
t_g7 = np.asarray(good7["time"])
ax_g7 = np.asarray(good7["x_accel"])
ay_g7 = np.asarray(good7["y_accel"])
az_g7 = np.asarray(good7["z_accel"])
a_g7 = np.hstack((ax_g7.reshape((-1,1)), ay_g7.reshape((-1,1)), az_g7.reshape((-1,1))))

# -- GOOD 8 -- #
# read in csv to access data 
good8 = pd.read_csv("./accel_data/good_8.csv")

# make them into columns
t_g8 = np.asarray(good8["time"])
ax_g8 = np.asarray(good8["x_accel"])
ay_g8 = np.asarray(good8["y_accel"])
az_g8 = np.asarray(good8["z_accel"])
a_g8 = np.hstack((ax_g8.reshape((-1,1)), ay_g8.reshape((-1,1)), az_g8.reshape((-1,1))))

# -- GOOD 9 -- #
# read in csv to access data 
good9 = pd.read_csv("./accel_data/good_9.csv")

# make them into columns
t_g9 = np.asarray(good9["time"])
ax_g9 = np.asarray(good9["x_accel"])
ay_g9 = np.asarray(good9["y_accel"])
az_g9 = np.asarray(good9["z_accel"])
a_g9 = np.hstack((ax_g9.reshape((-1,1)), ay_g9.reshape((-1,1)), az_g9.reshape((-1,1))))

# -- GOOD 10 -- #
# read in csv to access data 
good10= pd.read_csv("./accel_data/good_10.csv")

# make them into columns
t_g10 = np.asarray(good10["time"])
ax_g10 = np.asarray(good10["x_accel"])
ay_g10 = np.asarray(good10["y_accel"])
az_g10 = np.asarray(good10["z_accel"])
a_g10 = np.hstack((ax_g10.reshape((-1,1)), ay_g10.reshape((-1,1)), az_g10.reshape((-1,1))))

#endregion -- good fan data

#region -- bad fan data
#### --------- BAD FAN DATA --------- ####
# -- BAD 1 -- #
bad1 = pd.read_csv("./accel_data/bad_1.csv")

# make them into columns
t_b1 = np.asarray(bad1["time"])
ax_b1 = np.asarray(bad1["x_accel"])
ay_b1 = np.asarray(bad1["y_accel"])
az_b1 = np.asarray(bad1["z_accel"])
a_b1 = np.hstack((ax_b1.reshape((-1,1)), ay_b1.reshape((-1,1)), az_b1.reshape((-1,1))))

# -- BAD 2 -- #
bad2 = pd.read_csv("./accel_data/bad_2.csv")

# make them into columns
t_b2 = np.asarray(bad2["time"])
ax_b2 = np.asarray(bad2["x_accel"])
ay_b2 = np.asarray(bad2["y_accel"])
az_b2 = np.asarray(bad2["z_accel"])
a_b2 = np.hstack((ax_b2.reshape((-1,1)), ay_b2.reshape((-1,1)), az_b2.reshape((-1,1))))

# -- BAD 3 -- #
bad3 = pd.read_csv("./accel_data/bad_3.csv")

# make them into columns
t_b3 = np.asarray(bad3["time"])
ax_b3 = np.asarray(bad3["x_accel"])
ay_b3 = np.asarray(bad3["y_accel"])
az_b3 = np.asarray(bad3["z_accel"])
a_b3 = np.hstack((ax_b3.reshape((-1,1)), ay_b3.reshape((-1,1)), az_b3.reshape((-1,1))))

#endregion -- bad fan data

data_g = [a_g7, a_g8, a_g9]  ## NOTE : exluding good fan 10 bc it's not actually that good --> i think it should be labeled bad
data_b = [a_b1, a_b2, a_b3] 

""" #region -- plots
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

""" #endregion -- plots

#region -- calc stats

#### ------ CALCULATE STATS ------- ####

# 1. take averages of raw data : means are all pretty similar ---> std dev may be promising ? 
# print("good fans")
# for g in data_g:
#     print(f"avg : ", np.mean(g, axis=0))
#     print(f"std dev : ", np.std(g, axis=0))

# print("bad fans")
# for b in data_b:
#     print(f"avg : ", np.mean(b, axis=0))
#     print(f"std dev : ", np.std(b, axis=0))


# 2. max [absolute] amplitude --> doens't seem relevant ... except the y accel for bad fans are pretty bad
# print("good fans")
# for g in data_g:
#     # absolute = np.abs(g)
#     print("max amplitude : ", np.amax(g, axis=0))

# print("bad fans")
# for b in data_b:
#     # absolute = np.abs(b)
#     print("max amplitude : ", np.amax(b, axis=0))

 
# 3. use find peaks ?? FINISH HERE !
fig = go.Figure()
t_g = [t_g7, t_g8, t_g9]
t_b = [t_b1, t_b2, t_b3]
for i in range(3):
    peaks, _ = find_peaks(data_g[i])
    fig.add_trace(x=t_g[i], y=data_g[i])
    fig.add_trace(go.Scatter(x=t_g[i][peaks], y=data_g[i][peaks], mode='markers'))

# 4.  maybe determine at what theshold the amplitude hits a percentile ?


#endregion -- calc stats