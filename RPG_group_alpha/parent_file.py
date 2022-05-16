import pygame
import time
import numpy

numpy = numpy
pygame = pygame
pygame.init()
running = True

screen = pygame.display.set_mode((800, 800), flags=pygame.FULLSCREEN)

time.sleep(3)

screen_width = screen.get_width()  # 1152
screen_height = screen.get_height()  # 864

tick = 25


def sec(pixels, seconds):
    return pixels / tick / seconds
