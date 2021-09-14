import random

class Guess:
    def __init__(self):
        self.number = number
        self.guess = guess

    def

    def checkGuess(self):
        if (self.number == self.guess):
            print('zgadłeś!')
            return True
        elif (self.number > self.guess):
            print('Twoja liczba jest za mała!')
            return False
        elif (self.number < self.guess):
            print('Twoja liczba jest za duża!')
            return False

