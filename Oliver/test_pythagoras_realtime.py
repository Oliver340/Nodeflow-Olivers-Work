class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='a', preset='Float', plug=False)
        nodeflow.createAttribute(name='b', preset='Float', plug=False)
        nodeflow.createAttribute(name='c', preset='Float', socket=False)

class Update:
    def __init__(self, node):
        # Performs c=sqrt(a^2+b^2)
        nodeflow.updateAttribute(node=node, name='c', attr=(node.attrsData['a']['attr']**2 + node.attrsData['b']['attr']**2)**0.5)

class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf