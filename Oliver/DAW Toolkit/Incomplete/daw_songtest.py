import numpy as np
from .daw_notetest import WaveData, Note, Instrument
# D4,sn-D4,sn-D5,dsn-A4,den-R,sn-g4,sn-R,sn-G4,sn-R,sn-F4,sn-F4,sn-D4,sn-F4,sn-G4,sn
class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='Wave_Data', preset='Object', socket=False)
        nodeflow.createAttribute(name='Volume', preset='Float')
        #Note given as "NoteNumber" ex. "C4" the 4th C
        nodeflow.createAttribute(name='Notes', preset='String')
        nodeflow.createAttribute(name='BPM', preset='Float')

class Action:
    def __init__(self, node):    
        for attrName, attrData in node.attrsData.items():
            (globals()[attrName]) = attrData['attr']

        music_notes = Notes
        data = Action.get_song_data(music_notes)
        
        waveData = [max(-32768, min(int(sample), 32767)) for sample in data]

        waveObj = WaveData(waveData, 44100, 2, 2, len(waveData))
        nodeflow.updateAttribute(node=node, name='Wave_Data', attr=waveObj)


    def get_song_data(music_notes):
        # Function to concatenate all the waves (notes)
        note_freqs = Instrument.get_piano_notes() # Function that we made earlier
        music_notes = music_notes.split('-')
        music_notes = [note.split(',') for note in music_notes]
        song = [Instrument.get_sine_wave(note_freqs[note[0]], Note[note[1]].value/BPM, volume=Volume) for note in music_notes]
        song = np.concatenate(song)
        return song

class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf