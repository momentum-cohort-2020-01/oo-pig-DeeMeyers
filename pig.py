from random import randint

dieNumbers = [1,2,3,4,5,6]
maxScore = 100
startScore = 0

class Game:
    def __init__(self):
        self.opponent = Opponent()
        self.player = Player("Betsy")
        self.die = Die()

class Die:
    def __init__(self):
        self.roll = randint(1, len(dieNumbers))

    def __str__(self):
        return f"A {self.roll} was rolled"


class Player:
    def __init__(self, name):
        self.roundScore = 0
        self.totalScore = 0
        self.name = name
        self.opponent = Opponent()

    def playerTurn(self):
        curentRoll = Die()
        print(f"{self.name}! You rolled a {currentRoll).")
        if currentRoll == 1:
            print(f"Bad luck {self.name}, YOU GET NOTHING!")
            Opponent()
        



class Opponent:
    def __init__(self):
        self.roundScore = 0
        self.totalScore = 0
        self.name = 'STORMAGEDEON'
        


    