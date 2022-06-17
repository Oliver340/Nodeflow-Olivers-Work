import numpy as np
from scipy.fftpack import fftfreq, irfft, rfft
class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='Wave_Data', preset='Object')
        nodeflow.createAttribute(name='Frequency_Cutoff', preset='Integer')

class Action:
    def __init__(self, node):    
        for attrName, attrData in node.attrsData.items():
            (globals()[attrName]) = attrData['attr']
        

        W = fftfreq(Wave_Data.nFrames, d=1/Wave_Data.sampleRate)
        f_signal = rfft(Wave_Data.samples)

        cut_f_signal = f_signal.copy()
        cut_f_signal[(np.abs(W)<Frequency_Cutoff)] = 0

        cs = irfft(cut_f_signal)
        waveData = [max(-32768, min(int(sample), 32767)) for sample in cs]
        Wave_Data.samples = waveData
        nodeflow.updateAttribute(node=node, name='Wave_Data', attr=Wave_Data)

                    
class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf