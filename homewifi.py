import machine
import pycom
import time
from network import WLAN

pycom.heartbeat(False)
print ("LED on")
pycom.rgbled(0x7f0000)
time.sleep(1)

wlan = WLAN(mode=WLAN.STA)
wlan.connect('unifi-private', auth=(WLAN.WPA2, '3148959585322586'), timeout=5000 )
print("Connecting WLAN")
while not wlan.isconnected():
    machine.idle()
wlan = WLAN()

pycom.rgbled(0x00007F)

time.sleep(1)
pycom.rgbled(0x007f00)

print(wlan.ifconfig())
print("\n")

pycom.heartbeat(True)
