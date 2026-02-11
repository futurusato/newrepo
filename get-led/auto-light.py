import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
led = 26
tr = 6
gpio.setup(tr, gpio.IN)
gpio.setup(led, gpio.OUT)
while True:
    if gpio.input(tr)==1:
        gpio.output(led, 0)
    else:
        gpio.output(led,1)
