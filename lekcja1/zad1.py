import random

class Guess:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.guess = 0
        self.isCorrect = False

    def getGuess(self):
        while(self.isCorrect == False):
            self.guess = int(input("Zgadnij liczbe od 1 do 100: "))
            self.checkGuess()

    def checkGuess(self):
        if (self.number == self.guess):
            print('zgadłeś!')
            self.isCorrect = True
        elif (self.number > self.guess):
            print('Twoja liczba jest za mała!')
            self.isCorrect = False
        elif (self.number < self.guess):
            print('Twoja liczba jest za duża!')
            self.isCorrect = False

guess = Guess()
guess.getGuess()