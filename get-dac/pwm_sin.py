import pwm_dac as pd
import signal_generator as sg
import time
amplitude = 3
signal_frequency=10
sampling_frequency=1000

if __name__=="__main__":
    try:
        dac = pd.PWM_DAC(12,1000,3.3, True)
        start_time=time.time()
        while True:
            current_time=time.time()-start_time
            dac.set_voltage(sg.get_sin_wave_amplitude(signal_frequency, current_time)*amplitude)
            sg.wait_for_sampling_period(sampling_frequency)
    finally:
        dac.deinit()