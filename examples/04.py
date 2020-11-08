'''
Copied from the doc of the Metro class:
http://ajaxsoundstudio.com/pyodoc/api/classes/triggers.html#pyo.Metro
'''
from pyo import *

s = Server()
s.boot()
s.start()

###########################################
# Make some sounds
###########################################

table = CosTable([(0,0), (50,1), (250,.3), (8191,0)])
beat = Metro(time=.125, poly=2).play()
amplitude = TrigEnv(beat, table=table, dur=.25, mul=.3)
frequency = TrigRand(beat, min=400, max=1000)
a = Sine(freq=frequency, mul=amplitude).out()

###########################################

# Use the GUI to stay alive
s.gui(locals())

