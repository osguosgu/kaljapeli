
from time import time
from timer import Timer
from input_screen import *

MALE_FACTOR = 0.68
FEMALE_FACTOR = 0.55
BAC_REDUCTION_PER_SECOND = 0.016/3600

class Player:
    number_of_players = 0

    def __init__(self, name, gender, weight, sip_size=0.04, drink_alc_perc=0.05, color=(255,255,255), initial_beers=0):
        self.id = Player.number_of_players
        self.name = name
        self.gender = gender
        self.weight = weight
        self.sip_size = sip_size
        self.drink_alc_perc = drink_alc_perc
        self.color = color
        self.alcohol_consumed = 0
        self.bac = 0    
        self.gender = gender  
        self.gender_factor = MALE_FACTOR if gender == 'male' else FEMALE_FACTOR
        self.time_left_drunk = 0

        Player.number_of_players += 1

        for beer in range(initial_beers):
            self.drink()


    def drink(self):
        grams_of_alcohol = self.sip_size*(self.drink_alc_perc*1000)
        self.alcohol_consumed += grams_of_alcohol
        self.calculate_bac()

    def calculate_bac(self):
        total_bac = self.alcohol_consumed / (self.weight * self.gender_factor) * 100 * 10
        alcohol_burned = (time() - Timer.start_time) * BAC_REDUCTION_PER_SECOND
        real_bac = total_bac - alcohol_burned
        self.bac = real_bac if real_bac > 0 else 0

        self.time_left_drunk = self.bac / BAC_REDUCTION_PER_SECOND / 3600


def addPlayer(disp):
    name = Input_field(disp, "Name", False)
    gender = Select_field(disp, "Gender", ["male","female"])
    weight = int(Input_field(disp, "Weight in kg", True)) * 1000
    disp.fill((0, 0, 0))
    return Player(name,gender,weight)