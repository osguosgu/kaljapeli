import pygame as pg
from time import time

class Timer:

    start_time = 1
    circle_time = 1

    def start_clock():
        Timer.start_time = time()

    def time_left():
        return (time() - Timer.start_time) % Timer.circle_time