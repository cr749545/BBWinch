#!/usr/bin/env python
import time
from pymavlink import mavutil

#Winch control is connected on pin 4 of navigator.
winchPin=4
winchCW = 1100
winchCCW=1900
master = mavutil.mavlink_connection('tcp:127.0.0.1:5777')
master.wait_heartbeat()


#Function uses MAV util to set the auxiliary servo port to the desired PWM.
def set_servo_pwm(servo_n, microseconds):
	master.mav.command_long_send(
	master.target_system, master.target_component,
	mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
	0,
	servo_n,
	microseconds,
	0,0,0,0,0
	)

#Sets the winch to rotate either clockwise or counter-clockwise for the defined number of seconds (duration)
def moveWinch(direction, dur):
	print("Starting winch.")
	#Set the direction of motion.
	set_servo_pwm(winchPin,direction)
	#Go in that direction.
	time.sleep(dur)
	#Stop the winch.
	set_servo_pwm(4,1500)
	print("Winch stopped.")


#Move winch CW and CCW for ten seconds.
moveWinch(winchCW,10)
moveWinch(winchCCW,10)
