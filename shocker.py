from gpiozero import LED
from time import sleep
from threading import Thread


class Shocker:
    def __init__(self, channel):
        self.channel = channel
        self.led = LED(channel)
        self.led.on()

    def on(self):
        self.state = True
        self.led.off()

    def off(self):
        self.state = False
        self.led.on()

    def async_pulse(self, seconds):
        Thread(target=lambda: self.pulse(seconds)).start()

    def pulse(self, seconds=2):
        self.on()
        sleep(seconds)
        self.off()
