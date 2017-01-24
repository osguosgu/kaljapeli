import pygame as pg
from time import time



def main():
    pg.init()      
    surface_height = 500   
    surface_width = 1000    
    clock = pg.time.Clock()
    circle_time = 10
    main_surface = pg.display.set_mode((surface_width, surface_height))
    pg.mixer.init()
    laser_beam_sound = pg.mixer.Sound("laser_beam.wav")
    start = time()
    while True:
        time_left = (time() - start) % circle_time
        myfont = pg.font.SysFont("monospace", 100)
        myfont2 = pg.font.SysFont("monospace", 20)
        label = myfont.render("", 1, (255, 0, 0))
        label2 = myfont.render("{}:{}".format(int((time() - start) / circle_time), int((time() - start) % circle_time)), 1, (255, 0, 0))

        if (time_left < 5):
            label = myfont.render("Juokaa homot", 1, (255, 0, 0))   
        elif (time_left > circle_time-1):
            label = myfont.render("1", 1, (255, 0, 0))
            laser_beam_sound.play()
            
        elif (time_left > circle_time-2):
            label = myfont.render("2", 1, (255, 0, 0))
            laser_beam_sound.play()
            
        elif (time_left > circle_time-3):
            label = myfont.render("3", 1, (255, 0, 0))
            laser_beam_sound.play()
            
        elif (time_left > circle_time-4):
            label = myfont.render("4", 1, (255, 0, 0))
            
        elif (time_left > circle_time-5):
            label = myfont.render("5", 1, (255, 0, 0))
        
            
        print(time_left)
        main_surface.fill((0,0,0))
        main_surface.blit(label, (surface_width / 2 - label.get_width() / 2 , surface_height / 2 - label.get_height() / 2))
        main_surface.blit(label2, (0,0))
        pg.display.flip()



main()