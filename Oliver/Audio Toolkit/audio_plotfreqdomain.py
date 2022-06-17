from scipy.fftpack import fftfreq, irfft, rfft
import matplotlib.pyplot as plt
import numpy as np
class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='Wave_Data', preset='Object')

class Action:
    def __init__(self, node):    
        for attrName, attrData in node.attrsData.items():
            (globals()[attrName]) = attrData['attr']
        
        W = fftfreq(Wave_Data.nFrames, d=1/Wave_Data.sampleRate)
        f_signal = rfft(Wave_Data.samples)
        waveData = [np.abs(sample) for sample in f_signal]
        Time = [np.abs(sample) for sample in W]
        plt.plot(Time, waveData)
        plt.xlabel('Frequency')
        plt.ylabel('Amplitude')
        plt.show()

                    
class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf