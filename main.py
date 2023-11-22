# Author: de las Fuentes Monreal,   Ane
#         Gonzalez Castro,          Maria Angeles
#         Gonzalez Rodriguez,       Daniel
# Date: November 20th 2023
# Description: this program will contain all the necessary function calls

from GameEngine import GameEngine

def main():
    game = GameEngine()
    game.initializeGame()
    game.intro()
    print(game.remainingVeggies())
    print("Before moving rabbits:")
    game.printField()
    game.moveRabbits()
    print("After moving rabbits:")
    game.printField()

main()
