from matplotlib import pyplot as plt
import RPi.GPIO as GPIO
import time
import r2r_adc as r2r
def plot_sampling_period_hist(t):
    sampling_periods=[t[i+1]-t[i] for i in range(len(t)-1)]
    plt.figure(figsize=(10,6))
    plt.hist(sampling_periods)
    plt.title("Гистограмма периодов дискретизации")
    plt.xlabel("Интервал времени")
    plt.ylabel("Количество измерений")
    plt.grid(True)
    plt.xlim(0,0.06)
    plt.show()
def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title("График зависимости напряжения от времени")
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.grid(True)
    plt.show()
voltage_values=[]
time_values=[]
duration=3.0
try:
    dac = r2r.R2R_ADC(3.285,0.000001)
    start=time.time()
    while (time.time()-start)<duration:
        c=time.time()-start
        vol=dac.get_sc_voltage()
        voltage_values.append(vol)
        time_values.append(c)
    plot_voltage_vs_time(time_values, voltage_values, 3.285)
    plot_sampling_period_hist(time_values)
finally:
        dac.deinit()
