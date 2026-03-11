import r2r_adc as r2r
import adc_plot as graph
import time

adc = r2r.R2R_ADC(3.285,0.0001)
time_values=[]
voltage_values=[]
duration = 3.0

try:
    start=time.time()
    while (time.time()-start)<duration:
        c=time.time()-start
        vol=adc.get_sc_voltage()
        voltage_values.append(vol)
        time_values.append(c)
    graph.plot_voltage_vs_time(time_values, voltage_values, 3.285)
    graph.plot_sampling_period_hist(time_values)
finally:
        adc.deinit()

