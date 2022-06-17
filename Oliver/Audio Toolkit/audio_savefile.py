import wave
import struct
class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='File_Name', preset='String', attr='')
        nodeflow.createAttribute(name='Wave_Data', preset='Object')

class Action:
    def __init__(self, node):    
        for attrName, attrData in node.attrsData.items():
            (globals()[attrName]) = attrData['attr']
        
        wav_file=wave.open(File_Name, 'w')
        wav_file.setparams((Wave_Data.numChannels, Wave_Data.sampleWidth, Wave_Data.sampleRate, Wave_Data.nFrames, "NONE", "not compressed"))
        for sample in Wave_Data.samples:
            wav_file.writeframes(struct.pack('h', int(sample)))

                    
class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf