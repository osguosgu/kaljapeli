from timer import Timer


SIP_SIZE = 0.04
MALE_FACTOR = 0.68
FEMALE_FACTOR = 0.55
BAC_REDUCTION_PER_SECOND = 0.0016/3600

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

    def drink():
        grams_of_alcohol = SIP_SIZE*0.05*1000
        self.alcohol_consumed += grams_of_alcohol
        calculate_bac()

    def calculate_bac():
        total_bac = self.alcohol_consumed / (self.weight * self.gender_factor) * 100
        alcohol_burned =  