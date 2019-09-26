from gpiozero import LED
from time import sleep


class Shocker:
    channel = -1
    led = None

    def __init__(self, channel):
        self.channel = channel
        self.led = LED(channel)
        self.led.on()

    def on(self):
        self.led.off()

    def off(self):
        self.led.on()

    def pulse(self, seconds=2):
        self.led.off()
        sleep(seconds)
        self.led.on()
