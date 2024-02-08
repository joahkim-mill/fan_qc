import pandas as pd 
import numpy as np 

## parse through data and if it meets specs, print out pass ! otherwise print out fail message

filename = "good_7" # name of datafile without .csv [time, ax, ay, az]
filepath = f"./accel_data/{filename}.csv"

data = pd.read_csv(filepath)

t = np.asarray(data["time"])
ax = np.asarray(data["x_accel"])
ay = np.asarray(data["y_accel"])
az = np.asarray(data["z_accel"])
a = np.hstack((ax.reshape((-1,1)), ay.reshape((-1,1)), az.reshape((-1,1))))  # [ax , ay, az] columnwise

std_threshold = [0.4, 0.3, 0.4]  ## slightly tight thresholds, so tweak with more data
# calculate some stats using the absolute values, since the symmetry negates some of it
avg = np.mean(np.abs(a), axis=0)
std = np.std(np.abs(a), axis=0)

print("Average of ||accelerations|| : \t a_x", '\t'*3, "a_y", '\t'*3, "a_z")
print('\t'*4, '-'*66)
print('\t'*4, avg[0], '\t', avg[1], '\t', avg[2])
print("Standard Deviation of ||accelerations|| : a_x", '\t'*3, "a_y", '\t'*3, "a_z")
print('\t'*5, '-'*66)
print('\t'*5, std[0], '\t', std[1], '\t', std[2])

# test = np.array([1,0,0])
# print(std_threshold>=test)
# print(np.all(std_threshold>=test))

if (np.all(std_threshold >= std)):
    print("Fan QC Test: PASS !")
else:
    print("Fan QC Test: FAIL :(")


