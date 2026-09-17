import RPi.GPIO as G
import time
G.setmode(G.BCM)
leds =[24, 22,23,27,17,25,12,16]
G.setup(leds, G.OUT)
G.output(leds, 0)
lt = 0.2
while True:
    for led in leds:
        G.output(led, 1)
        time.sleep(0.2)
        G.output(led, 0)
    for led in reversed(leds):
        G.output(led, 1)
        time.sleep(0.2)
        G.output(led, 0)