# Pi Zero Time Lapse Camera App - FastGTR
# Version 1 - May 2020
import time
from picamera import PiCamera
from datetime import datetime, timedelta

camera = PiCamera()
camera.resolution = (2592, 1944)
camera.vflip = True
camera.hflip = True
camera.iso = 200
time.sleep(2) # Wait for the automatic gain control to settle
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g

ts=time.strftime("%Y-%m-%d-%H%M%S", time.localtime())
camera.capture('img-'+ts+'.jpg', format="jpeg", quality=90)