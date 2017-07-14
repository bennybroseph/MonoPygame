import pygame

import graphics

from complex_types import Bounds, Color, Vector2
from component import Component

class Renderer(Component):
    _renderers = []

    @staticmethod
    def _render():
        for renderer in Renderer._renderers:
            if renderer.enabled:
                renderer.render()

    def __init__(self, bounds = Bounds(), name = "New Renderer"):
        assert isinstance(bounds, Bounds)

        Component.__init__(self, name)

        self.enabled = True
        self.bounds = bounds

        Renderer._renderers.append(self)

    def render(self):
        pass

class PrimitiveRenderer(Renderer):
    def __init__(self,
                 color = Color(255, 255, 255),
                 bounds = Bounds(),
                 name = "New PrimitiveRenderer"):
        assert isinstance(color, Color)

        Renderer.__init__(self, bounds, name)

        self.color = color

    def render(self):
        """Draws the object"""
        pass

class LineRenderer(PrimitiveRenderer):
    def __init__(self,
                 min = Vector2(0, 0),
                 max = Vector2(1, 1),
                 color = Color(255, 255, 255),
                 name = "New LineRenderer"):
        assert isinstance(min, Vector2) and isinstance(max, Vector2)

        PrimitiveRenderer.__init__(self, color, name = name)

        self.bounds.min = min
        self.bounds.max = max

    def render(self):
        pygame.draw.line(graphics.Graphics.screen,
                         self.color.tuple,
                         (self.bounds.min + self.transform.position).tuple,
                         (self.bounds.max + self.transform.position).tuple)