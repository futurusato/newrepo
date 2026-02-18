import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
pins = [22,27,17,26,25,21,20,16]
gpio.setup(pins, gpio.OUT)
dynamic_range = 3.3
def voltage_to_number(voltage):
    if not (0.0 <= voltage<= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
        print("Устанавливаем 0.0 В")
        return 0

        return int(voltage / dynamic_range * 255)
def number_to_dac(value):
    gpio.output(pins, [int(element) for element in bin(value)[2:].zfill(8)])
try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах:"))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз \n")
finally:
    gpio.output(pins, 0)
    gpio.cleanup()