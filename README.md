Project description: the following files are used to control mini-winch onboard a BlueRobotics BlueBoat. The blueboat is controlled via a raspberry pi / BR navigator.


Contents:
BBWinch.py - python implementation for control of Beast 2000 RC winch.
loiterRead.py - python implementation for determining navigation status of blueboat (specifcally when the boat is loitering around a waypoint).
readSwitch.py - python implementation to read digital value from the navigator board.
TODO:
Implement limit switch to determine when winch has fully spooled.
