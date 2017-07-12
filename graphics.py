import pygame

from renderer import Renderer
from complex_types import Size, Color

class Graphics(object):
    screen = None

    size = Size()
    fillcolor = Color()

    @staticmethod
    def init(size = Size(640, 460),
             caption = "Pygame",
             fillcolor = Color(0, 0, 0)):
        assert(size, Size)
        assert(caption, str)
        assert(fillcolor, Color)

        Graphics.size = size
        Graphics.fillcolor = fillcolor

        pygame.init()

        Graphics.screen = pygame.display.set_mode((int(Graphics.size.w),
                                                   int(Graphics.size.h)))

        pygame.display.set_caption(caption)

    @staticmethod
    def draw():
        Graphics.screen.fill(Graphics.fillcolor.tuple)

        Renderer._render()

        pygame.display.update()

