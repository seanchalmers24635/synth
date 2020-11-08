from pyo import *

s = Server()

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
