import pygame as pg
from time import time
from timer import Timer
import game_logic
from colors import *

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
        self.main_surface.fill(BLACK)

    #TODO refactor.. made in hurry
    def draw_game_message(self):
        

        if self.game_mode.game_id == game_logic.MINUTE_BEER:
            if (self.game_mode.game_message_text != ""):
                text = self.game_mode.game_message_text + self.game_mode.get_counter_text()
                self.text_label = self.big_font.render(text, 1, RED, BLACK)

                position_x = self.main_surface.get_width() / 2 - self.text_label.get_width() / 2
                position_y = self.main_surface.get_height() / 2 - self.text_label.get_height() / 2
                self.main_surface.blit(self.text_label, ( position_x , position_y))

        elif self.game_mode.game_id == game_logic.OPTIMIZED_BAC and self.game_mode.show_drinkers:
            label_rows = []
            row = []
            for d in self.game_mode.drinkers:
                if (len(row) == 4):
                    label_rows.append(list(row))
                    row = []
                text_label = self.normal_font.render(d.name, 1, d.color, BLACK)
                row.append(text_label)

            if (len(row) != 0):
                label_rows.append(row)

            rows = []
            for i, row in enumerate(label_rows):
                row_width = sum(l.get_width() + LINE_SPACE for l in row)

                position_x = self.main_surface.get_width() / 2 - row_width / 2
                position_y = self.main_surface.get_height() / 3 - i*row[0].get_height() / 2 + 1.7*i*row[0].get_height()

                for j, l in enumerate(row):
                    self.main_surface.blit(l, ( position_x , position_y))
                    position_x += l.get_width() + 2*LINE_SPACE
        
        if (self.game_mode.get_counter_text() != ""):
            text = self.game_mode.get_counter_text()
            self.count_label = self.big_font.render(text, 1, RED, BLACK)
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
        # if (self.game_mode.game_id == game_logic.OPTIMIZED_BAC and self.game_mode.show_drinkers):
        #     return
        for i, p in enumerate(self.players):
            p.calculate_bac()
            stats = self.small_font.render("{}. {: <8} {:.6f} o/oo, alc consumed: {:.2f} grams, sober in {:.2f} hours".format(i+1,p.name, p.bac, p.alcohol_consumed, p.time_left_drunk),1 ,  p.color )
            self.main_surface.blit(stats, (LINE_SPACE, self.info_bar.get_height() + LINE_SPACE + i * stats.get_height()))

    def draw_count_down(self):
        self.init_screen()
        self.draw_game_message()

    def draw(self):
        self.init_screen()
        self.draw_info_bar()
        self.draw_player_stats()
        self.draw_game_message()

       
        