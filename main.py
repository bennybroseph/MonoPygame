import pygame
import sys

from pygame.locals import *

from pygame_time import Time
from graphics import Graphics, Size
from renderer import LineRenderer
from complex_types import  Vector2
from game_object import GameObject, Transform
from component import Component
from ui import Text
from matrix import Matrix

def main():
    Graphics.init(Size(1280, 720))
    Time.init()

    line = GameObject()
    line.add_component(LineRenderer(Vector2(0, 0), Vector2(10, 10)))

    fps = GameObject()
    text = fps.add_component(Text)

    # game loop
    while True:
        # check for events
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        update()
        text.text = str(int(Time.time))
        text.transform.position = text.transform.position + Vector2(1, 0)

        Graphics.draw()

def update():
    Time.update()

    Component._awake()
    Component._start()

    Component._fixed_update()

    Component._update()
    Component._late_update()

main()
