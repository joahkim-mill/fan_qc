import pandas as pd 
import plotly.graph_objects as go 
# from scipy.signal import find_peaks
import streamlit as st

fig = go.Figure()

pre_files = ["bad_delta/Bad Fan 4.txt", "bad_delta/Bad Fan 5.txt", "prebaked_/Fan 1.txt"]
post_files = ["post_oven/Bad Fan 4 -- Post-Oven.txt", "post_oven/Bad Fan 5 -- Post-Oven.txt", "post_oven/Good Fan 1 -- Post-Oven.txt"]

# print(pre_files[0])
# print(pre_files[0][10:-4])
pre_color = ['royalblue', 'green', 'salmon']
post_color = ['skyblue', 'lawngreen', 'peachpuff']
for f in range(3):
    
    pre = pd.read_csv(pre_files[f], sep=" ", header=None, skiprows=14, engine="python")
    pre.columns = ["Freq(Hz)", "SPL(dB)", "Phase(degrees)"]

    post = pd.read_csv(post_files[f], sep=" " , header=None, skiprows=14, engine='python')
    post.columns = ["Freq(Hz)", "SPL(dB)", "Phase(degrees)"]


    fig.add_trace(go.Scatter(x=pre["Freq(Hz)"],
                             y=pre["SPL(dB)"],
                             name=pre_files[f][10:-4],
                             mode='lines',
                             line=dict(shape='linear', width=2, color=pre_color[f])
                             ))

    fig.add_trace(go.Scatter(x=post["Freq(Hz)"],
                             y=post["SPL(dB)"],
                             mode="lines+markers",
                             line=dict(shape='linear', dash='dashdot',width=2, color=post_color[f]),
                             marker = dict(size=3,),
                             name=post_files[f][10:-4]
                             ))
    
fig.update_layout(title="Comparison of Fans Pre and Post Running in Oven",
                  xaxis_title="Frequency [Hz]",
                  yaxis_title="SPL [dB]",
                  height=650,
                  width=950,
                  )
    
st.plotly_chart(fig)