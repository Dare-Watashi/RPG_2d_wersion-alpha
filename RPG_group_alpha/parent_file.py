import pygame
import numpy
from threading import Thread
import sys
import winsound

numpy = numpy
pygame.init()
talkfont = pygame.font.SysFont("Arial", 48)
objectsfont = pygame.font.SysFont("Arial", 24)

running = True

screen = pygame.display.set_mode((1600, 1080), flags=pygame.FULLSCREEN)

screenwidth = screen.get_width()  # 1600
screenheight = screen.get_height()  # 900

clock = pygame.time.Clock()
tick = 25


def mps(pixels, seconds):  # meters per second
    return pixels / seconds / tick


def sectoframes(sec):
    return sec * tick


class ThreadCenter:
    def __init__(self):
        self.threads = []

        '''self.emergencythread = Thread(target=self.emergency, daemon=True)
        self.emergencythread.start()

        def emergency(self):
        global running
        while True:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False
                exit(0)'''

    def append(self, target, args=()):
        newthread = Thread(target=target, args=args)
        newthread.daemon = True
        self.threads.append(newthread)
        self.threads[-1].start()


threadCenter = ThreadCenter()


'''*********** world part ***********'''
actualmap = 1
mapcorners = {1: (400, 50, screenwidth-400, screenheight-50),
              2: (25, 25, screenwidth-50, screenheight-50)}
