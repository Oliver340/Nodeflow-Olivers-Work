import numpy as np
import enum
# D4,sn-D4,sn-D5,dsn-A4,den-R,sn-g4,sn-R,sn-G4,sn-R,sn-F4,sn-F4,sn-D4,sn-F4,sn-G4,sn
class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='Wave_Data', preset='Object', socket=False)
        nodeflow.createAttribute(name='Volume', preset='Float')
        #Note given as "NoteNumber" ex. "C4" the 4th C
        nodeflow.createAttribute(name='Song_Data', preset='String')
        nodeflow.createAttribute(name='BPM', preset='Float')
        nodeflow.createAttribute(name='Instrument', preset='Object')
        nodeflow.createAttribute(name='Notes', preset='Object')

class Action:
    def __init__(self, node):    
        for attrName, attrData in node.attrsData.items():
            (globals()[attrName]) = attrData['attr']
        music_notes = Song_Data
        data = Action.get_song_data(music_notes)
        
        waveData = [max(-32768, min(int(sample), 32767)) for sample in data]

        waveObj = WaveData(waveData, 44100, 2, 2, len(waveData))
        nodeflow.updateAttribute(node=node, name='Wave_Data', attr=waveObj)


    def get_song_data(music_notes):
        # Function to concatenate all the waves (notes)
        note_freqs = Notes() # Function that we made earlier
        music_notes = music_notes.split('-')
        music_notes = [note.split(',') for note in music_notes]
        song = [Instrument(note_freqs[note[0]], Note[note[1]].value/BPM, volume=Volume) for note in music_notes]
        song = np.concatenate(song)
        return song


class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf


class WaveData:
    def __init__(self, samples, sampleRate, numChannels, sampleWidth, nFrames):
        self.samples = samples
        self.sampleRate = sampleRate
        self.numChannels = numChannels
        self.sampleWidth = sampleWidth
        self.nFrames = nFrames

class Note(enum.Enum):
    #tsn = triplet sixteenth note
    wn   =  240
    dhn  =  180
    hn   =  120
    dqn  =   90
    qn   =   60
    den  =   45
    en   =   30
    dsn  = 22.5
    sn   =   15
    tqn  =   40
    ten  =   20
    tsn  =   10