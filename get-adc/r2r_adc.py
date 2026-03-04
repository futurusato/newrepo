import RPi.GPIO as gpio
import time
class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range=dynamic_range
        self.verbose = verbose
        self.compare_time=compare_time

        self.bits_gpio=[26,20,19,16,13,12,25,11]
        self.comp_gpio=21

        gpio.setmode(gpio.BCM)
        gpio.setup(self.bits_gpio, gpio.OUT, initial = 0)
        gpio.setup(self.comp_gpio, gpio.IN)
    def deinit(self):
        for pin in self.bits_gpio:
            gpio.output(pin, gpio.LOW)
        gpio.cleanup()
    
    def number_to_dac(self, number):
        def set_number(self,number):
            gpio.output(self.bits_gpio,[int(element) for element in bin(number)[2:].zfill(8)])
        voltage=(number/255)*self.dynamic_range
        print(f"Установлено напряжение: {voltage:.3f}")
    
    def sequential_counting_adc(self):
        for number in range(256):
            self.number_to_dac(number)
            time.sleep(self.compare_time)

            if gpio.input(self.comp_gpio)==gpio.HIGH:
                return number
            else:
                return 255
    def get_sc_voltage(self):
        digital_value=self.sequential_counting_adc()
        voltage = (digital_value/255)*self.dynamic_range
        return voltage
    
if __name__=="__main__":
    try:
        DR=2.7
        adc = R2R_ADC(dynamic_range=DR, compare_time=0.01, verbose=True)
        while True:
            voltage=adc.get_sc_voltage()
            print(f"\nТекущее напряжение:{voltage:.3f}В")
    finally:
        adc.deinit()