# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the VL53L0X distance sensor.
# Will print the sensed range/distance every second.
from time import time_ns, sleep

import board
import busio

import adafruit_vl53l0x


from udp_client import udpClient

client = udpClient()

# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

# Optionally adjust the measurement timing budget to change speed and accuracy.
# See the example here for more details:
#   https://github.com/pololu/vl53l0x-arduino/blob/master/examples/Single/Single.ino
# For example a higher speed but less accurate timing budget of 20ms:
# vl53.measurement_timing_budget = 20000
# Or a slower but more accurate timing budget of 200ms:
# vl53.measurement_timing_budget = 200000
# The default timing budget is 33ms, a good compromise of speed and accuracy.

# Main loop will read the range and print it every second.
t_old = time_ns()


#for i in range(400):
#    client.udpClientSend(i)
#    sleep(0.05)   

T = 0.08*1e9

min = -1
max = 0
cumsum2 = 0
cumsum = 0
n = 0
while True:
    t_new = time_ns()
    diff = (t_new - t_old)

    
    if diff >= T:
        t_old = t_new
        range_mm = vl53.range
        client.udpClientSend(range_mm)   
        if diff > max:
            max = diff
        if diff < min or min < 0:
            min = diff
            
        n += 1
        cumsum += range_mm**2
        cumsum2 += range_mm
        var = cumsum2/n - cumsum/n
        
        
        print(f"diff={diff/1e9:.3f}, min={min/1e9:.3f}, max={max/1e9:.3f}, var={var/1e9:.3f}, n={n}")
        
    else:
        sleep((T-diff)*0.9e-9)
    #print("Range: {0}mm".format(range_mm))

    