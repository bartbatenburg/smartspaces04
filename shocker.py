from gpiozero import LED
from asyncio import get_event_loop

event_loop = get_event_loop()


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
        self.on()
        event_loop.call_later(seconds, self.off)
