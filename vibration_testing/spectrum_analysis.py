import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import streamlit as st

good = [1, 7, 8, 9, 10]
bad = range(1,14) 


# #region plotting good and bad on separate subplots
# fig = make_subplots(rows=2, cols=1, vertical_spacing=0.2)
# for g in good:
#     filepath = f"./piezo_audacity_data/good_{g}.txt"
#     good_data = pd.read_csv(filepath, sep='\t')
#     print(good_data)
#     freq = good_data["Frequency (Hz)"]
#     db = good_data["Level (dB)"]
#     fig.add_trace(go.Scatter(x=freq, y=db, name=f"Good {g}", 
#                             #  legendgroup='1'
#                              ), 
#                              row=1, col=1)

# for b in bad:
#     filepath = f"./piezo_audacity_data/bad_{b}.txt"
#     bad_data = pd.read_csv(filepath, sep='\t')

#     freq = bad_data["Frequency (Hz)"]
#     db = bad_data["Level (dB)"]
#     fig.add_trace(go.Scatter(x=freq, y=db, name=f"Bad {b}", 
#                             #  legendgroup='2'
#                              ), 
#                              row=2, col=1)

# fig.update_layout(title="Fan Spectrum Visualization", height=800, width=900,
#                   xaxis1_title="Frequency [Hz]", yaxis1_title="Level [dB]",
#                   xaxis2_title="Frequency [Hz]", yaxis2_title="Level [dB]",
#                 #   legend_tracegroupgap=250
#                   )

# st.plotly_chart(fig)
# #endregion subplots

# #region plotting all together on one plot
# fig = go.Figure()
# for g in good:
#     filepath = f"./piezo_audacity_data/good_{g}.txt"
#     good_data = pd.read_csv(filepath, sep='\t')
#     freq = good_data["Frequency (Hz)"]
#     db = good_data["Level (dB)"]
#     fig.add_trace(go.Scatter(x=freq, y=db, name=f"Good {g}", line=dict(width=1.25)))
# for b in bad:
#     filepath = f"./piezo_audacity_data/bad_{b}.txt"
#     bad_data = pd.read_csv(filepath, sep='\t')
#     freq = bad_data["Frequency (Hz)"]
#     db = bad_data["Level (dB)"]
#     fig.add_trace(go.Scatter(x=freq, y=db, name=f"Bad {b}", line=dict(width=1.25)))
# fig.update_layout(title="Fan Frequency Spectrum", height=800, width=900,
#                   xaxis_title="Frequency [Hz]", yaxis_title="Level [dB]")
# st.plotly_chart(fig)
# #endregion

#region take average of signals
fig = go.Figure()
db_good= np.zeros((8191,))  # each row will contain level[dB] data across frequencies
db_bad = np.zeros((8191,))

for g in good:
    filepath = f"./piezo_audacity_data/good_{g}.txt"
    good_data = pd.read_csv(filepath, sep='\t')
    freq = good_data["Frequency (Hz)"]
    db = np.asarray(good_data["Level (dB)"]).ravel()
    db_good = np.vstack((db_good, db)) # adding on rows to the array of data
    fig.add_trace(go.Scatter(x=freq, y=db, name=f"good {g}", line=dict(width=1)))
for b in bad:
    filepath = f"./piezo_audacity_data/bad_{b}.txt"
    bad_data = pd.read_csv(filepath, sep='\t')
    freq = bad_data["Frequency (Hz)"]
    db = np.asarray(bad_data["Level (dB)"]).ravel()
    db_bad = np.vstack((db_bad, db)) # adding on rows to the array of data
    fig.add_trace(go.Scatter(x=freq, y=db, name=f"bad {b}", line=dict(width=1)))

# get rid of row of zeros
db_good = db_good[1:,:]
db_bad = db_bad[1:,:]

# freq = bad_data["Frequency (Hz)"]
avg_db_good = np.mean(db_good, axis=0)
avg_db_bad = np.mean(db_bad, axis=0)

# sum_db_good = np.sum(db_good, axis=0)
# sum_db_bad = np.sum(db_bad, axis=0)

fig.add_trace(go.Scatter(x=freq, y=avg_db_good, name="Average Good"))
# fig.add_trace(go.Scatter(x=freq, y=sum_db_good, name="Sum Good"))

fig.add_trace(go.Scatter(x=freq, y=avg_db_bad, name="Average Bad"))
# fig.add_trace(go.Scatter(x=freq, y=sum_db_bad, name="Sum Bad"))

fig.update_layout(title="Average of the Signals", height=700, width=850,
                  xaxis_title="Frequency [Hz]", yaxis_title="Level [dB]")
st.plotly_chart(fig)
#endregion take average of signals