import pandas as pd 
import plotly.graph_objects as go 
from scipy.signal import find_peaks
import streamlit as st

# """
# Once noise recordings from REW have been exported as .txt files, can be read in here and extrapolated for 
# peak frequencies above a specified dB threshold. The peaks and corresponding dB/Hz values will be printed.
# Can optionally plot the data as well.
# """

def visualize_stats():
    st.header("Check the box(es) of the fan data you wish to see")
    check_dict = dict({})
    
    checks = st.columns(3)
    with checks[0]:
        good = st.checkbox('Pre-Baked Fans')
        check_dict["g1"] = st.checkbox('Good 1')
        check_dict["g2"] = st.checkbox('Good 2')
        check_dict["g3"] = st.checkbox('Good 3')
        check_dict["g4"] = st.checkbox('Good 4')
        check_dict["g5"] = st.checkbox('Good 5')
    with checks[1]:
        check_dict["g6"] = st.checkbox('Good 6')
        check_dict["g7"] = st.checkbox('Good 7')
        check_dict["g8"] = st.checkbox('Good 8')
        check_dict["g9"] = st.checkbox('Good 9')
        check_dict["g10"] = st.checkbox('Good 10')
    with checks[2]:
        bad = st.checkbox('Bad Fans')
        check_dict["b1"] = st.checkbox('Bad 1')
        check_dict["b2"] = st.checkbox('Bad 2')
        check_dict["b3"] = st.checkbox('Bad 3')
        check_dict["b4"] = st.checkbox('Bad 4')
        check_dict["b5"] = st.checkbox('Bad 5')

    num_rows = 957

    fig = go.Figure()
    
    # add in good fan stats
    if good:
        good_fans = pd.DataFrame({"good 1":[0]*num_rows}) 

        for i in range(1,11):
            url = f"https://github.com/joahkim-mill/fan_qc/raw/main/prebaked_delta/Fan%20{i}.txt"
            data = pd.read_csv(url, sep=" ", header=None, skiprows=14, engine='python')
            print("read: ", i)
            data.columns = ["Freq(Hz)", "SPL(dB)", "Phase(degrees)"] 
            good_fans[f"good {i}"] = data["SPL(dB)"]
            
        good_fans["avg"] = good_fans.mean(axis=1)
        good_fans["std_dev"] = good_fans.std(axis=1, ddof=0)

        x = data["Freq(Hz)"]
        fig.add_trace(go.Scatter(x=x,
                                y=good_fans["avg"] + good_fans["std_dev"],
                                name="Good Fans +1 Std Dev",
                                fill=None,
                                mode='lines',
                                line=dict(width=0.5, color='rgb(89, 161, 271)'),
                                ))
        fig.add_trace(go.Scatter(x=x,
                                y=good_fans["avg"] - good_fans["std_dev"],
                                name="Good Fans -1 Std Dev",
                                fill='tonexty',
                                mode='lines',
                                line=dict(width=0.5, color='rgb(89, 161, 271)'),
                                ))
        fig.add_trace(go.Scatter(x=x,
                                y=good_fans["avg"],
                                name="Good Fans Avg",
                                line=dict(width=1.25, color='purple')
                                ))
    
    # add in bad fan stats 
    if bad:
        bad_fans = pd.DataFrame({"bad 1":[0]*num_rows})

        for j in range(1,6):
            url = f"https://github.com/joahkim-mill/fan_qc/raw/main/bad_delta/Bad%20Fan%20{j}.txt"
            data = pd.read_csv(url, sep=" " , header=None, skiprows=14, engine='python')
            data.columns = ["Freq(Hz)", "SPL(dB)", "Phase(degrees)"]
            bad_fans[f"bad {j}"] = data["SPL(dB)"]

        bad_fans["avg"] = bad_fans.mean(axis=1)
        bad_fans["std_dev"] = bad_fans.std(axis=1, ddof=0)

        x = data["Freq(Hz)"]
        fig.add_trace(go.Scatter(x=x,
                                y=bad_fans["avg"] + bad_fans["std_dev"],
                                name="Bad Fans +1 Std Dev",
                                fill=None,
                                mode='lines',
                                line=dict(width=0.5, color='rgb(247, 232, 94)'),
                                ))
        fig.add_trace(go.Scatter(x=x,
                                y=bad_fans["avg"] - bad_fans["std_dev"],
                                name="Bad Fans -1 Std Dev",
                                fill='tonexty',
                                mode='lines',
                                line=dict(width=0.5, color='rgb(247, 232, 94)'),
                                ))
        fig.add_trace(go.Scatter(x=x,
                                y=bad_fans["avg"],
                                name="Bad Fans Avg",
                                line=dict(width=1.25, color='green')
                                ))
    
    for g in range(1,11):
        if check_dict[f"g{g}"]:
            fig.add_trace(x=x,
                          ### TO DO : FINISH !! ###
            )

    fig.update_layout(title="Signal Averages & Standard Deviations",
                      xaxis_title="Frequency [Hz]",
                      yaxis_title="SPL [dB]",
                      height=600,
                      width=800
                      )
    st.plotly_chart(fig)
    return 


# dB threshold at which we want to find which frequencies are peaks
# dB_threshold = st.slider("dB Threshold: ", 0, 80, 80)
dB_threshold = st.number_input("dB Threshold: ", value=None, placeholder='Type a number ... ')

fig = go.Figure()

for i in range(1,11):
    filename = f"Fan {i}"
    
    url = f"https://github.com/joahkim-mill/fan_qc/raw/main/prebaked_delta/Fan%20{i}.txt"
    data = pd.read_csv(url, sep=" ", header=None, skiprows=14, engine='python')
    data.columns = ["Freq(Hz)", "SPL(dB)", "Phase(degrees)"] 

    if not (dB_threshold == None) :
        peaks, _ = find_peaks(data["SPL(dB)"], height=dB_threshold) # find the peaks in the dB

        if len(peaks) > 0:  # only attempt to draw peaks if they actually exist
            fig.add_trace(go.Scatter(mode='markers', 
                                    x=data["Freq(Hz)"][peaks], 
                                    y=data["SPL(dB)"][peaks], 
                                    name=f"{filename} Peaks", 
                                    #  marker=dict(color='red')
                                    )
                            )

    fig.add_trace(go.Scatter(x=data["Freq(Hz)"], 
                             y=data["SPL(dB)"], 
                             name=f"{filename} Noise Recording",
                             )
                    )

for j in range(1,6):
    filename = f"Bad Fan {j}" 

    url = f"https://github.com/joahkim-mill/fan_qc/raw/main/bad_delta/Bad%20Fan%20{j}.txt"
    data = pd.read_csv(url, sep=" " , header=None, skiprows=14, engine='python')
    data.columns = ["Freq(Hz)", "SPL(dB)", "Phase(degrees)"]

    if not (dB_threshold == None):
        peaks, _ = find_peaks(data["SPL(dB)"], height=dB_threshold) # find the peaks in the dB
        
        if len(peaks) > 0:  # only attempt to draw peaks if they actually exist
            fig.add_trace(go.Scatter(mode='markers', 
                                    x=data["Freq(Hz)"][peaks], 
                                    y=data["SPL(dB)"][peaks], 
                                    name=f"{filename} Peaks", 
                                    #  marker=dict(color='red'),
                                    )
                            )

    fig.add_trace(go.Scatter(x=data["Freq(Hz)"], 
                             y=data["SPL(dB)"], 
                             name=f"{filename} Noise Recording"
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

visualize_stats()


# # print out the peak data points
# st.text("        Peaks        ")
# for p in peaks:
#     st.text(f"{data["SPL(dB)"][p]} dB      {data["Freq(Hz)"][p]} Hz \n")

