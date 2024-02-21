import numpy as np
import pandas as pd
import torch
from torch import nn 
from sklearn.model_selection import train_test_split 

# create a model class 
class PiezoModel(nn.Module):
    def __init__(self):
        super().__init__()
        # create nn.Linear layers
        self.layer_1 = nn.Linear(in_features=8191, out_features=8250)  # out_features is set to an arbitrary number rn, finetune later !
        self.layer_2 = nn.Linear(in_features=8250, out_features=1) # takes in the features and outputs 1 (y)
    
    # forward pass computation
    def forward(self, x):
        return self.layer_2(self.layer_1(x))  # layer 1 --> layer 2

"""  # create tensors and save them to be loaded in 
# create numpy array of all the data to be used for testing/training sets
good = [1, 7, 8, 9, 10]
bad = range(1,14)

numFans = len(good) + len(bad)
X = np.zeros((numFans, 8191))  
y = np.zeros((numFans,))  #   0 --> bad fan  ,  1 --> good fan
for b in bad:
    filepath = f"./piezo_audacity_data/bad_{b}.txt"
    data = pd.read_csv(filepath, sep='\t')
    # freq = data["Frequency (Hz)"]
    db = np.asarray(data["Level (dB)"]).ravel() 
    X[b-1,:] = db  # set each row to be a set of fan dB datapoints across frequecy spectrum
    y[b-1] = 0

for g in range(len(good)):
    filepath = f"./piezo_audacity_data/good_{good[g]}.txt"
    data = pd.read_csv(filepath, sep='\t')
    db = np.asarray(data["Level (dB)"]).ravel() 
    X[len(bad) + g, :] = db 
    y[len(bad) + g] = 1

X = torch.from_numpy(X).type(torch.float)
y = torch.from_numpy(y).type(torch.float) 

# torch.save(X, 'X_tensor.pt') 
# torch.save(y, 'y_tensor.pt')

"""
X = torch.load('X_tensor.pt')
y = torch.load('y_tensor.pt')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) #20% test, 80% train
# print(len(X_train), len(X_test), len(y_train), len(y_test))
device = "cuda" if torch.cuda.is_available() else "cpu"

model = PiezoModel().to(device)

untrained_predictions = model(X_test.to(device))
# print(f"Length of predictions: {len(untrained_predictions)}, Shape: {untrained_predictions.shape}")
# print(f"Length of test samples: {len(y_test)}, Shape: {y_test.shape}")



