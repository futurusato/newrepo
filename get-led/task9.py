import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
leds = [16,12,25,17,27,23,22,24]
up = 9
down=10
gpio.setup(up, gpio.IN)
gpio.setup(down, gpio.IN)
gpio.setup(leds, gpio.OUT)
gpio.output(leds,0)
num = 0
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
sleep_time = 0.2
while True:
    if gpio.input(up):
        num+=1
        print(num,dec2bin(num))
        time.sleep(sleep_time)
    if gpio.input(down):
        num-=1
        print(num,dec2bin(num))
        time.sleep(sleep_time)
    if num<0 or num>255:
        print(0, dec2bin(0))
        time.sleep(sleep_time)
    if gpio.input(down and up):
        num=255
        print(num,dec2bin(num))
        time.sleep(sleep_time)
    gpio.output(leds,dec2bin(num))