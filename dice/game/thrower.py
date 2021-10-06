import random

class Thrower:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        dice (boolean): 
        num_throws (number): 
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Thrower): an instance of Director.
        """
        self.dice = []
        self.num_throws = 0

    def can_throw(self):
        """Determines whether or not the Thrower can throw again. 
        It returns a boolean value that is true if the dice have 
        at least a five, or a one, or the num_throws is greater 
        than zero. Otherwise, it returns false.
        
        Args:
            self (Thrower): an instance of Director.
        """
        if self.num_throws > 0:
            return True
        elif 1 in self.dice:
            self.dice.clear()
            return True
        elif 5 in self.dice:
            self.dice.clear()
            return True
        else:
            return False

    def get_points(self):
        """Calculates and returns the total points for the current
        dice. Ones are worth 100 points. Fives are worth 50 points.
        
        Args:
            self (Thrower): an instance of Director.
        """
        if 1 in self.dice:
            add_one = self.dice.count(1) * 100
            add_five = self.dice.count(5) * 50
            return add_one + add_five
        elif 5 in self.dice:
            add_one = self.dice.count(1) * 100
            add_five = self.dice.count(5) * 50
            return add_one + add_five
        else:
            return 0

    def throw_dice(self):
        """Randomly generates five new dice values and adds them 
        to the dice list. It also increments the num_throws attribute 
        by one.
        
        Args:
            self (Thrower): an instance of Director.
        """
        for x in range(5):
            one = random.randint(1, 6)
            self.dice.append(one)