from tkinter import *
import random

class GuessingGame:
    def __init__(self, master):
        self.number = random.randint(1, 100)
        self.guess = 0
        self.isCorrect = False

        self.textVar = StringVar()

        self.master = master
        master.title("Guessing Game")

        self.title = Label(master, text="Guess the number from 1 to 100")
        self.title.grid(column=0, row=0)

        self.input = Entry(master)
        self.input.grid(column=0, row=1)

        self.button = Button(master, text="Guess", command=self.getGuess)
        self.button.grid(column=0, row=2)

        self.text = Label(master, textvariable=self.textVar)
        self.text.grid(column=0, row=3)

    def getGuess(self):
        self.guess = int(self.input.get())
        self.checkGuess()

    def checkGuess(self):
        if (self.number == self.guess):
            self.textVar.set("zgadłeś!")
            self.isCorrect = True
        elif (self.number > self.guess):
            self.textVar.set('Twoja liczba jest za mała!')
            self.isCorrect = False
        elif (self.number < self.guess):
            self.textVar.set('Twoja liczba jest za duża!')
            self.isCorrect = False

root = Tk()
guess = GuessingGame(root)
root.mainloop()