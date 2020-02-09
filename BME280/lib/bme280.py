import pycom
import struct
from machine import I2C
    
BME280_REG_ID = const(0xD0)
BME280_REG_RESET = const(0xE0)
BME280_REG_CTRL_HUM = const(0xF2)
BME280_REG_STATUS = const(0XF3)
BME280_REG_CTRL_MEAS = const(0xF4)
BME280_REG_CONFIG = const(0xF5)
BME280_REG_PRESS_START = const(0xF7)
BME280_REG_TEMP_START = const(0xFA)
BME280_REG_HUM_START = const(0xFD)
    
class BME280:
    def __init__(self, i2c, addr=0x77):
        self.i2c = i2c
        self.addr = addr
        devices = i2c.scan()
        # Fill a list with scans
        if len(devices) == 0:
            print("(BME280) No I2C devices found!")
        else:
            print('(BME280) I2C devices found:',len(devices))
            for device in devices:  
                if(device == addr):
                    print("(BME280) Address: ",hex(device))
                    self.whoami =  self.i2c.readfrom_mem(self.addr, BME280_REG_ID, 1)
                    if (self.whoami[0] != 0x60):
                        raise ValueError("(BME280) Returned whoami of ",self.whoami[0], " but expected 0x60")
                    else:
                        print("(BME280) Good address, whoami confirmed: ",hex(self.whoami[0]))
                else:
                    print("(BME280) Other I2C Device Address: ",hex(device))
        print("(BME280) Writing 0xB6 to Reset")
        self.i2c.writeto_mem(self.addr, BME280_REG_RESET, 0xB6)
                
            

