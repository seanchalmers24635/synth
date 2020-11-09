from pyo import *

s = Server()

# Try different audio systems
s = Server(duplex=1, winhost="asio")

# Try setting different input/output devices
s.setInputDevice(2)
s.setOutputDevice(7)

# Start the server
s.boot()
s.start()

###########################################
# Make some sounds
###########################################
a = Sine(freq=440, mul=0.2).out()

###########################################

# Use the GUI to stay alive
s.gui(locals())
