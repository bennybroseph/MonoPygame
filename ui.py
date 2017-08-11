import pygame
import numbers
import math

from graphics import Graphics, Renderer, Color
from pygame_time import Time

class Text(Renderer):
    def __init__(self,
                 text : str = "",
                 color : Color = Color(255, 255, 255),
                 font : str = "monospace",
                 size : int = 28,
                 name : str = "New Text"):
        assert(text, str)
        assert(color , Color)
        assert(font, str)
        assert(size, numbers.Number)

        Renderer.__init__(self, name = name)

        self.text = text
        self.color = color

        #TODO: Create font class
        self.size = int(size)
        self.font = pygame.font.SysFont("monospace", self.size)

    def render(self):
        # render text
        rendered_text = self.font.render(self.text, 1, self.color.tuple)

        temp_rect = rendered_text.get_rect()

        rendered_text = pygame.transform.smoothscale(rendered_text, (100, 100))
        rendered_text = pygame.transform.rotate(rendered_text,
                                                math.cos(Time.time) * (180 / math.pi))

        rect = rendered_text.get_rect()

        position = self.bounds.center + self.transform.position

        rect.center = (temp_rect.center[0] + position.x,
                       temp_rect.center[1] + position.y)

        Graphics.screen.blit(rendered_text, rect)
