import RPi.GPIO as G
import time
G.setmode(G.BCM)
led = 26
G.setup(led, G.OUT)
state = 0
period = 1.0
while True:
    G.output(led, state)
    state = not state
    time.sleep(period)