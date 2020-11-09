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
table = CosTable([(0,0), (50,1), (250,.3), (8191,0)])
beat = Metro(time=.500, poly=2).play()
amplitude = TrigEnv(beat, table=table, dur=.25, mul=.3)
frequency = TrigRand(beat, min=400, max=450)
a = Sine(freq=frequency, mul=amplitude).out()
h1 = Harmonizer(a, transpo=12).out()
h2 = Harmonizer(h1, transpo=5).out()

#b = Sine(freq=100, mul=0.999).out()
ch = Chorus(a, depth=5, feedback=0.999999).out()
###########################################

# Use the GUI to stay alive
s.gui(locals())
