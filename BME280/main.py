import pycom
import time
import struct
from machine import I2C
from machine import UART
from bme280 import BME280

pycom.heartbeat(False)

# UART
uart = UART(1, baudrate=115200)
uart.init(115200, bits=8, parity=None, stop=1)  # init with given parameters
# I2C
i2c = I2C(0)                         # create on bus 0
i2c = I2C(0, I2C.MASTER)             # create and init as a master
i2c = I2C(0, pins=('P9', 'P10'))
i2c.init(I2C.MASTER, baudrate=100000)  # init as a master
# BME280
enviro_sensor = BME280(i2c, addr=0x77)

terny = True
while True:
    # Dim Heartbeat
    if terny:
        pycom.rgbled(0x000011)  # Blue
    else:
        pycom.rgbled(0x000000)  # Off
    terny = not terny
    time.sleep(1)

