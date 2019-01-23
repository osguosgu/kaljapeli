import pygame as pg
import sys
from time import time
from drawer import *
from timer import Timer
from input_screen import *
from player import *
from game_logic import *


def main():

    pg.init()      
    surface_height = 900   
    surface_width = 1500
    main_surface = pg.display.set_mode((surface_width, surface_height))


    players = []
    more_players = True
    while more_players:
        ask = "Press Enter for new player, or anything else to start (korjaa tää antsa)"
        fontobject = pg.font.Font(None,46)
        main_surface.blit(fontobject.render(ask, 1, (255,255,255)), (main_surface.get_width()/2-fontobject.size(ask)[0]/2, main_surface.get_height()/2-75))
        pygame.display.flip()

        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.key == K_RETURN:
                    main_surface.fill((0, 0, 0))
                    players.append(addPlayer(main_surface))
                else:
                    more_players = False
    
            
    pg.mixer.init()

    # oskari = Player('Oskari', 'male', 82000, 0.05, (0,255,0))
    # niko = Player('Niko', 'male', 64500, 0.02, (200,0,100))
    # nikolina = Player('Nikolina', 'female', 64500, 0.02, (200,50,100))
    # petsku = Player('Petsku', 'male', 90000, 0.053, (240,100,20))
    # otto = Player('Otto', 'male', 70000, 0.1, (0,255,20))
    # late = Player('Late', 'male', 97000, 0.053, GREEN)
    
    # camilla = Player('Camilla', 'female', 70000, 0.053, BLUE)
    # roosa = Player('Roosa' , 'female', 70000, 0.053, PURPLE)

    #testi = Player(name, gender, weight(grams), sip/drink size (liters), alco%, color(rbg)  )
    sale = Player('Z4guero', 'male', 85000, 0.04 , 0.05, PURPLE )
    rihis = Player('Rihis', 'male', 85000, 0.04, 0.049, RED, 1 )
    antsa = Player('Antsa', 'male', 82000, 0.04, 0.05, PINK )
    sanna = Player('Sanna', 'female',59000, 0.04, 0.05, BLUE)
    kalmis = Player('Kalmis', 'male', 85000, 0.04, 0.05, PURPLE)
    ilnord = Player('ilnord', 'male', 75000, 0.04, 0.05, PINK)
    tuktuk = Player('tuktuk', 'male', 73000, 0.04, 0.05, GREEN)
    otto = Player('Otto', 'male', 70000, 0.04 ,0.05, WHITE)
    elsi = Player('elsi', 'male', 64000, 0.04, 0.05, LIGHT_BLUE)
    petsku = Player('Petsku', 'male', 90000,0.04, 0.05, ORANGE)
    mikko = Player('Mikko', 'male', 80000, 0.04, 0.05, BLUE)
    kirsi = Player('Kirsi', 'female', 69000, 0.04, 0.05, GREY)
    nikke = Player('Nikke', 'male', 65000, 0.04, 0.053, GREEN)
    liina = Player('Liina', 'female', 60000, 0.04, 0.05, PINK )


    players.extend([sale,rihis,antsa, sanna,kalmis,ilnord,tuktuk,otto,elsi,petsku,mikko,kirsi,nikke])

    #game_mode = ClassicMinuteBeerMode(players)
    game_mode = OptimizedBACMode(players)

    drawer = Drawer(main_surface, players, game_mode)

    Timer.reset_clock()
    Timer.round_time = 5
    #Count down loop
    while Timer.get_elapsed_time() < Timer.round_time:
        game_mode.update_game()
        drawer.draw_count_down()
        pg.display.flip()

    Timer.reset_clock()
    Timer.round_time = 40
    #Main loop
    while True:
        for evt in pygame.event.get():
            if game_mode.game_id == OPTIMIZED_BAC and evt.type == KEYDOWN:
                if len(game_mode.drinkers) != 0:
                    game_mode.drinkers = []
                else:
                    game_mode.drinkers = game_mode.drinkers_backup
        pygame.event.get()
        game_mode.update_game()
        drawer.draw()
        pg.display.flip()



main()