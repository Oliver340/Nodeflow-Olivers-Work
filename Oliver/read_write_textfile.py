class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='File_Name', preset='String', plug=False, attr='')
        nodeflow.createAttribute(name='Input', preset='String', plug=False, attr='')
        nodeflow.createAttribute(name='File_Data', preset='String', socket=False, attr='')

class Action:
    def __init__(self, node):       
        for attrName, attrData in node.attrsData.items():
            (globals()[attrName]) = attrData['attr']

        # Read and write over a file and don't create a new one if File_Name doesn't exist
        myFile = open(File_Name, "r+")
        if Input != "":
            myFile.truncate(0)
            myFile.write(Input)

        myFile.seek(0)
        # Update output with the text file data      
        nodeflow.updateAttribute(node=node, name='File_Data', attr=myFile.read())
        myFile.seek(0)
        print(myFile.read())

        myFile.close()

class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf