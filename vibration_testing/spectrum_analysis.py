import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import streamlit as st
from scipy.signal import find_peaks, find_peaks_cwt
import torch 


#region compute average of good fans
X = torch.load('spring_good.pt')  
good = X.numpy()
freq = torch.load('frequency.pt')
freq = freq.numpy()

avg = np.mean(good, axis=0)
std = np.std(good, axis=0)

# # create dataframe to save the stats
# df = pd.DataFrame()
# df["avg"] = avg 
# df["std dev"] = std

# df.to_csv("model")

# #region streamlit plotting
# fig = go.Figure()

# # # std_dev_mult = 1.5
# std_dev_mult = st.number_input("Input a Standard Deviation Multiplier")
# std_dev = np.concatenate([(avg+ std_dev_mult*std), (avg- std_dev_mult*std)[::-1]])

# out_b= np.zeros((bad.shape[0],))
# out_g = np.zeros((good.shape[0],))

# fig.add_trace(go.Scatter(x=np.concatenate([freq, freq[::-1]]), y=std_dev, name=f"Avg +/- {std_dev_mult} Std Dev", 
#                          fill='toself',
#                          line=dict(width=0.5, color='#fad7f1'),
#                          ))
# fig.add_trace(go.Scatter(x=freq, y=avg, name='average good fan',
#                          line=dict(width=0.75, color='#bc37ed')))

# check_peak = st.checkbox('Use Peaks')
# #endregion streamlit plotting

# #region inspect the good redo recordings
# # since this comes after finding the average and standard deviation of the original dataset, we can see how the re-recorded fans do 
# redo = [10, 22, 24, 27, 37, 52, 64, 65, 7, 47, 49, 51, 14, 48, 53, 61]

# for r in redo: # starts from 0, so fan 1 is good[0] and so on
#     filepath = f"./piezo_audacity_data/good/good_{r}_redo.txt"
#     data = pd.read_csv(filepath, sep='\t')
#     db = np.asarray(data["Level (dB)"]).ravel() 
#     # replace original good data with the redo 
#     good[r - 1] = db

# redo_bad = [8, 11, 12, 13, 15]

# for rb in redo_bad:
#     filepath = f"./piezo_audacity_data/bad/bad_{rb}_redo.txt"
#     data = pd.read_csv(filepath, sep='\t')
#     db = np.asarray(data["Level (dB)"]).ravel()
#     bad[rb - 1] = db
# #endregion inspect the good redo recordings
    
# #region find the crossings of avg +/- ()*std dev
# count = 0
# for b in bad:
#     if check_peak:
#         # using peaks instead of raw data points 
#         peaks, _ = find_peaks(b)
#         out_b[count] = (int)(np.sum((b > (avg + std_dev_mult*std))[peaks]))
#     else:
#         # using raw data points
#         out_b[count] = (int)(np.sum(b > (avg + std_dev_mult*std)))
    
#     count += 1

#     fig.add_trace(go.Scatter(x=freq, y=b, name=f"bad fan {count}",
#                              line=dict(width=0.5)))
    
# count = 0
# for g in good: 
#     if check_peak:
#         # using peaks instead of raw data points
#         peaks, _ = find_peaks(g)
#         out_g[count] = (int)(np.sum((g > (avg + std_dev_mult*std))[peaks]))

#     else:
#         # using raw data points
#         out_g[count] = (int)(np.sum(g > (avg + std_dev_mult*std)))

#     count += 1
    
#     fig.add_trace(go.Scatter(x=freq, y=g, name=f"good fan {count}",
#                              line=dict(width=0.5)))

# if check_peak:
#     fig.update_layout(title='fans with the avg / std dev using peaks', xaxis_title='Frequency(Hz)', yaxis_title='dB',
#                   width=1000, height=700)
# else:
#     fig.update_layout(title='fans with the avg / std dev', xaxis_title='Frequency(Hz)', yaxis_title='dB',
#                   width=1000, height=700)
    
# st.plotly_chart(fig)

# col = st.columns(2)
# with col[0]:
#     st.header("bad fan outlier count:")
#     st.table(out_b)

# with col[1]:
#     st.header("good fan outlier count:")
#     st.table(out_g)

# #endregion
    




""" USING ORIGINAL DATA WITHOUT SPRINGS

#region compute average of good fans
X = torch.load('X_tensor.pt')  
X = X.numpy()
freq = torch.load('frequency.pt')
freq = freq.numpy()
numBadFans = 16
bad = X[:numBadFans, :] #rows 0-15
good = X[numBadFans:,:] #rows 15-82

avg = np.mean(good, axis=0)
std = np.std(good, axis=0)

# # create dataframe to save the stats
# df = pd.DataFrame()
# df["avg"] = avg 
# df["std dev"] = std

# df.to_csv("model")

# #region streamlit plotting
# fig = go.Figure()

# # # std_dev_mult = 1.5
# std_dev_mult = st.number_input("Input a Standard Deviation Multiplier")
# std_dev = np.concatenate([(avg+ std_dev_mult*std), (avg- std_dev_mult*std)[::-1]])

# out_b= np.zeros((bad.shape[0],))
# out_g = np.zeros((good.shape[0],))

# fig.add_trace(go.Scatter(x=np.concatenate([freq, freq[::-1]]), y=std_dev, name=f"Avg +/- {std_dev_mult} Std Dev", 
#                          fill='toself',
#                          line=dict(width=0.5, color='#fad7f1'),
#                          ))
# fig.add_trace(go.Scatter(x=freq, y=avg, name='average good fan',
#                          line=dict(width=0.75, color='#bc37ed')))

# check_peak = st.checkbox('Use Peaks')
# #endregion streamlit plotting

# #region inspect the good redo recordings
# # since this comes after finding the average and standard deviation of the original dataset, we can see how the re-recorded fans do 
# redo = [10, 22, 24, 27, 37, 52, 64, 65, 7, 47, 49, 51, 14, 48, 53, 61]

# for r in redo: # starts from 0, so fan 1 is good[0] and so on
#     filepath = f"./piezo_audacity_data/good/good_{r}_redo.txt"
#     data = pd.read_csv(filepath, sep='\t')
#     db = np.asarray(data["Level (dB)"]).ravel() 
#     # replace original good data with the redo 
#     good[r - 1] = db

# redo_bad = [8, 11, 12, 13, 15]

# for rb in redo_bad:
#     filepath = f"./piezo_audacity_data/bad/bad_{rb}_redo.txt"
#     data = pd.read_csv(filepath, sep='\t')
#     db = np.asarray(data["Level (dB)"]).ravel()
#     bad[rb - 1] = db
# #endregion inspect the good redo recordings
    
# #region find the crossings of avg +/- ()*std dev
# count = 0
# for b in bad:
#     if check_peak:
#         # using peaks instead of raw data points 
#         peaks, _ = find_peaks(b)
#         out_b[count] = (int)(np.sum((b > (avg + std_dev_mult*std))[peaks]))
#     else:
#         # using raw data points
#         out_b[count] = (int)(np.sum(b > (avg + std_dev_mult*std)))
    
#     count += 1

#     fig.add_trace(go.Scatter(x=freq, y=b, name=f"bad fan {count}",
#                              line=dict(width=0.5)))
    
# count = 0
# for g in good: 
#     if check_peak:
#         # using peaks instead of raw data points
#         peaks, _ = find_peaks(g)
#         out_g[count] = (int)(np.sum((g > (avg + std_dev_mult*std))[peaks]))

#     else:
#         # using raw data points
#         out_g[count] = (int)(np.sum(g > (avg + std_dev_mult*std)))

#     count += 1
    
#     fig.add_trace(go.Scatter(x=freq, y=g, name=f"good fan {count}",
#                              line=dict(width=0.5)))

# if check_peak:
#     fig.update_layout(title='fans with the avg / std dev using peaks', xaxis_title='Frequency(Hz)', yaxis_title='dB',
#                   width=1000, height=700)
# else:
#     fig.update_layout(title='fans with the avg / std dev', xaxis_title='Frequency(Hz)', yaxis_title='dB',
#                   width=1000, height=700)
    
# st.plotly_chart(fig)

# col = st.columns(2)
# with col[0]:
#     st.header("bad fan outlier count:")
#     st.table(out_b)

# with col[1]:
#     st.header("good fan outlier count:")
#     st.table(out_g)

# #endregion
    

"""