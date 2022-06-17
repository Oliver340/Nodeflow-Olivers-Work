import matplotlib.pyplot as plt
import numpy as np
class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='Wave_Data', preset='Object')

class Action:
    def __init__(self, node):    
        for attrName, attrData in node.attrsData.items():
            (globals()[attrName]) = attrData['attr']
        
        Time = np.linspace(0, len(Wave_Data.samples) / (Wave_Data.sampleRate * Wave_Data.numChannels), num=len(Wave_Data.samples))
        plt.plot(Time, Wave_Data.samples)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.show()
                    
class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf