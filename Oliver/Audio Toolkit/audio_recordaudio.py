import sounddevice as sd
import numpy as np

class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='Wave_Data', preset='Object')
        nodeflow.createAttribute(name='Duration', preset='Integer')

class WaveData:
    def __init__(self, samples, sampleRate, numChannels, sampleWidth, nFrames):
        self.samples = samples
        self.sampleRate = sampleRate
        self.numChannels = numChannels
        self.sampleWidth = sampleWidth
        self.nFrames = nFrames

class Action:
    def __init__(self, node):    
        for attrName, attrData in node.attrsData.items():
            (globals()[attrName]) = attrData['attr']

        fs=44100
        duration = Duration  # seconds
        myrecording = sd.rec(duration * fs, samplerate=fs, channels=2,dtype=np.short)
        print("Recording Audio")
        sd.wait()
        print("Audio recording complete")
        
        waveData = [item for sublist in myrecording for item in sublist]
        waveObj = WaveData(np.array(waveData), fs, 2, 2, len(waveData))
        nodeflow.updateAttribute(node=node, name='Wave_Data', attr=waveObj)

        
class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf
