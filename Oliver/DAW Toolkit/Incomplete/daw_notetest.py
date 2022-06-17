import numpy as np
import enum
class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='Wave_Data', preset='Object', socket=False)
        nodeflow.createAttribute(name='Duration', preset='Float')
        nodeflow.createAttribute(name='Volume', preset='Float')
        #Note given as "NoteNumber" ex. "C4" the 4th C
        nodeflow.createAttribute(name='Note', preset='String')

class Action:
    def __init__(self, node):    
        for attrName, attrData in node.attrsData.items():
            (globals()[attrName]) = attrData['attr']

        # Get middle C frequency
        note_freqs = Instrument.get_piano_notes()
        frequency = note_freqs[Note]

        # Pure sine wave
        sine_wave = Instrument.get_sine_wave(frequency, Duration, volume=Volume)
        
        waveData = [max(-32768, min(int(sample), 32767)) for sample in sine_wave]

        waveObj = WaveData(waveData, 44100, 2, 2, len(waveData))
        nodeflow.updateAttribute(node=node, name='Wave_Data', attr=waveObj)

class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf



class Instrument:
    @staticmethod
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
        return note_freqs

    @staticmethod
    def get_sine_wave(frequency, duration=0.5, sample_rate=44100, amplitude=4096, number_channels=2, volume=1):
        t = np.linspace(0, duration, int(sample_rate*duration*number_channels)) # Time axis
        # g(f) = A sin(2πft)
        wave =  volume*amplitude*np.sin(2*np.pi*frequency*t)
        return wave

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