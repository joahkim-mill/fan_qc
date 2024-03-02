import pandas as pd 
import numpy as np 
from scipy.signal import find_peaks 

# import avg and std_dev from git to evaluate avg + 2*std_dev
model = pd.read_csv("https://raw.githubusercontent.com/joahkim-mill/fan_qc/main/vibration_testing/model")
avg = model["avg"].to_numpy()  # (8191,)
std_dev = model["std dev"].to_numpy()  # (8191,)

actual_good = [1, 4, 6, 7, 8, 10]
label = ["Bad", "Good"]
# read in blind test data 
for test in range(1, 12):
    filepath = f"./piezo_audacity_data/blind_test/{test}.txt"

    # filepath = f"./piezo_audacity_data/bad/bad_16.txt"
    data = pd.read_csv(filepath, sep='\t')
    freq = data["Frequency (Hz)"]
    dB = data["Level (dB)"].to_numpy()  # (8191,)

    # calculate upper threshold -- not too concerned with lower threshold since it shouldn't matter if it's quieter
    std_dev_mult = 2
    cutoff = 100
    threshold = avg + std_dev_mult*std_dev 

    # find peaks 
    peaks, _ = find_peaks(dB)

    # determine crossings
    count = np.sum(dB[peaks] > threshold[peaks])
    buffer = 50
    # print out the result

    print(f"Fan #{test} : {label[test in actual_good]}") 
    print("~~~"*10)
    print(f"\t Counted {count} crossings over the threshold.")

    if count > cutoff: # fail [bad fan] 
        print("\t FAIL : Bad Fan")
    elif count <= cutoff:
        print("\t PASS : Good Fan")

    if (count >= cutoff) and (count - cutoff <= buffer):
        print("\t Borderline : may want to re-check") 
    
    print("\n")

# if count <= cutoff -> pass [good fan]
# if count within cutoff+50, additionally print out that it's borderline / check again ??



