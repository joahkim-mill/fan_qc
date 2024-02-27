import numpy as np
import pandas as pd 
import torch

good = range(1,68)
bad = range(1,14)
num_bad_noise = 2*len(bad)

numFans = len(good) + len(bad)
X = np.zeros((numFans + num_bad_noise, 8191))  
y = np.zeros((numFans + num_bad_noise,))  #   0 --> bad fan  ,  1 --> good fan

for b in bad:
    filepath = f"./piezo_audacity_data/bad/bad_{b}.txt"
    data = pd.read_csv(filepath, sep='\t')
    if b == 1:
        freq = np.asarray(data["Frequency (Hz)"]).ravel()
        freq = torch.from_numpy(freq).type(torch.float) 
        torch.save(freq, 'frequency.pt')

    db = np.asarray(data["Level (dB)"]).ravel() 
    X[b-1,:] = db  # set each row to be a set of fan dB datapoints across frequecy spectrum
    y[b-1] = 0

for g in range(len(good)):
    filepath = f"./piezo_audacity_data/good/good_{good[g]}.txt"
    data = pd.read_csv(filepath, sep='\t')
    db = np.asarray(data["Level (dB)"]).ravel() 
    X[len(bad) + g, :] = db 
    y[len(bad) + g] = 1

noise_percentage = 0.2
noise_size = int(noise_percentage * 8191) 
random_indices = np.random.choice(8191, noise_size) 

for noise in range(len(bad)):   # first 14 rows are bad fans
    X[numFans + (2*noise), :] = X[noise] + np.random.normal(0, 2, X[noise].shape)  # add gaussian noise
    X[numFans + (2*noise + 1), :] = X[noise] # add noise at random indices
    X[numFans + (2*noise + 1), random_indices] = np.rint(X[numFans + (2*noise + 1), random_indices])  

    y[numFans + (2*noise)] = 0
    y[numFans + (2*noise + 1)] = 0

X = torch.from_numpy(X).type(torch.float)
y = torch.from_numpy(y).type(torch.float) 

torch.save(X, 'X_addNoise_tensor.pt') 
torch.save(y, 'y_addNoise_tensor.pt')



# mean = 
# std_dev = 
# shape = 
# gaussian_noise = np.random.normal(mean, std_dev, shape)