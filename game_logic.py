from time import time
from timer import Timer

MINUTE_BEER = 0
OPTIMIZED_BAC = 1

class BasicLogic():


    def __init__(self, players):
        self.counter_text = ""
        self.players = players
        self.some_drinking_to_do = True

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
        print(round_left)
        if (round_left <= 5):
            self.update_counter(round_left)
            self.game_message_text = ""
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
        self.show_drinkers = False

    def update_game(self):
        round_left = Timer.round_time_left()
        if (round_left <= 5):
            self.update_counter(round_left)
            self.show_drinkers = False

        elif(round_left >= Timer.round_time - 5):
            if self.some_drinking_to_do:
                self.counter_text = ""
                self.drinkers = self.get_drinkers()
                self.players_drink(self.drinkers)
                self.show_drinkers = True
           

    def get_drinkers(self):
        average_bac = self.get_average_bac()
        return [p for p in self.players if p.bac <= average_bac]


    def get_average_bac(self):
        sum = 0.0
        for p in self.players:
            sum += p.bac

        return sum / len(self.players)
