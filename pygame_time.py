import pygame

class Time(object):
    _clock = pygame.time.Clock()

    refreshRate = 60
    timeScale = 1.0

    time = 0.0
    deltaTime = 0.0

    @staticmethod
    def init(refreshRate = 60, timeScale = 1):
        Time.refreshRate = int(refreshRate)
        Time.timeScale = float(timeScale)

        Time.deltaTime = float(Time._clock.get_time())

    @staticmethod
    def update():
        Time._clock.tick(Time.refreshRate * Time.timeScale)

        Time.deltaTime = float(Time._clock.get_time()) / 1000.0
        Time.time += Time.deltaTime
