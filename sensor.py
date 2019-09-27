from __future__ import division
from smbus import SMBus
from time import sleep

PWR_M = 0x6B
DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_EN = 0x38


# X2 & Z2, abs(een) > 0.5, abs(ander) > 0.7
# X1: >-0.1 ==> <-0.5

class Sensor:
    ADDR_X = 0x3B
    ADDR_Y = 0x3D
    ADDR_Z = 0x3F

    def __init__(self, bus, address):
        self.address = address
        self.bus = SMBus(bus)
        self.x = 0
        self.y = 0
        self.z = 0
        self.bus.write_byte_data(self.address, DIV, 7)
        self.bus.write_byte_data(self.address, PWR_M, 1)
        self.bus.write_byte_data(self.address, CONFIG, 0)
        self.bus.write_byte_data(self.address, GYRO_CONFIG, 24)
        self.bus.write_byte_data(self.address, INT_EN, 1)

    def update(self):
        self.x = self.readMPU(Sensor.ADDR_X)
        self.y = self.readMPU(Sensor.ADDR_Y)
        self.z = self.readMPU(Sensor.ADDR_Z)

    def readMPU(self, address):
        high = self.bus.read_byte_data(self.address, address)
        low = self.bus.read_byte_data(self.address, address + 1)
        value = ((high << 8) | low)
        if value > 32768:
            value = value - 65536
        return value / 16384.0


if __name__ == '__main__':
    sensor1 = Sensor(0, 0x68)
    sensor2 = Sensor(1, 0x68)

    while True:
        sensor1.update()
        sensor2.update()
        print("X1=%f, Y1=%f, Z1=%f" % (sensor1.x, sensor1.y, sensor1.z))
        print("X2=%f, Y2=%f, Z2=%f" % (sensor2.x, sensor2.y, sensor2.z))
        sleep(0.25)
