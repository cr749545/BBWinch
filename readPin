import RPi.GPIO as GPIO

#Note: "pin14" is the raspi name for the name, on the navigator stack it is 
#referred to as the Tx port of serial1.
#Check to ensure the serial pin isn't in use with navigator hardware.
inputPin = 14
#Setup for pin14 to be read as a digital input.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Set pin as input.
GPIO.setup(inputPin, GPIO.IN)
#Set pin to pulldown.
GPIO.setup(inputPin, GPIO.LOW)
#Poll the pin.
state = GPIO.input(inputPin)
while(True)
  if(state):
  	print("ON")
    #Run the winch script here.
  else:
  	print("OFF")
  #Do nothing.
