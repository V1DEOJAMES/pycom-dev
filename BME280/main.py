import pycom
import time
import struct
from machine import I2C
from machine import UART

pycom.heartbeat(False)

# UART
uart = UART(1, baudrate=115200)
uart.init(115200, bits=8, parity=None, stop=1)  # init with given parameters
uart.write('I2C Scanner')
print('I2C Scanner')


i2c = I2C(0)                         # create on bus 0
i2c = I2C(0, I2C.MASTER)             # create and init as a master
# create and use non-default PIN assignments (P10=SDA, P11=SCL)
i2c = I2C(0, pins=('P9', 'P10'))
i2c.init(I2C.MASTER, baudrate=100000)  # init as a master

terny = True
while True:
    # Dim Heartbeat
    if terny:
        pycom.rgbled(0x000011)  # Blue
    else:
        pycom.rgbled(0x000000)  # Off
    
    terny = not terny
    
    devices = i2c.scan()
    # Fill a list with scans
    if len(devices) == 0:
        print("No I2C device !")
    else:
        print('I2C devices found:',len(devices))

    for device in devices:  
        print("Decimal address: ",device," | Hexa address: ",hex(device))
    
    time.sleep(1)

