import numbers

from renderer import *

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
        label = self.font.render(self.text, 1, self.color.tuple)
        graphics.Graphics.screen.blit(label, self.bounds.center.tuple)
