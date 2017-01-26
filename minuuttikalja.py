import pygame as pg
import sys
from time import time
from drawer import *
from timer import Timer
from player import Player
from game_logic import *
import input_screen



def main():
    pg.init()      
    surface_height = 500   
    surface_width = 1000
    main_surface = pg.display.set_mode((surface_width, surface_height))

    pg.mixer.init()
    laser_beam_sound = pg.mixer.Sound("laser_beam.wav")

    oskari = Player('Oskari', 'male', 82000, 0.05, (0,255,0))
    niko = Player('Niko', 'male', 64500, 0.02, (200,0,100))
    nikoliina = Player('Nikoliina', 'female', 64500, 0.02, (200,0,100))
    petsku = Player('Petsku', 'male', 90000, 0.1, (240,100,20))

    players = [niko, oskari, petsku, nikoliina]

    game_mode = ClassicMinuteBeerMode(players)

    drawer = Drawer(main_surface, players, game_mode)

    Timer.reset_clock()
    Timer.round_time = 5
    #Count down loop
    while Timer.get_elapsed_time() < Timer.round_time:
        game_mode.update_game()
        drawer.draw_count_down()
        pg.display.flip()

    Timer.reset_clock()
    Timer.round_time = 60
    #Main loop
    while True:
        game_mode.update_game()
        drawer.draw()
        pg.display.flip()



main()