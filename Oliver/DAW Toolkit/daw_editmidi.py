import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='Midi_Data', preset='Object')

class Action:
    def __init__(self, node):    
        for attrName, attrData in node.attrsData.items():
            (globals()[attrName]) = attrData['attr']

        result_array = Midi_Data
        
        octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
        keys = np.array([x+str(y) for y in range(0,9) for x in octave])
        # Trim to standard 88 keys
        start = np.where(keys == 'A0')[0][0]
        end = np.where(keys == 'C8')[0][0]
        keys = keys[start:end+1]

        plt.ion()
        fig, ax = plt.subplots()
        for axis in [ax.xaxis, ax.yaxis]:
            axis.set_major_locator(ticker.MaxNLocator(integer=True))
        plt.plot(range(result_array.shape[0]), np.multiply(np.where(result_array>0, 1, 0), range(1, 89)), marker='.', markersize=1, linestyle='')
        plt.ylim(0, 88)

        nodeflow.updateAttribute(node=node, name='Midi_Data', attr=result_array)


        global x1, y1
        def onclick(event):
            global x1, y1
            x1, y1 = event.xdata, event.ydata
            if event.button == 2:
                i = round(x1)
                while i - 1 >= 0 and result_array[i - 1][round(y1) - 1] != 0:
                        i = i - 1
                while i < len(result_array) and result_array[i][round(y1) - 1] != 0:
                    result_array[i][round(y1) - 1] = 0
                    i = i + 1
                nodeflow.updateAttribute(node=node, name='Midi_Data', attr=result_array)
                plt.clf()
                plt.ylim(0, 88)
                plt.plot(range(result_array.shape[0]), np.multiply(np.where(result_array>0, 1, 0), range(1, 89)), marker='.', markersize=1, linestyle='')

        def onrelease(event):
            global x1, y1
            if event.button == 3:
                x2, y2 = event.xdata, event.ydata
                for i in range(round(x1), round(x2) + 1):
                    if i < 0:
                        i = 0
                    if i >= len(result_array):
                        i = len(result_array) - 1
                    result_array[i][round(y1) - 1] = 127
                nodeflow.updateAttribute(node=node, name='Midi_Data', attr=result_array)
                plt.clf()
                plt.ylim(0, 88)
                plt.plot(range(result_array.shape[0]), np.multiply(np.where(result_array>0, 1, 0), range(1, 89)), marker='.', markersize=1, linestyle='')

        fig.canvas.mpl_connect('button_press_event', onclick)
        fig.canvas.mpl_connect('button_release_event', onrelease)
        
        plt.show()
    

class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf