# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

# Build the array holding the data on each limb
from array import *

# Two PCA985 controllers
# PWM1 is on 0x40
# PWM2 is on 0x41
Limbs = [["LeftFrontShoulder","PWM1",8,250,500],
        ["LeftFrontElbow","PWM1",10,250,500],
        ["LeftFrontAnkle","PWM1",13,250,500],
        ["LeftMiddleShoulder","PWM1",9,250,500],
        ["LeftMiddleElbow","PWM1",14,250,500],
        ["LeftMiddleAnkle","PWM1",15,250,500],
        ["LeftBackShoulder","PWM2",8,250,500],
        ["LeftBackElbow","PWM2",9,250,500],
        ["LeftBackAnkle","PWM2",10,250,500],
        ["RightFrontShoulder","PWM1",7,250,500],
        ["RightFrontElbow","PWM1",5,250,500],
        ["RightFrontAnkle","PWM1",2,250,500],
        ["RightMiddleShoulder","PWM2",6,250,500],
        ["RightMiddleElbow","PWM2",1,250,500],
        ["RightMiddleAnkle","PWM2",0,250,500],
        ["RightBackShoulder","PWM2",7,250,500],
        ["RightBackElbow","PWM2",6,250,500],
        ["RightBackAnkle","PWM2",5,250,500]]

# for i in range(len(Limbs)):
# 	print(str(Limbs[i][0]) + ' will run from ' + str(Limbs[i][3]) + ' to ' + str(Limbs[i][4]))
# 	print()

#print(Limbs[0])

#print(Limbs[1][2])

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 250  # Min pulse length out of 4096
servo_max = 500  # Max pulse length out of 4096
servo_name = 13

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

# print('Moving servo on channel 0, press Ctrl-C to quit...')
    
for i in range(len(Limbs)):
	if Limbs[i][1] == "PWM1":
		print(str(Limbs[i][0]) + ' will run from ' + str(Limbs[i][3]) + ' to ' + str(Limbs[i][4]))
		pwm.set_pwm(servo_name, 0, servo_min)
		time.sleep(3)
		pwm.set_pwm(servo_name, 0, servo_max)
		x = input('Press Enter to continue:')
		print()

