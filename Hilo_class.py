import random
from select import select

class Hilo:
    """ Face cards create a game of guessing whether the next card will be higher or lower in value than the previously drawn card."""
    ##list of cards 
    def __init__(self):
        self.cards_list = []
        
    def create_cards(self):
            for i in range(4):
                for i in range(1,14):
                    self.cards_list.append(i)

    def random_select(self):
        i = random.choice(self.cards_list) 
        self.cards_list.remove(i)
        return i
