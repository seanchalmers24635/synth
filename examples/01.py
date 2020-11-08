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

# Stay alive briefly and then exit
time.sleep(5)
s.stop()
s.shutdown()
