import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import streamlit as st
from scipy.signal import find_peaks, find_peaks_cwt
import torch 

# good = range(1,10)
# bad = range(1,14) 
# good = [1]
# bad = [1]


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
#     filepath = f"./piezo_audacity_data/good/good_{g}.txt"
#     good_data = pd.read_csv(filepath, sep='\t')
#     freq = good_data["Frequency (Hz)"]
#     db = good_data["Level (dB)"]
#     fig.add_trace(go.Scatter(x=freq, y=db, name=f"Good {g}", line=dict(width=1.25)))
# for b in bad:
#     filepath = f"./piezo_audacity_data/bad/bad_{b}.txt"
#     bad_data = pd.read_csv(filepath, sep='\t')
#     freq = bad_data["Frequency (Hz)"]
#     db = bad_data["Level (dB)"]
#     fig.add_trace(go.Scatter(x=freq, y=db, name=f"Bad {b}", line=dict(width=1.25)))
# fig.update_layout(title="Fan Frequency Spectrum", height=800, width=900,
#                   xaxis_title="Frequency [Hz]", yaxis_title="Level [dB]")
# st.plotly_chart(fig)
# #endregion


# #region find peaks of signals
# fig = go.Figure()
# db_good= np.zeros((8191,))  # each row will contain level[dB] data across frequencies
# db_bad = np.zeros((8191,))


# good_peaks_df = pd.DataFrame(index=range(14))  # change these index ranges depending on how many peaks are found !!
# bad_peaks_df = pd.DataFrame(index=range(15))
# for g in good:
#     filepath = f"./piezo_audacity_data/good_{g}.txt"
#     good_data = pd.read_csv(filepath, sep='\t')
#     freq = good_data["Frequency (Hz)"]
#     db = np.asarray(good_data["Level (dB)"]).ravel() 
#     db_good = np.vstack((db_good, db)) # adding on rows to the array of data
#     fig.add_trace(go.Scatter(x=freq, y=db, name=f"good {g}", line=dict(width=1)))
#     # peaks, _ = find_peaks(db, rel_height=10)
#     peaks = find_peaks_cwt(db, widths=range(60, 200))
#     # print(f"good peaks num: {peaks.shape}")
    
#     good_peaks_df[f"good {g}"] = freq[peaks].reset_index(drop=True)
#     fig.add_trace(go.Scatter(x=freq[peaks], y=db[peaks], name=f"good {g} peaks", mode='markers'))
# for b in bad:
#     filepath = f"./piezo_audacity_data/bad_{b}.txt"
#     bad_data = pd.read_csv(filepath, sep='\t')
#     freq = bad_data["Frequency (Hz)"]
#     db = np.asarray(bad_data["Level (dB)"]).ravel()
#     db_bad = np.vstack((db_bad, db)) # adding on rows to the array of data
#     fig.add_trace(go.Scatter(x=freq, y=db, name=f"bad {b}", line=dict(width=1)))
#     # peaks, _ = find_peaks(db, rel_height=10)
#     peaks = find_peaks_cwt(db, widths=range(60,200))
#     # print(f"bad peaks num: {peaks.shape}")
  
#     bad_peaks_df[f"bad {b}"] = freq[peaks].reset_index(drop=True)
#     fig.add_trace(go.Scatter(x=freq[peaks], y=db[peaks], name=f"bad {b} peaks", mode='markers'))

# # get rid of row of zeros
# db_good = db_good[1:,:]
# db_bad = db_bad[1:,:]

# # avg_db_good = np.mean(db_good, axis=0)
# # avg_db_bad = np.mean(db_bad, axis=0)

# # sum_db_good = np.sum(db_good, axis=0)
# # sum_db_bad = np.sum(db_bad, axis=0)

# # fig.add_trace(go.Scatter(x=freq, y=avg_db_good, name="Average Good"))
# # fig.add_trace(go.Scatter(x=freq, y=sum_db_good, name="Sum Good"))

# # fig.add_trace(go.Scatter(x=freq, y=avg_db_bad, name="Average Bad"))
# # fig.add_trace(go.Scatter(x=freq, y=sum_db_bad, name="Sum Bad"))

# fig.update_layout(title="Peaks of the Signals", height=800, width=900,
#                   xaxis_title="Frequency [Hz]", yaxis_title="Level [dB]")
# st.plotly_chart(fig)


# # st.dataframe(good_peaks_df, column_config=dict(width="medium"))
# # st.dataframe(bad_peaks_df, column_config=dict(width="medium"))


# st.data_editor(
#     good_peaks_df,
#     column_config={
#         "widgets": st.column_config.Column(
#             width="medium",
#             disabled=True
#         )
#     },
#     # hide_index=True,
#     # num_rows="dynamic",
# )

# st.data_editor(
#     bad_peaks_df,
#     column_config={
#         "widgets": st.column_config.Column(
#             width="medium",
#             disabled=True
#         )
#     },
#     # hide_index=True,
#     # num_rows="dynamic",
# )

# #endregion find peaks of signals

# # plot good peaks to get a visual sense of which ones are common
# fig_peaks = go.Figure()
# for p in good_peaks_df:
#     # print(p)
#     fig_peaks.add_trace(go.Scatter(x=good_peaks_df[p], y=[0]*len(good_peaks_df[p]), name=p, 
#                                    mode='markers', marker=dict(size=10)))
# fig_peaks.update_layout(title="Peak Comparison of Good Fans", height=500, width=900)
# st.plotly_chart(fig_peaks)


#region compute average of good fans
X = torch.load('X_tensor.pt')  
X = X.numpy()
freq = torch.load('frequency.pt')
freq = freq.numpy()
bad = X[:13, :]
good = X[13:,:]

avg = np.mean(good, axis=0)
std = np.std(good, axis=0)
fig = go.Figure()

# std_dev_mult = 1.5
std_dev_mult = st.number_input("Input a Standard Deviation Multiplier")
std_dev = np.concatenate([(avg+ std_dev_mult*std), (avg- std_dev_mult*std)[::-1]])

out_b= np.zeros((13,))
out_g = np.zeros((67,))

fig.add_trace(go.Scatter(x=np.concatenate([freq, freq[::-1]]), y=std_dev, name=f"Avg +/- {std_dev_mult} Std Dev", 
                         fill='toself',
                         line=dict(width=0.5, color='#fad7f1'),
                         ))
fig.add_trace(go.Scatter(x=freq, y=avg, name='average good fan',
                         line=dict(width=0.75, color='#bc37ed')))

count = 0
for b in bad:
    out_b[count] = (int)(np.sum(b > (avg + std_dev_mult*std)))
    # if count ==0:
    #     st.table(b>(avg+std))
    count += 1

    fig.add_trace(go.Scatter(x=freq, y=b, name=f"bad fan {count}",
                             line=dict(width=0.5)))
    

count = 0
for g in good: 
    out_g[count] = (int)(np.sum(g > (avg + std_dev_mult*std)))
    count += 1
    fig.add_trace(go.Scatter(x=freq, y=g, name=f"good fan {count}",
                             line=dict(width=0.5)))
  
fig.update_layout(title='average fans', xaxis_title='Frequency(Hz)', yaxis_title='dB',
                  width=900, height=600)

st.plotly_chart(fig)
col = st.columns(2)
with col[0]:
    st.header("bad fan outlier count:")
    st.table(out_b)
    # st.dataframe(out_b)
with col[1]:
    st.header("good fan outlier count:")
    st.table(out_g)
    # st.dataframe(out_g)


#endregion