# HoneyPot - Discoveray Vehicle

We are building a remote vehicle to discover and take photos of the the 4th floor false ceiling.
We have enough hardware to make: **A vehicle controlled by a mounted raspberry pi, along with a fixed angle camera**

The raspberry will have a server (PHP) with a simple web interface to send commands and receive video stream. The commands sent are translated by the server to GPIO signals to controls the motors.

# Important note:
The prototype built in the project will be used in other entertainment projects designed by "you". 

# suggestions:
1. Making a VR Laser Tag War.
2. Use Bot over robot so he can interact with voice and answer it.

# !ISSUES 
1. Fix permission of gpiomem to be rootless access in order to work with python
2. Install vlc-nox to run the RTMP server

# Run Steps [Reboot Required]
1. Enable RPi camera module using GUI:
  a. Start Menu -> Raspberry Pi Configuration
  b. Interfaces Tab 
  c. Enable Camera
  
2. Terminal
  a. sudo raspi-config
  b. Select the Interfacing Options.
  c. Enable the camera
  
# Running Camera streamer
1. python3 rpi_camera_surveillance_system.py
2. http:localhost:8000/ 

# Mocking RPi hardware for development 
1. install fake-rpi: pip install fake-rpi (https://pypi.org/project/fake-rpi/)
  
