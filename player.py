
from time import time
from timer import Timer


SIP_SIZE = 0.04
MALE_FACTOR = 0.68
FEMALE_FACTOR = 0.55
BAC_REDUCTION_PER_SECOND = 0.016/3600

class Player:

    def __init__(self, name, gender, weight, drink_alc_perc=0.05, color=(255,255,255)):
        self.name = name
        self.gender = gender
        self.weight = weight
        self.drink_alc_perc = drink_alc_perc
        self.color = color
        self.alcohol_consumed = 0
        self.bac = 0    
        self.gender = gender  
        self.gender_factor = MALE_FACTOR if gender == 'male' else FEMALE_FACTOR
        self.time_left_drunk = 0
    def drink(self):
        grams_of_alcohol = SIP_SIZE*(self.drink_alc_perc*1000)
        self.alcohol_consumed += grams_of_alcohol
        self.calculate_bac()

    def calculate_bac(self):
        total_bac = self.alcohol_consumed / (self.weight * self.gender_factor) * 100
        alcohol_burned = (time() - Timer.start_time) * BAC_REDUCTION_PER_SECOND
        real_bac = total_bac - alcohol_burned
        self.bac = real_bac if real_bac > 0 else 0

        self.time_left_drunk = self.bac / BAC_REDUCTION_PER_SECOND / 3600