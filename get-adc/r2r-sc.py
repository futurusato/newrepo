import RPi.GPIO as gpio
import r2r_adc as r2r
import time
import matplotlib.pyplot as plt 
adc = r2r.R2R_ADC(dynamic_range, compare_time==0.0001, verbose=False)
voltage_values=[]
time_values=[]
duration = 3.0

try:
    start_time=time.time()
    current_time=time.time()-start_time
