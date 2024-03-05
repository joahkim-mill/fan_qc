import numpy as np
import pandas as pd
import torch

#region create tensor of good fan data and save it to be loaded in 
# create numpy array of all the good fan data to be used 
good = list(range(1,67))
good.pop(61) # don't have data for fan 62

# print(good)

numFans = len(good)
spring_good = np.zeros((numFans, 8191))  

# for b in bad:
#     filepath = f"./piezo_audacity_data/bad/bad_{b}.txt"
#     data = pd.read_csv(filepath, sep='\t')
#     # freq = data["Frequency (Hz)"]
#     db = np.asarray(data["Level (dB)"]).ravel() 
#     X[b-1,:] = db  # set each row to be a set of fan dB datapoints across frequecy spectrum
#     y[b-1] = 0
count = 0
for g in good:
    filepath = f"./piezo_audacity_data/spring_good/{g}.txt"
    data = pd.read_csv(filepath, sep='\t')
    db = np.asarray(data["Level (dB)"]).ravel() 
    spring_good[count, :] = db 

spring_good = torch.from_numpy(spring_good).type(torch.float)
# y = torch.from_numpy(y).type(torch.float) 

torch.save(spring_good, 'spring_good.pt') 
# torch.save(y, 'y_tensor.pt')

#endregion create tensors



# #region create tensors and save them to be loaded in 
# # create numpy array of all the data to be used for testing/training sets
# good = range(1,68)
# bad = range(1,17)

# numFans = len(good) + len(bad)
# X = np.zeros((numFans, 8191))  
# y = np.zeros((numFans,))  #   0 --> bad fan  ,  1 --> good fan
# for b in bad:
#     filepath = f"./piezo_audacity_data/bad/bad_{b}.txt"
#     data = pd.read_csv(filepath, sep='\t')
#     # freq = data["Frequency (Hz)"]
#     db = np.asarray(data["Level (dB)"]).ravel() 
#     X[b-1,:] = db  # set each row to be a set of fan dB datapoints across frequecy spectrum
#     y[b-1] = 0

# for g in range(len(good)):
#     filepath = f"./piezo_audacity_data/good/good_{good[g]}.txt"
#     data = pd.read_csv(filepath, sep='\t')
#     db = np.asarray(data["Level (dB)"]).ravel() 
#     X[len(bad) + g, :] = db 
#     y[len(bad) + g] = 1

# X = torch.from_numpy(X).type(torch.float)
# y = torch.from_numpy(y).type(torch.float) 

# torch.save(X, 'X_tensor.pt') 
# torch.save(y, 'y_tensor.pt')

# #endregion create tensors

