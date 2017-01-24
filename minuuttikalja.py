import pygame as pg
import sys
from time import time
from drawer import *
from timer import Timer




def main():
    pg.init()      
    surface_height = 500   
    surface_width = 1000
    main_surface = pg.display.set_mode((surface_width, surface_height))
    pg.mixer.init()
    laser_beam_sound = pg.mixer.Sound("laser_beam.wav")

    timer = Timer(10)
    timer.start_clock()
    drawer = Drawer(main_surface, timer)

    while True:
        
        drawer.draw()
        pg.display.flip()



main()