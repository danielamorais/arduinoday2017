import pingo
from time import sleep

board = pingo.detect.MyBoard()
led_pin = board.pins[13]
led_pin.mode = pingo.OUT

while True:
    led_pin.hi()
    sleep(1)
    led_pin.lo()
    sleep(1)
