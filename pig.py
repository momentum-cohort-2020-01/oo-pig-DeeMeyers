from random import randint

dieNumbers = [1,2,3,4,5,6]
maxScore = 100
startScore = 0
print('im alvie')
class Game:
    def __init__(self):
        self.opponent = Opponent()
        self.player = Player("Betsy")
        self.die = Die()
        self.player.playerTurn()
        

class Die:
    def __init__(self):
        self.roll = randint(1, len(dieNumbers))
        print(self.roll)

    def __str__(self):
        return f"A {self.roll} was rolled"


class Player:
    def __init__(self, name):
        self.roundScore = 0
        self.totalScore = 0
        self.name = name
        self.opponent = Opponent()

    def playerTurn(self):
        self.currentRoll = Die().roll
        print(f"{self.name}! You rolled a {self.currentRoll}.")
        if self.currentRoll == 1:
            print(f"Bad luck {self.name}, YOU GET NOTHING!")
            Opponent()
        elif (self.currentRoll + self.totalScore) == 100:
            print("Ya win ")
        else:
            pick = input("Do you want to (h)old or (r)oll?")
            if pick == "h":
                self.totalScore += self.roundScore
                print("Playing it safe I see...")
                Opponent()
            if pick == "r":
                self.roundScore += self.roundScore
                print("Good luck bub!")
                self.playerTurn()


class Opponent:
    def __init__(self):
        self.roundScore = 0
        self.totalScore = 0
        self.name = 'STORMAGEDEON'
        print(f'NOW {self.name} WILL GO')

    def opponentTurn(self):
        self.currentRoll = Die().roll
        print(f'{slef.name} ROLLED A {self.currentRoll}')
        if self.currentRoll == 1:
            print(f'{self.name} ENDS HER TURN')
            Player().playerTurn

Game()
    