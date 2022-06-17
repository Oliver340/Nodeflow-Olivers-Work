from .polysynth import *

class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='File_Name', preset='String', attr='')
        nodeflow.createAttribute(name='Oscillator', preset='String', attr='sine')

class Action:
    def __init__(self, node):
        self.thread(Run, [node])

    def thread(self, target, args):
        from threading import Thread
        thread = Thread(target=target, args=args)
        thread.daemon = True
        thread.start()

class Run:
    def __init__(self, node):
        synth = PolySynth()
        if (node.attrsData['Oscillator']['attr'] == 'sine'):
            osc = get_sin_oscillator
        elif (node.attrsData['Oscillator']['attr'] == 'square'):
            osc = get_square_oscillator
        elif (node.attrsData['Oscillator']['attr'] == 'saw'):
            osc = get_saw_oscillator
        elif (node.attrsData['Oscillator']['attr'] == 'triangle'):
            osc = get_triangle_oscillator

        synth.rec_play(osc_function=osc, file_name=node.attrsData['File_Name']['attr'])

class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf