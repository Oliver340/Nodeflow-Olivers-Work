import numpy as np
class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='Notes', preset='Object', socket=False)

class Action:
    def __init__(self, node):    
        for attrName, attrData in node.attrsData.items():
            (globals()[attrName]) = attrData['attr']


        notes = Action.get_piano_notes
        nodeflow.updateAttribute(node=node, name='Notes', attr=notes)

    def get_piano_notes():   
        # White keys are in Uppercase and black keys (sharps) are in lowercase
        octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
        base_freq = 440 #Frequency of Note A4
        keys = np.array([x+str(y) for y in range(0,9) for x in octave])
        # Trim to standard 88 keys
        start = np.where(keys == 'A0')[0][0]
        end = np.where(keys == 'C8')[0][0]
        keys = keys[start:end+1]

        # note_freq = base_freq * 2^(n/12) ; where n is the number of notes away from the base note
        note_freqs = dict(zip(keys, [2**((n+1-49)/12)*base_freq for n in range(len(keys))]))
        note_freqs[''] = 0.0 # stop
        note_freqs['R'] = 0.0 # rest
        return note_freqs

class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf



