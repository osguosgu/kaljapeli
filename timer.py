import pygame as pg
from time import time

class Timer:

    def __init__(self, circle_time):
        self.clock = pg.time.Clock()
        self.circle_time = circle_time

    def start_clock(self):
        self.start = time()

    def time_left(self):
        return (time() - self.start) % self.circle_time