#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO

import rfs
import ph
import ppm
import wts
import Ats
import Ahs

import wvs
import Prf
import Pfr
import Prw
import mp

GPIO.setmode(GPIO.BOARD)

#device module explained with gpio slot
GPIO.setup(chan, GPIO.IN) # wts = water temp sensor ADC
GPIO.setup(chan, GPIO.IN) # ppm = tds sensor ADC
GPIO.setup(chan, GPIO.IN) # ph = ph sensor ADC 
GPIO.setup(chan, GPIO.IN) # ats = ambient temp sensor DHT-11 
GPIO.setup(chan, GPIO.IN) # ahs = ambient humidity sensor DHT-11 
GPIO.setup(chan, GPIO.IN) # rfs = reservoir fluid sensor 
GPIO.setup(chan, GPIO.OUT) # wvs = water valve solenoid
GPIO.setup(chan, GPIO.OUT) # prf = pump reservoir to field
GPIO.setup(chan, GPIO.OUT) # pfr = pump field to reservoir
GPIO.setup(chan, GPIO.OUT) # prw = pump reservoir to waste
GPIO.setup(chan, GPIO.OUT) # HVAC 
GPIO.setup(chan, GPIO.OUT) # lighting 

#reserv fluid level variables
rps_max=100
rps_min=75

#calls reservoir fluid sensor mod returns capacity in an integer value
rps = rps.int()

#calls modules ph and Ppm returns results
ppm = Ppm.int()
ph = Ph.int()

#Constant display for ppm Ph rps and status
reserv fluid level and water purity check
I f rps > int(75) :
    prw:
        wvs:
            Ppm < int(100)
                Or print("fresh water ppm higher than expected error")

Else prf





#initiate pump reservoir to field
 psf on untel fwts response              



if __name__ == '__main__': 

