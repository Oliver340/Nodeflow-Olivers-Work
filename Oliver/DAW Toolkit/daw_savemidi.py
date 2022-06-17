import mido
import numpy as np

class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='File_Name', preset='String', attr='')
        nodeflow.createAttribute(name='Midi_Data', preset='Object')


class Action:
    def __init__(self, node):    
        for attrName, attrData in node.attrsData.items():
            (globals()[attrName]) = attrData['attr']

        mid_new = arry2mid(Midi_Data)
        mid_new.save(File_Name)


def arry2mid(ary, tempo=500000):
    # get the difference
    new_ary = np.concatenate([np.array([[0] * 88]), np.array(ary)], axis=0)
    changes = new_ary[1:] - new_ary[:-1]
    # create a midi file with an empty track
    mid_new = mido.MidiFile()
    track = mido.MidiTrack()
    mid_new.tracks.append(track)
    track.append(mido.MetaMessage('set_tempo', tempo=tempo, time=0))
    # add difference in the empty track
    last_time = 1
    numNotes = 0
    for ch in changes:
        if set(ch) == {0}:  # no change
            last_time += 1
        else:
            on_notes = np.where(ch > 0)[0]
            on_notes_vol = ch[on_notes]
            for n, v in zip(on_notes, on_notes_vol):
                numNotes = numNotes + 1

    i = 0
    last_time = 1
    for ch in changes:
        if set(ch) == {0}:  # no change
            last_time += 1
        else:
            on_notes = np.where(ch > 0)[0]
            on_notes_vol = ch[on_notes]
            off_notes = np.where(ch < 0)[0]
            first_ = True
            for n, v in zip(on_notes, on_notes_vol):
                i = i + 1
                new_time = last_time if first_ else 0
                track.append(mido.Message('note_on', note=n + 21, velocity=v, time=new_time))
                if i == numNotes:
                    track.append(mido.Message('note_on', note=n + 21, velocity=v, time=int(new_time/3)))
                first_ = False
            for n in off_notes:
                new_time = last_time if first_ else 0
                track.append(mido.Message('note_off', note=n + 21, velocity=0, time=new_time))
                first_ = False
            last_time = 1
    
    return mid_new 
        

class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf