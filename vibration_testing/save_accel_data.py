import time
import pandas as pd
import board 
import busio 
import adafruit_adxl34x 
import numpy as np 

## make sure to change the name of the file it gets saved to, or it will get overwritten
i2c = board.I2C() 
accelerometer = adafruit_adxl34x.ADXL345(i2c)
# accelerometer.setDataRate(ADXL345_DATARATE_200_HZ)

i=0
tf = 10  # endtime [sec]
# sample_rate = accelerometer.data_rate  # currently 10 [Hz] ? but can be changed
sample_rate = 100
dt = 1/sample_rate
num_samples = (int)(tf * sample_rate)

# initialize list to contain all of the data
accel_data = []  # [time [sec], x_acc, y_acc, z_acc]
t0 = time.time()  # starting time 

for i in range(num_samples):
    # print out accelerations [m/s^2]
    # print(time.time()-t0, "%f %f %f" % accelerometer.acceleration)
    accel_data.append([(time.time() - t0), accelerometer.acceleration[0], accelerometer.acceleration[1], accelerometer.acceleration[2]])
    time.sleep(dt)
   
a=pd.DataFrame(accel_data)
a.columns=["time", "x_accel", "y_accel", "z_accel"]  # time[s], accelerations [m/s^2]
a.to_csv("/home/pi/fan_qc/good_fan_1_accel.csv")
