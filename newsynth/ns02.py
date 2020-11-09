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
beat = Metro(time=.700, poly=2).play()
amplitude = TrigEnv(beat, table=table, dur=3, mul=.3)
frequency = TrigChoice(beat, [100, 200, 300])
a = Sine(freq=frequency, mul=amplitude).out()
#h2 = Harmonizer(a, transpo=12).out()
# Use the GUI to stay alive
s.gui(locals())
