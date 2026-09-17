import RPi.GPIO as G
G.setmode(G.BCM)
led = 26
G.setup(led, G.OUT)
delitel = 6
G.setup(delitel, G.OUT)
state = 0
while True:
    if G.input(delitel) == 0:
        G.input(delitel)
        state = 0
        G.output(led, state)
    else:
        state = 1
        G.output(led, state)
