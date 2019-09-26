from gpiozero import LED
from asyncio import new_event_loop, set_event_loop

loop = new_event_loop()
set_event_loop(loop)


class Shocker:
    channel = -1
    led = None

    def __init__(self, channel):
        self.channel = channel
        self.led = LED(channel)
        self.led.on()

    def on(self):
        print("Turning on channel %s" % self.channel)
        self.led.off()

    def off(self):
        print("Turning off channel %s" % self.channel)
        self.led.on()

    def pulse(self, seconds=2):
        def db():
            print("CB")
            self.off()

        print("Loop status: " + ("Running" if loop.is_running else "Closed"))
        self.on()
        loop.call_later(seconds, db)
