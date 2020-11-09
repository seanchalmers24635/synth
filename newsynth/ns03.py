from pyo import *

s = Server().boot()
s.start()

a = SineLoop(freq=[200,300,400,500], feedback=0.05, mul=.1).out()

def event_0():
    a.freq=[200]

def event_2():
    a.freq=[300]

def event_1():
    a.freq=[150]


m = Metro(1).play()
c = Counter(m, min=0, max=3)
sc = Score(c)



s.gui(locals())