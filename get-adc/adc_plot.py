import matplotlib.pyplot as plt 
def plot_voltage_vs_time(time, voltage, max_voltage):
     plt.figure(figsize=(10,6))
     plt.plot(time,voltage)
     plt.title("График зависимости напряжения оа входе АЦП от времени")
     plt.ylabel("Напряжение, В")
     plt.xlabel("Время, с")
     plt.grid()
     plt.show()
def plot_sampling_period_hist(time):
    sampling_periods=[]
    plt.figure(figsize==(10,6))
    plt.hist(sampling_periods)
    plt.title("Распределение периодов дискретизации измерений по времени на одно измерение")
    plt.ylabel("Количество измерений")
    plt.xlabel("Период измерения, с")
    plt.xlin(0,0.86)
    plt.show()