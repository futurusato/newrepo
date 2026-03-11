from matplotlib import pyplot as plt

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
