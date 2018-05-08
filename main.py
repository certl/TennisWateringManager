from time import sleep
#from network import LoRa
import socket
import binascii
from pycom import heartbeat,rgbled
#from pybytes import Pybytes
from machine import Pin,ADC,RTC
#from pysense import Pysense
#from SI7006A20 import SI7006A20
#from MPL3115A2 import MPL3115A2,PRESSURE


# Start WIFI configuration at boot
print("\nStarting Wifi ...")
execfile('/flash/homewifi.py')

print("\nDone connecting Wifi")

print("\nSetting up RTC ...")
rtc = RTC()
rtc.ntp_sync("pool.ntp.org")

print("\nSetting up Pins")
adc = ADC()
apin_court1 = adc.channel(pin='P13',attn=ADC.ATTN_11DB)
apin_court2 = adc.channel(pin='P14',attn=ADC.ATTN_11DB)
vcc_out = Pin('P9', mode = Pin.OUT, pull = Pin.PULL_DOWN)
valve_court_1 = Pin('P19', mode = Pin.OUT, pull = Pin.PULL_DOWN)
valve_court_2 = Pin('P20', mode = Pin.OUT, pull = Pin.PULL_DOWN)
valve_middle = Pin('P21', mode = Pin.OUT, pull = Pin.PULL_DOWN)

print("\nStarting work now\n\n")

"""Pybytes Registration"""
"""USERNAME = "christoph.ertl@me.com"
DEVICE_ID = "ad9f9646-b990-496d-b976-81ea7ee6df68"
SERVER = "mqtt.pybytes.pycom.io"
pybytes = Pybytes(USERNAME, DEVICE_ID, SERVER)
pybytes.connect_wifi()
"""

"""Pressure Sensor"""
"""def press_sensor():
    mpp = MPL3115A2(py,mode=PRESSURE)
    press = mpp.pressure()
 return press
"""

"""Humidity Sensor"""
"""def humid_temp_sensor():
    si = SI7006A20(py)
    humid = si.humidity()
    temp = si.temperature()
 return(humid,temp)
"""

def moist_sensor(court):
    vcc_out.value(1)
    if court == 1:
        print("Getting court moisture for court 1. ")
        volts = apin_court1.value()
    elif court == 2:
        print("Getting court moisture for court 2. ")
        volts = apin_court2.value()
    else:
        volts = 0
        print("Unexpected court number received: %d", court)
    vcc_out.value(0)
    return volts/4.096

def manage_watering(court, state)
    if court == 1:
        if


def main():
#    temp = int(humid_temp_sensor()[1])
#    press = int(press_sensor())
#    humid = int(humid_temp_sensor()[0])
    moist_court1 = int(moist_sensor(1) /4.096)
    moist_court2 = int(moist_sensor(2) /4.096)
    pybytes.send_virtual_pin_value(False, 16, moist_court1)
    pybytes.send_virtual_pin_value(False, 15, moist_court2)
#    pybytes.send_virtual_pin_value(False, 14, press)
#    pybytes.send_virtual_pin_value(False, 13, humid)

    """ Turn on watering if necessary """
    manage_watering()





    sleep(3)
main()
py.go_to_sleep()
