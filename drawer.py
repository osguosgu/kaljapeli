import pygame as pg
from time import time
RED = (255, 0, 0)
LINE_SPACE = 10
class Drawer:

    def __init__(self, main_surface, timer, players):
        self.main_surface = main_surface
        self.small_font = pg.font.SysFont("monospace", 20)
        self.normal_font = pg.font.SysFont("monospace", 50)
        self.big_font = pg.font.SysFont("monospace", 100)
        self.count_label = self.big_font.render("", 1, RED)
        self.timer = timer
        self.players = players

    def init_screen(self, ):
        self.main_surface.fill((0,0,0))

    def draw_count_down(self):
        time_left = self.timer.time_left()
        if (time_left < 5):
            self.count_label = self.big_font.render("Juokaa prkl", 1, RED)
        elif (time_left > self.timer.circle_time-1):
            self.count_label = self.big_font.render("1", 1, RED)
            # laser_beam_sound.play()
            
        elif (time_left > self.timer.circle_time-2):
            self.count_label = self.big_font.render("2", 1, RED)
            # laser_beam_sound.play()
            
        elif (time_left > self.timer.circle_time-3):
            self.count_label = self.big_font.render("3", 1, RED)
            # laser_beam_sound.play()
            
        elif (time_left > self.timer.circle_time-4):
            self.count_label = self.big_font.render("4", 1, RED)
            
        elif (time_left > self.timer.circle_time-5):
            self.count_label = self.big_font.render("5", 1, RED)

        self.main_surface.blit(self.count_label, (self.main_surface.get_width() / 2 - self.count_label.get_width() / 2 , self.main_surface.get_height() / 2 - self.count_label.get_height() / 2))

    def draw_info_bar(self):
        self.info_bar = self.normal_font.render("{}:{} - {}s game - Round {}".format(int((time() - self.timer.start) / 60), int((time() - self.timer.start) % 60), self.timer.circle_time, int((time() - self.timer.start) / self.timer.circle_time)), 1, RED)
        self.main_surface.blit(info_bar, (self.main_surface.get_width() / 2 - info_bar.get_width() / 2,0))

    def draw_player_stats(self):
        for p in self.players:
            stats = self.normal_font.render("{}:{} - {}s game - Round {}".format(), p.get_color())
            self.main_surface.blit(stats, (self.info_bar.get_height() + LINE_SPACE,0))


    def draw(self):
        self.init_screen()
        self.draw_info_bar()
        self.draw_player_stats()
        self.draw_count_down()


       
        