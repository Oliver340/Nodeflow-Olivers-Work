import pygame

class Node:
    def __init__(self, node):
        nodeflow.createAttribute(name='File_Name', preset='String', attr='')
        nodeflow.createAttribute(name='Volume_Percent', preset='Float', attr=1.0)

class Action:
    def __init__(self, node):
        for attrName, attrData in node.attrsData.items():
            (globals()[attrName]) = attrData['attr']
        self.thread(Run, [node])

    def thread(self, target, args):
        from threading import Thread
        thread = Thread(target=target, args=args)
        thread.daemon = True
        thread.start()

    
class Run:
    def __init__(self, node):
        # pick a midi music file you have ...
        # (if not in working folder use full path)
        music_file = File_Name

        freq = 44100    # audio CD quality
        bitsize = -16   # unsigned 16 bit
        channels = 2    # 1 is mono, 2 is stereo
        buffer = 1024    # number of samples
        pygame.mixer.init(freq, bitsize, channels, buffer)

        # optional volume 0 to 1.0
        pygame.mixer.music.set_volume(Volume_Percent)

        try:
            Run.play_music(music_file)
        except KeyboardInterrupt:
            # if user hits Ctrl/C then exit
            # (works only in console mode)
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.stop()
            raise SystemExit
            
    
    def play_music(music_file):
        clock = pygame.time.Clock()
        try:
            pygame.mixer.music.load(music_file)
            print("Music file %s loaded!" % music_file)
        except pygame.error:
            print("File %s not found! (%s)" % (music_file, pygame.get_error()))
            return
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            # check if playback has finished
            clock.tick(30)

class Setup:
    def __init__(self, nf, n, s):
        global nodeflow
        nodeflow = nf


