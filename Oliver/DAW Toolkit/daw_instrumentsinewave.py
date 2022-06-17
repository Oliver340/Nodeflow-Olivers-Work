import numpy as np
from .polysynth import *
class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='Instrument', preset='Object', socket=False)

class Action:
    def __init__(self, node):    
        for attrName, attrData in node.attrsData.items():
            (globals()[attrName]) = attrData['attr']

        instrument = Action.get_sine_wave
        nodeflow.updateAttribute(node=node, name='Instrument', attr=instrument)


    def get_sine_wave(frequency, duration=0.5, sample_rate=44100, amplitude=4096, number_channels=2, volume=1):
        t = np.linspace(0, duration, int(sample_rate*duration*number_channels)) # Time axis
        # g(f) = A sin(2πft)
        wave =  volume*amplitude*np.sin(2*np.pi*frequency*t)
        return wave


class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf


