'''
This is the Pyo code demoed in https://www.youtube.com/watch?v=ROlkhVs15AM&t=1m20s

Hint: comment out the 'stop()' lines to hear that element

'''

from pyo import *

s = Server()

# Start the server
s.boot()
s.start()

###########################################
# Make some sounds
###########################################

## Configuring our beat ##########################

### signal shape (in this case, a square wave)
wav = SquareTable()

### beat timing
# beat = Metro(time=1, poly=1).play()
beat = Metro(time=0.125, poly=5).play()
# beat = Beat(time=0.125, taps=64, poly=5).play()

### amplitude envelope shape
envelope = CosTable([(0,0), (100,1), (500,.3), (8191,0)])
# envelope = CurveTable([(0,0),(2048,.5),(4096,.2),(6144,.5),(8192,0)], 0, 20)

### amplitude
amplitude = TrigEnv(beat, table=envelope, dur=0.25, mul=0.6)

### random notes
pitch = TrigXnoiseMidi(beat, dist=3, scale=0, mrange=(24, 24))


## Triggering an oscillator ##########################

oscillator = Osc(table=wav, freq=pitch, mul=amplitude).out()
oscillator.stop()


## We love synth ##########################

### synth signal shape
sig = SawTable(order=12).normalize()
# sig = LinTable([(0,20), (200,5), (1000,2), (8191,1)])

### tempo
metro_synth = Metro(time=0.125, poly=2).play()

### LFO filter
lfo = LFO(freq=1.2, sharp=0.2, type=4, mul=110, add=220)

### synth envelope
envelope_synth = TrigEnv(metro_synth, table=sig, dur=0.5)


## Triggering a synth ##########################

synth = FM(carrier=[220.5,220], ratio=[.2498,.2503], index=envelope_synth, mul=0.5).out()
synth = FM(carrier=lfo, ratio=[.2498,.2503], index=envelope_synth, mul=0.3).out()
synth.stop()


## Who doesn't like the 80's ? ##########################

lfd = Sine([.4,.2], mul=.2, add=.5)
synth_80 = SuperSaw(freq=440, detune=lfd, bal=6, mul=0.2).out()
synth_80.stop()

###########################################


# Use the GUI to stay alive
s.gui(locals())

