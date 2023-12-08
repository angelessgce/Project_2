# Author: de las Fuentes Monreal,   Ane
#         Gonzalez Castro,          Maria Angeles
#         Gonzalez Rodriguez,       Daniel
# Date: November 20th 2023
# Description: this program will contain all the necessary function calls

from GameEngine import GameEngine


def main():
    game = GameEngine()  # Instantiate and store a GameEngine object
    game.initializeGame()  # Initialize the game
    game.intro()  # Display the game's introduction

    while game.remainingVeggies() > 0:
        print(f"There are {game.remainingVeggies()} remaining veggies.")  # Remaining veggies
        game.printField()  # Print the field
        game.moveRabbits()  # Move the rabbits
        game.moveCaptain()  # Move the captain

    game.gameOver()  # When exiting the loop, the game ends
    game.highScore()  # Saving your score in the list of previous scores, and showing the positions list on screen


main()
