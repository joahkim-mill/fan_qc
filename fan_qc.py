import pandas as pd 
import plotly.graph_objects as go 
from scipy.signal import find_peaks
import streamlit as st

# """
# Once noise recordings from REW have been exported as .txt files, can be read in here and extrapolated for 
# peak frequencies above a specified dB threshold. The peaks and corresponding dB/Hz values will be printed.
# Can optionally plot the data as well.
# """

# dB threshold at which we want to find which frequencies are peaks
# dB_threshold = st.slider("dB Threshold: ", 0, 80, 80)
dB_threshold = st.text_input("dB Threshold: ")
# dB_threshold = 45  

fig = go.Figure()

for i in range(1,11):
    filename = f"Fan {i}"
    
    url = f"https://github.com/joahkim-mill/fan_qc/raw/main/prebaked_delta/Fan%20{i}.txt"
    data = pd.read_csv(url, sep=" ", header=None, skiprows=14, engine='python')
    data.columns = ["Freq(Hz)", "SPL(dB)", "Phase(degrees)"] 

    peaks, _ = find_peaks(data["SPL(dB)"], height=dB_threshold) # find the peaks in the dB

    fig.add_trace(go.Scatter(x=data["Freq(Hz)"], 
                             y=data["SPL(dB)"], 
                             name=f"{filename} Noise Recording",
                             )
                    )
    fig.add_trace(go.Scatter(mode='markers', 
                             x=data["Freq(Hz)"][peaks], 
                             y=data["SPL(dB)"][peaks], 
                             name=f"{filename} Peaks", 
                            #  marker=dict(color='red')
                             )
                    )


for j in range(1,5):
    filename = f"Bad Fan {j}" 

    url = f"https://github.com/joahkim-mill/fan_qc/raw/main/bad_delta/Bad%20Fan%20{j}.txt"
    data = pd.read_csv(url, sep=" " , header=None, skiprows=14, engine='python')
    data.columns = ["Freq(Hz)", "SPL(dB)", "Phase(degrees)"]

    peaks, _ = find_peaks(data["SPL(dB)"], height=dB_threshold) # find the peaks in the dB

    fig.add_trace(go.Scatter(x=data["Freq(Hz)"], 
                             y=data["SPL(dB)"], 
                             name=f"{filename} Noise Recording"
                             )
                    )
    fig.add_trace(go.Scatter(mode='markers', 
                             x=data["Freq(Hz)"][peaks], 
                             y=data["SPL(dB)"][peaks], 
                             name=f"{filename} Peaks", 
                            #  marker=dict(color='red'),
                             )
                    )


fig.update_layout(title="Pre-Baked Delta Fan Noise Recording", 
                  xaxis_title="Frequency Spectrum [Hz]", 
                  yaxis_title="SPL[dB]",
                  height=600,
                  width=800
                  )
fig.update_xaxes(title_font_color="black")
fig.update_yaxes(title_font_color="black")

st.plotly_chart(fig)

# # print out the peak data points
# st.text("        Peaks        ")
# for p in peaks:
#     st.text(f"{data["SPL(dB)"][p]} dB      {data["Freq(Hz)"][p]} Hz \n")

