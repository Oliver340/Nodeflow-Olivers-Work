import pyaudio
import struct
import threading
# pip install pipwin
# pipwin install pyaudio
class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='Wave_Data', preset='Object')
        nodeflow.createAttribute(name='Playing', preset='Bool', socket=False, plug=False, attr=False)

class Action:
    def __init__(self, node):    
        for attrName, attrData in node.attrsData.items():
            (globals()[attrName]) = attrData['attr']

        global p
        
        if Playing:
            stream.stop_stream()    # "Stop Audio Recording
            # stream.close()          # "Close Audio Recording
            p.terminate()           # "Audio System Close
            nodeflow.updateAttribute(node=node, name='Playing', attr=False)
        else:
            p = threading.Thread(target=Action.playAudio)
            p.start()
            nodeflow.updateAttribute(node=node, name='Playing', attr=True)


    def playAudio():
        global stream
        audio = pyaudio.PyAudio()
        stream = audio.open(format = audio.get_format_from_width(Wave_Data.sampleWidth),
                        channels = Wave_Data.numChannels,
                        rate = Wave_Data.sampleRate,
                        output = True)
        # from samples to the new binary file
        new_binary_data = struct.pack('{}h'.format(len(Wave_Data.samples)), *Wave_Data.samples)
        stream.write(new_binary_data)
        stream.close()


class Update:
    def __init__(self, node):   
        p.join()
        nodeflow.updateAttribute(node=node, name='Playing', attr=False)
                
     
class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf
