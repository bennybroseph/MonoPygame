import pygame
import sys

from pygame.locals import *

from graphics import Graphics
from complex_types import  Vector2
from pygame_object import *
from game_object import *
from component import *
from collision import *
from ui import *

def main():
    Graphics.init(Size(1280, 720))

    clock = pygame.time.Clock()

    player = GameObject()
    player.add_component(LineRenderer(Vector2(0, 0), Vector2(10, 10)))

    fps = GameObject()
    text = fps.add_component(Text())

    # game loop
    while True:
        # check for events
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        clock.tick(60)

        update()
        text.text = str(int(clock.get_fps()))

        Graphics.draw()

def update():
    Component._awake()
    Component._start()

    Component._fixed_update()

    Component._update()
    Component._late_update()

main()
