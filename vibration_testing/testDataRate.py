import time
import pandas as pd
import board 
import busio 
import adafruit_adxl34x 
import numpy as np 
from micropython import const
from collections import deque 

_REG_BW_RATE: int = const(0x2C)  # Data rate and power mode control

RATE_3200_HZ: int = const(0b1111)  # 1600Hz Bandwidth   140mA IDD
RATE_1600_HZ: int = const(0b1110)  # 800Hz Bandwidth    90mA IDD
RATE_800_HZ: int = const(0b1101)  # 400Hz Bandwidth   140mA IDD
RATE_400_HZ: int = const(0b1100)  # 200Hz Bandwidth   140mA IDD
RATE_200_HZ: int = const(0b1011)  # 100Hz Bandwidth   140mA IDD
RATE_100_HZ: int = const(0b1010)  # 50Hz Bandwidth   140mA IDD
RATE_50_HZ: int = const(0b1001)  # 25Hz Bandwidth    90mA IDD
RATE_25_HZ: int = const(0b1000)  # 12.5Hz Bandwidth    60mA IDD
RATE_12_5_HZ: int = const(0b0111)  # 6.25Hz Bandwidth    50mA IDD
RATE_6_25HZ: int = const(0b0110)  # 3.13Hz Bandwidth    45mA IDD
RATE_3_13_HZ: int = const(0b0101)  # 1.56Hz Bandwidth    40mA IDD
RATE_1_56_HZ: int = const(0b0100)  # 0.78Hz Bandwidth    34mA IDD
RATE_0_78_HZ: int = const(0b0011)  # 0.39Hz Bandwidth    23mA IDD
RATE_0_39_HZ: int = const(0b0010)  # 0.20Hz Bandwidth    23mA IDD
RATE_0_20_HZ: int = const(0b0001)  # 0.10Hz Bandwidth    23mA IDD
RATE_0_10_HZ: int = const(0b0000)  # 0.05Hz Bandwidth    23mA IDD (default value)

## make sure to change the name of the file it gets saved to, or it will get overwritten
i2c = board.I2C() 
accelerometer = adafruit_adxl34x.ADXL345(i2c)
# accelerometer.setDataRate(ADXL345_DATARATE_200_HZ)
accelerometer._write_register_byte(_REG_BW_RATE, RATE_100_HZ)  # --> could be irrelevant ? 

i=0
tf = 5  # endtime [sec]

# initialize list to contain all of the data
accel_data = deque()  # [time [sec], x_acc, y_acc, z_acc]
t0 = time.time()  # starting time 

# for i in range(num_samples):
while (time.time() - t0) < tf:
    # print out accelerations [m/s^2]
    # print(time.time()-t0, "%f %f %f" % accelerometer.acceleration)
    accel_data.append([(time.time() - t0), accelerometer.acceleration[0], accelerometer.acceleration[1], accelerometer.acceleration[2]])
   
a=pd.DataFrame(accel_data)
a.columns=["time", "x_accel", "y_accel", "z_accel"]  # time[s], accelerations [m/s^2]
a.to_csv("/home/pi/fan_qc/vibration_testing/test_deque_accel.csv")
