import pygame

from complex_types import *

class Graphics(object):
    size = Size(0, 0)

    screen = None

    @staticmethod
    def init(newSize = Size(640, 460), caption = "Pygame"):
        Graphics.size = newSize

        pygame.init()
    
        Graphics.screen = \
            pygame.display.set_mode((int(Graphics.size.w), int(Graphics.size.h)))

        pygame.display.set_caption(caption)


