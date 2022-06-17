class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='Wave_Data', preset='Object')
        nodeflow.createAttribute(name='Volume_Percent', preset='Float', attr=1.0)

class Action:
    def __init__(self, node):    
        for attrName, attrData in node.attrsData.items():
            (globals()[attrName]) = attrData['attr']
  
        waveData = [max(-32768, min(int(sample * Volume_Percent), 32767)) for sample in Wave_Data.samples]
        Wave_Data.samples = waveData
        nodeflow.updateAttribute(node=node, name='Wave_Data', attr=Wave_Data)

# class Update:
#     def __init__(self, node):    
#         waveData = [sample * node.attrsData['Volume_Percent']['attr'] for sample in node.attrsData['Wave_Data']['attr'].samples]
#         node.attrsData['Wave_Data']['attr'].samples = waveData
#         nodeflow.updateAttribute(node=node, name='Wave_Data', attr=node.attrsData['Wave_Data']['attr'])

class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf