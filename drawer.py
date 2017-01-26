import pygame as pg
from time import time
from timer import Timer

RED = (255, 0, 0)
LINE_SPACE = 10

class Drawer:

    def __init__(self, main_surface, players, game_mode):
        self.main_surface = main_surface
        self.small_font = pg.font.SysFont("monospace", 20)
        self.normal_font = pg.font.SysFont("monospace", 50)
        self.big_font = pg.font.SysFont("monospace", 100)
        self.count_label = self.big_font.render("", 1, RED)

        self.players = players
        self.game_mode = game_mode

        self.some_drinking_to_do = False

    def init_screen(self, ):
        self.main_surface.fill((0,0,0))

    def draw_game_message(self):

        text = self.game_mode.get_game_message()
        self.count_label = self.big_font.render(text, 1, RED)

        position_x = self.main_surface.get_width() / 2 - self.count_label.get_width() / 2
        position_y = self.main_surface.get_height() / 2 - self.count_label.get_height() / 2
        self.main_surface.blit(self.count_label, ( position_x , position_y))

    def draw_info_bar(self):
        minutes = int((Timer.get_elapsed_time()) / 60)
        seconds = int((Timer.get_elapsed_time()) % 60)
        round_num = int((Timer.get_elapsed_time()) / Timer.round_time)
        self.info_bar = self.normal_font.render("{}:{:0>2} - {}s game - Round {}".format(minutes, seconds, Timer.round_time, round_num), 1, RED)

        position_x = self.main_surface.get_width() / 2 - self.info_bar.get_width() / 2
        position_y = 0
        self.main_surface.blit(self.info_bar, (position_x, position_y))

    def draw_player_stats(self):

        for i, p in enumerate(self.players):
            p.calculate_bac()
            stats = self.small_font.render("{}. {: <8} {:.6f} o/oo, alc consumed: {:.2f} grams, sober in {:.2f} hours".format(i+1,p.name, p.bac, p.alcohol_consumed, p.time_left_drunk),1 ,  p.color )
            self.main_surface.blit(stats, ( LINE_SPACE, self.info_bar.get_height() + LINE_SPACE + i * stats.get_height()))

    def draw_count_down(self):
        self.init_screen()
        self.draw_game_message()



    def draw(self):
        self.init_screen()
        self.draw_info_bar()
        self.draw_player_stats()
        self.draw_game_message()


       
        