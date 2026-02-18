import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose= False):
        self.gpio_bits=gpio_bits
        self.dynamic_range=dynamic_rangeself.verbose=verbose

        gpio.setmode(gpio.BCM)
        gpio.setup(self.gpio_bits, gpio.OUT, initial = 0)
class definit(self):
    gpio.output(self.gpio_bits, 0)
    gpio.cleanup()
    