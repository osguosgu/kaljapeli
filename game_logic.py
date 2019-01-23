from time import time
from timer import Timer
import pygame as pg
import pyttsx3 as VoiceOfKaljapeli
from threading import Thread

MINUTE_BEER = 0
OPTIMIZED_BAC = 1

class BasicLogic():


    def __init__(self, players):
        self.counter_text = ""
        self.players = players
        self.some_drinking_to_do = True
        self.laser_beam_sound = pg.mixer.Sound("laser_beam.wav")
        self.vokp = VoiceOfKaljapeli.init();

        volume = self.vokp.getProperty('volume')
        self.vokp.setProperty('volume', 2*volume)

        rate = self.vokp.getProperty('rate')
        self.vokp.setProperty('rate', rate/2)

        self.should_i_talk = True

    def get_counter_value(self, round_left):
        return int(round_left) + 1

    def players_drink(self, drinkers):
        
        for p in drinkers:
            p.drink()
        self.players.sort(key=lambda x: x.bac, reverse=True)
        self.some_drinking_to_do = False

    def get_counter_text(self):
        return self.counter_text

    def update_counter(self, round_left):
        self.counter_text = str(self.get_counter_value(round_left))
        self.some_drinking_to_do = True

class ClassicMinuteBeerMode(BasicLogic):

    def __init__(self, players):
        super().__init__(players)
        self.game_id = MINUTE_BEER
        self.game_message_text = ""

    def update_game(self):
        round_left = Timer.round_time_left()
        if (round_left <= 5):
            self.update_counter(round_left)
            self.game_message_text = ""
            if (round_left <= 2):
                self.laser_beam_sound.play()
        elif(round_left >= Timer.round_time - 5):
            self.counter_text = ""
            self.game_message_text = "Juokaa prkl"
            if self.some_drinking_to_do:
                self.players_drink(self.players)
        else:
            self.game_message_text = ""

class OptimizedBACMode(BasicLogic):

    def __init__(self, players):
        super().__init__(players)
        self.game_id = OPTIMIZED_BAC
        self.drinkers = []
        self.drinkers_backup = []
        self.show_drinkers = True

    def update_game(self):
        round_left = Timer.round_time_left()
        
        if (round_left <= 5):
            self.should_i_talk = True
            self.update_counter(round_left)
            if (round_left <= 2):
                self.laser_beam_sound.play()

        elif(round_left >= Timer.round_time - 5):
            if (self.some_drinking_to_do):
                self.counter_text = ""
                self.drinkers = self.get_drinkers()
                self.drinkers_backup = self.drinkers
                self.players_drink(self.drinkers)
            if (self.should_i_talk):
                thread = Thread(target = self.punish)
                thread.start()
                self.should_i_talk = False

    def punish(self):
        self.vokp.say(self.get_drinkers_str())
        self.vokp.runAndWait()

    def get_drinkers_str(self):
        return ' drinks '.join([player.name for player in self.drinkers]) + ' drinks'

    def get_drinkers(self):
        average_bac = self.get_average_bac()
        return [p for p in self.players if p.bac <= average_bac]


    def get_average_bac(self):
        sum = 0.0
        for p in self.players:
            sum += p.bac

        return sum / len(self.players)
