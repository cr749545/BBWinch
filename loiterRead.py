#Basic test program for reading the values of the hearbeat message.
#Set up includes:
import time
from pymavlink import mavutil

#Create the connection:
master = mavutil.mavlink_connection('tcp:127.0.0.1:5777')

#Wait for a hearbeat message:
master.wait_heartbeat()
#Confirm HB received.
print("Received Hearbeat.")

#Read contents of the heartbeat message.
msg_received = False
msg = master.recv_match(type='HEARTBEAT',blocking=True)
#Keep reading messages until you get one of Type==11, which will contain flight mode updates.
while(msg_received==False):
	msg=master.recv_match(type='HEARTBEAT',blocking=True)
	if(msg.type==11):
		msg_received = True
#Check the value of the custom state to see the state of the vehicle.
#Convert the message to a string:
print(msg)
print("Type:",msg.type,"Custom mode value is:",msg.custom_mode)
print(msg.type)
