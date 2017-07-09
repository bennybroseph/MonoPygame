import pygame
import sys

from pygame.locals import *

from complex_types import *
from graphics import *
from pygame_object import *
from game_object import *
from component import *
from collision import *
from renderer import *

def main():
    Graphics.init(Size(1280, 720))
    
    bounds = Bounds()
    print(bounds.extents)

    player = GameObject()
    player.add_component(LineRenderer(Vector2(0, 0), Vector2(10, 10)))

    
    # game loop
    while True:
        # check for events
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        
        update()

        draw()        

def update():
    Component._awake()
    Component._start()

    Component._fixed_update()

    Component._update()
    Component._late_update()

def draw():
    Graphics.screen.fill((0, 0, 0))

    Renderer._render()
    draw_circle(0, 0, 10)

    pygame.display.update()

def draw_circle(x, y, radius = 1.0, color = (255, 255, 255)):
    pygame.draw.circle(Graphics.screen, 
                       (255, 255, 255), 
                       (int(x + (Graphics.size.w / 2)), int((Graphics.size.h / 2) - y)),
                       radius)

main()
