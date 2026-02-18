import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
outp=[16,20,21,25,26,17,27,22]
GPIO.setup(outp,GPIO.OUT)
dyn_range=float(input())
def voltage_to_nomber(voltage):
    if not (0.0<=voltage<=dyn_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00- {dyn_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0

    return int(voltage/dyn_range*255)
def number_to_dac(value):
    GPIO.output(outp,[int(element) for element in bin(value)[2:].zfill(8)])
try:
    while True:
        try:
            voltage=float(input("Введите напряжение в вольтах:"))
            number=voltage_to_nomber(voltage)
            number_to_dac(number)
        except ValueError:
            print("Вы ввели не число.Попробуйте ещё раз\n")
finally:
    GPIO.output(outp,0)
    GPIO.cleanup()