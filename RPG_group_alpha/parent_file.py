import pygame
import numpy
from threading import Thread
from random import randint
import sys

numpy = numpy
pygame.init()
talkfont = pygame.font.SysFont("Arial", 48)
skillsfont = pygame.font.SysFont("Arial", 36)
objectsfont = pygame.font.SysFont("Arial", 24)

running = True

screen = pygame.display.set_mode((1600, 1080), flags=pygame.FULLSCREEN)

screenwidth = screen.get_width()  # 1600
screenheight = screen.get_height()  # 900

clock = pygame.time.Clock()
tick = 25

mousepressed = False


def mps(pixels, seconds=1):  # meters per second
    return pixels * 25 / seconds / tick


def sectoframes(sec):
    return sec * tick


class ThreadCenter:
    def __init__(self):
        self.threads = {}

    def append(self, target, args=(), name=''):
        if not name:
            name = str(target)
        newthread = Thread(target=target, args=args, name=name)
        newthread.daemon = True
        self.threads[name] = newthread
        self.threads[name].start()

    def exists(self, name):
        return name in self.threads.keys()

    def sleep(self):
        global playersmenuopened, running
        while playersmenuopened:
            if not running:
                break


threadCenter = ThreadCenter()


'''*********** world part ***********'''
actualmap = 2
mapcorners = {1: (400, 50, screenwidth-400, screenheight-50),
              2: (30, 30, screenwidth-50, screenheight-50)}

'''*********** player part ***********'''
talkingscene = False

'''*********** draw part ***********'''
todraw = {'things': [],
          'icons': {}}

'''*********** player part ***********'''
playersmenuopened = False
playerisfighting = False

'''*********** creatures part ***********'''
creaturesmap = {1: [],
                2: []}