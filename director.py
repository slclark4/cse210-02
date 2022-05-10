from Hilo_class import Hilo
class Director:
    """The person who is playing Hilo decides whether to put all their points on the line or not by choosing to play and guess higher or lower."""
    def __init__(self):
        self.hilo= Hilo() 
        self.card_list = self.hilo.create_cards()
        self.guess =""
        self.previous_card =  self.hilo.random_select()
        self.is_playing = True
        self.total_score = 300
###

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        playing = input("Would you like to play?\n:Y/N\n:")
        if playing.lower() =="n":
            self.is_playing = False
        else:
            print(f"The previous card is {self.previous_card}")
            self.guess= input("Do you think the next card will be Higher or lower?\n:H/L \n:")
#        self.is_playing = (roll_dice == "y")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        
        if not self.is_playing:
            return 
        
        card = self.hilo.random_select()

        print(f"The previous card was {self.previous_card}\nThe new card is {card}")
        if card > self.previous_card:
            if self.guess.lower() in "h":
                print("You guessed correct and earned 100 points!")
                self.total_score += 100
            else:
                print("Sorry you guessed incorrectly and lose 75 points...")
                self.total_score -= 75
        elif card < self.previous_card:
            if self.guess.lower() in "l":
                print("You guessed correct and earned 100 points!")
                self.total_score += 100
            else:
                print("Sorry you guessed incorrectly and lose 75 points...")
                self.total_score -= 75
        else:
            print("The cards were the same you lose 75 points...")
            self.total_score -= 75
        self.previous_card = card

    def do_outputs(self):
        """Change this function to randomly select a card from the hilo list and determine if the card is higher or lower than the guess.
        """
        if not self.is_playing:
            return
        
        
        

        print(f"Your total score is {self.total_score}")
        self.is_playing == (self.total_score > 0)