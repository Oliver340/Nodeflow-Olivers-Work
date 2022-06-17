class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='a', preset='Float', plug=False)
        nodeflow.createAttribute(name='b', preset='Float', plug=False)
        nodeflow.createAttribute(name='c', preset='Float', socket=False)

class Action:
    def __init__(self, node):
        for attrName, attrData in node.attrsData.items():
            (globals()[attrName]) = attrData['attr']

        # Performs c=sqrt(a^2+b^2)
        nodeflow.updateAttribute(node=node, name='c', attr=(a**2 + b**2)**0.5)

class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf