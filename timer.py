import pygame as pg
from time import time

class Timer:

    start_time = 1
    round_time = 1

    def reset_clock():
        Timer.start_time = time()

    def round_time_left():
        return Timer.round_time - ((time() - Timer.start_time) % Timer.round_time)

    def get_elapsed_time():
        return time() - Timer.start_time