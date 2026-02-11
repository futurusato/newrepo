import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
button = 13
led = 26
gpio.setup(button, gpio.IN)
gpio.setup(led, gpio.OUT)
state = 0
while True:
    if gpio.input(button):
        state = not state
        gpio.output(led, state)
        time.sleep(0.2)