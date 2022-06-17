from playsound import playsound
import multiprocessing
class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='File_Name', preset='String', plug=False, attr='')
        nodeflow.createAttribute(name='Playing', preset='Bool', socket=False, plug=False, attr=False)

class Action:
    def __init__(self, node):    
        for attrName, attrData in node.attrsData.items():
            (globals()[attrName]) = attrData['attr']

        global p
        if Playing:
            p.terminate()
            nodeflow.updateAttribute(node=node, name='Playing', attr=False)
        else:
            p = multiprocessing.Process(target=playsound, args=(File_Name,))
            p.start()
            nodeflow.updateAttribute(node=node, name='Playing', attr=True)
            

class Update:
    def __init__(self, node):   
        p.join()
        nodeflow.updateAttribute(node=node, name='Playing', attr=False)
                
     
class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf
