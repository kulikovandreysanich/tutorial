import RPi.GPIO as G
import time
G.setmode(G.BCM)
led = 26
G.setup(led, G.OUT)
botton = 13
G.setup(botton, G.IN)
state = 0
period = 0.2
while True:
    if G.input(botton):
        state = not state
        G.output(led, state)
        time.sleep(period)