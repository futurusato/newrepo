import time
import adc_plot as graph
import r2r_adc

adc = r2r_adc.R2R_ADC(3.285,0.000001)

voltage_values=[]
time_values=[]
duration = 3.0

try:
    start=time.time()
    while (time.time()-start)<duration:
        c=time.time()-start
        vol=adc.get_sar_voltage()
        voltage_values.append(vol)
        time_values.append(c)
    graph.plot_voltage_vs_time(time_values, voltage_values, 3.285)
    graph.plot_sampling_period_hist(time_values)

finally:
        adc.deinit()
