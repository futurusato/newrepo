import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency=10
sampling_frequency=1000

try:
    dac = r2r.R2R_DAC([16,20,21,25,26,17,27,22],3.183, True)

    t=0
    sampling_period=1.0/sampling_frequency
    
    while True:
    
        try:
            normalized_amp=sg.get_sin_wave_amplitude(signal_frequency, t)
            output_voltage=normalized_amp*amplitude
            dac_value=int((output_voltage/3.3)*255)
            dac_value=max(0,min(255,dac_value))
            dac.set_output(dac_value)
            sg.wait_for_sampling_period(sampling_frequency)
            t+=sampling_period
        except KeyboardInterrupt:
            break
finally:
    if dac is not None:
        dac.deinit()