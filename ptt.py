#!/usr/bin/env python3

import os
import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

hostname = 'intercom1'  # Hostname or IP of device to call

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 40 to be an input pin and set initial value to be pulled high (on)

mic = 0
print ("Setting mic to off")
os.system("amixer -c 1 sset Mic off")
print("Mic muted")

while True:
	try:
		if mic == 0 and GPIO.input(40) == GPIO.LOW:
			mic = 1
			print("Unmuting mic")
			os.system("amixer -c 1 sset Mic on")
			print("Calling intercom1")
			os.system("screen -S seren -p 0 -X stuff '/c {}\n'".format(hostname))
			print("Mic unmuted")
		elif mic == 1 and GPIO.input(40) == GPIO.HIGH:
			mic = 0
			print("Muting mic")
			os.system("amixer -c 1 sset Mic off")
			print("Hanging up")
			os.system("screen -S seren -p 0 -X stuff '/H\n'")
			print("Mic muted")
	except:
		print("Failed to execute command")
