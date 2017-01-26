from time import time
from timer import Timer


class BasicLogic():


    def __init__(self, players):
        self.game_message_text = ""
        self.players = players

    def get_counter_value(self, round_left):
        return int(round_left) + 1
    #     if (time_left < 5):
    #         self.count_label = self.big_font.render("Juokaa prkl", 1, RED)

    #         if self.some_drinking_to_do:
    #             for p in self.players:
    #                 p.drink()
    #             self.players.sort(key=lambda x: x.bac, reverse=True)
    #             self.some_drinking_to_do = False

    #     elif (time_left > Timer.round_time-1):
    #         self.count_label = self.big_font.render("1", 1, RED)
    #         self.some_drinking_to_do = True
    #         # laser_beam_sound.play()
            
    #     elif (time_left > Timer.round_time-2):
    #         self.count_label = self.big_font.render("2", 1, RED)
    #         # laser_beam_sound.play()
            
    #     elif (time_left > Timer.round_time-3):
    #         self.count_label = self.big_font.render("3", 1, RED)
    #         # laser_beam_sound.play()
            
    #     elif (time_left > Timer.round_time-4):
    #         self.count_label = self.big_font.render("4", 1, RED)
            
    #     elif (time_left > Timer.round_time-5):
    # self.count_label = self.big_font.render("5", 1, RED)


class ClassicMinuteBeerMode(BasicLogic):

    def __init__(self, players):
        super().__init__(players)
        self._some_drinking_to_do = True

    def update_game(self):
        round_left = Timer.round_time_left()

        if (round_left <= 5):
            self.game_message_text = str(self.get_counter_value(round_left))
            self._some_drinking_to_do = True
        elif(round_left >= Timer.round_time - 5):
            self.game_message_text = "Juokaa prkl"
            self.players_drink()
        else:
            self.game_message_text = ""


    def players_drink(self):
        if self._some_drinking_to_do:
            for p in self.players:
                p.drink()
            self.players.sort(key=lambda x: x.bac, reverse=True)
            self._some_drinking_to_do = False

    def get_game_message(self):
        return self.game_message_text


# class optimized_bac_mode(BasicLogic):

#     def __init__(self, players):
#         super().__init__(players)
#         self._some_drinking_to_do = {p.id : True for p in players}


#     def update_game(self):
#         round_left = Timer.round_time_left()

#         if (round_left <= 5):
#             self.game_message_text = str(self.get_counter_value(round_left))
#             self.update_drinkers()
#         elif(round_left >= Timer.round_time - 5):
#             self.game_message_text = "Juokaa prkl"
#             self.players_drink()
#         else:
#             self.game_message_text = ""

