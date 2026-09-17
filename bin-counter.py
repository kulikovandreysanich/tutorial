import RPi.GPIO as G
import time
G.setmode(G.BCM)
leds =[16, 12, 25, 17, 27, 23, 22, 24]
G.setup(leds, G.OUT)
G.output(leds, 0)
up = 9
G.setup(up, G.IN)
down = 10
G.setup(down, G.IN)
num = 0
sleep = 0.2
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)] 
while True:
    if G.input(up):
        num +=1
        time.sleep(sleep)
    if G.input(down):
        num -=1
        time.sleep(sleep)
    if num < 0:
        num = 255
    if num > 255:
        num = 0
    print(num,dec2bin(num))
    G.output(leds, dec2bin(num))
    time.sleep(0.1)