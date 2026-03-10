import RPi.GPIO as GPIO
import time
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    def deinit(self):
        GPIO.output(self.bits_gpio,0)
        GPIO.cleanup()
    def number_to_dac(self,number):
        num=dec2bin(number)
        GPIO.output(self.bits_gpio,num)
    def sequential_counting_adc(self):
        max=255
        for val in range(max+1):
            self.number_to_dac(val)
            time.sleep (0.01)
            comp=GPIO.input(self.comp_gpio)
            if comp==1:
               return val
        return max
    def get_sc_voltage(self):
        volt=(self.sequential_counting_adc()/256)*self.dynamic_range
        GPIO.output(self.bits_gpio,self.sequential_counting_adc())
        return volt
    def successive_approximation_adc(self):
        v=0
        for i in range(7,-1,-1):
            v|=(1<<i)
            self.number_to_dac(v)
            comp=GPIO.input(self.comp_gpio)
            time.sleep (0.01)
            if comp==1:
               v&=~(1<<i)
        return(v)
    def get_sar_voltage(self):
        volt=(self.successive_approximation_adc()/256)*self.dynamic_range
        GPIO.output(self.bits_gpio,self.successive_approximation_adc())
        return volt
if  __name__=="__main__":
    try:
        dac = R2R_ADC(3.285)
        while True:
            print(dac.get_sar_voltage())
    finally:
        dac.deinit()
