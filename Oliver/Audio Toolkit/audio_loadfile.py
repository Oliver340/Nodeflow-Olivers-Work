import numpy as np
import wave, struct
class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='File_Name', preset='String', attr='')
        nodeflow.createAttribute(name='Wave_Data', preset='Object', socket=False)

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

        wav_file = wave.open(File_Name, 'rb')
        binary_data = wav_file.readframes(wav_file.getnframes())
        samples = np.array(struct.unpack('{n}h'.format(n=wav_file.getnframes()*wav_file.getnchannels()), binary_data))
        sampleRate = wav_file.getframerate()
        numChannels = wav_file.getnchannels()
        sampleWidth = wav_file.getsampwidth()
        nFrames = wav_file.getnframes()
        wav_file.close()

        waveObj = WaveData(samples, sampleRate, numChannels, sampleWidth, len(samples))
        nodeflow.updateAttribute(node=node, name='Wave_Data', attr=waveObj)


class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf