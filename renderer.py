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
                 color = Color(),
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
                 width = 1,
                 color = Color(),
                 name = "New LineRenderer"):
        assert isinstance(min, Vector2) and isinstance(max, Vector2)

        PrimitiveRenderer.__init__(self, color, name = name)

        self.bounds.min = min
        self.bounds.max = max

        self.width = width

    def render(self):
        pygame.draw.line(graphics.Graphics.screen,
                         self.color.tuple,
                         self.bounds.min.tuple,
                         self.bounds.max.tuple,
                         self.width)

class LinesRenderer(PrimitiveRenderer):
    def __init__(self,
                 lines = [Vector2(0, 0), Vector2(1, 1)],
                 width = 1,
                 color = Color(),
                 name = "New LinesRenderer"):
        assert isinstance(lines, list)
        assert isinstance(lines[0], Vector2)

        PrimitiveRenderer.__init__(self, color, name = name)

        self.lines = lines
        self.width = width

    def render(self):
        pygame.draw.lines(graphics.Graphics.screen,
                          self.color.tuple,
                          False,
                          self.lines,
                          self.width)
