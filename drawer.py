import pygame as pg
from time import time
from timer import Timer
RED = (255, 0, 0)
LINE_SPACE = 10

class Drawer:

    def __init__(self, main_surface, players):
        self.main_surface = main_surface
        self.small_font = pg.font.SysFont("monospace", 20)
        self.normal_font = pg.font.SysFont("monospace", 50)
        self.big_font = pg.font.SysFont("monospace", 100)
        self.count_label = self.big_font.render("", 1, RED)

        self.players = players
        self.some_drinking_to_do = False

    def init_screen(self, ):
        self.main_surface.fill((0,0,0))

    def draw_count_down(self):
        time_left = Timer.time_left()
        if (time_left < 5):
            self.count_label = self.big_font.render("Juokaa prkl", 1, RED)

            if self.some_drinking_to_do:
                for p in self.players:
                    p.drink()
                self.players.sort(key=lambda x: x.bac, reverse=True)
                self.some_drinking_to_do = False

        elif (time_left > Timer.circle_time-1):
            self.count_label = self.big_font.render("1", 1, RED)
            self.some_drinking_to_do = True
            # laser_beam_sound.play()
            
        elif (time_left > Timer.circle_time-2):
            self.count_label = self.big_font.render("2", 1, RED)
            # laser_beam_sound.play()
            
        elif (time_left > Timer.circle_time-3):
            self.count_label = self.big_font.render("3", 1, RED)
            # laser_beam_sound.play()
            
        elif (time_left > Timer.circle_time-4):
            self.count_label = self.big_font.render("4", 1, RED)
            
        elif (time_left > Timer.circle_time-5):
            self.count_label = self.big_font.render("5", 1, RED)

        self.main_surface.blit(self.count_label, (self.main_surface.get_width() / 2 - self.count_label.get_width() / 2 , self.main_surface.get_height() / 2 - self.count_label.get_height() / 2))

    def draw_info_bar(self):
        minutes = int((time() - Timer.start_time) / 60)
        seconds = int((time() - Timer.start_time) % 60)
        round_num = int((time() - Timer.start_time) / Timer.circle_time)
        self.info_bar = self.normal_font.render("{}:{:0>2} - {}s game - Round {}".format(minutes, seconds, Timer.circle_time, round_num), 1, RED)
        self.main_surface.blit(self.info_bar, (self.main_surface.get_width() / 2 - self.info_bar.get_width() / 2,0))

    def draw_player_stats(self):

        for i, p in enumerate(self.players):
            p.calculate_bac()
            stats = self.small_font.render("{}. {}: {:.6f} o/oo, alc consumed: {:.2f} grams, sober in {:.2f} hours".format(i+1,p.name, p.bac, p.alcohol_consumed, p.time_left_drunk),1 ,  p.color )
            self.main_surface.blit(stats, ( 0, self.info_bar.get_height() + LINE_SPACE + i * stats.get_height()))


    def draw(self):
        self.init_screen()
        self.draw_info_bar()
        self.draw_player_stats()
        self.draw_count_down()


       
        