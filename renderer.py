import pygame

from complex_types import *
from graphics import *
from component import *

class Renderer(Component):
    _renderers = []

    @staticmethod
    def _render():
        for renderer in Renderer._renderers:
            if renderer.enabled:
                renderer.render()

    def __init__(self, bounds = Bounds(), tag = "", name = "New Renderer"):
        assert isinstance(bounds, Bounds)

        Component.__init__(self, tag, name)

        self.enabled = True
        self.bounds = bounds

        Renderer._renderers.append(self)

    def render(self):
        pass

class PrimitiveRenderer(Renderer):
    def __init__(self, 
                 color = (255, 255, 255), 
                 bounds = Bounds(), 
                 tag = "", 
                 name = "New PrimitiveRenderer"):
        Renderer.__init__(self, bounds, tag, name)
    
        self.color = color

    def render(self):
        """Draws the object"""
        pass

class LineRenderer(PrimitiveRenderer):
    def __init__(self, 
                 min = Vector2(0, 0),
                 max = Vector2(1, 1),
                 color = (255, 255, 255),
                 tag = "", 
                 name = "New LineRenderer"):
        assert isinstance(min, Vector2) and isinstance(max, Vector2)

        PrimitiveRenderer.__init__(self, color, tag = tag, name = name)

        self.bounds.min = min
        self.bounds.max = max

    def render(self):
        pygame.draw.line(Graphics.screen, 
                         self.color, 
                         (self.bounds.min.x, self.bounds.min.y),
                         (self.bounds.max.x, self.bounds.max.y))