from matplotlib import pyplot as plt
import time
import mcp3021_driver as mcp
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
duration = 3.0
try:
    acd=mcp.MCP3021(3.285)
    start=time.time()
    while (time.time()-start)<duration:
        c=time.time()-start
        vol=acd.get_voltage()
        voltage_values.append(vol)
        time_values.append(c)
    plot_voltage_vs_time(time_values, voltage_values, 3.285)
    plot_sampling_period_hist(time_values)
finally:
    acd.deinit()

