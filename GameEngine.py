# Author: de las Fuentes Monreal,    Ane
#         Gonzalez Castro,          Maria Angeles
#         Gonzalez Rodriguez,       Daniel
# Date: November 20th 2023
# Description: this program will contain the function necessary to initialize all the data for the game

import os  # To check if the file exists
import random

from Veggie import Veggie


class GameEngine:
    NUMBEROFVEGGIES = 30
    NUMBEROFRABBITS = 5
    HIGHSCOREFILE = "highscore.data"

    def __init__(self):
        self.__field = []
        self.__rabbits = []
        self.__captain = None
        self.__vegetables = []
        self.__score = 0

    def initVeggies(self):
        lineNumber = 0

        # prompt the user for the name of the file
        filename = input("Please enter the name of the file: ")

        # check if it exists, keep asking if it does not
        while not os.path.exists(filename):
            filename = input("That file does not exist! Please enter the name of the file: ")

        myFile = open(filename, "r")  # open to access the data

        for line in myFile:  # I iterate through the data and keep it
            lineNumber += 1
            if lineNumber == 1:  # the first line is the size of the grid
                data = line.strip().split(',')
                height = int(data[-2])  # clean the data
                width = int(data[-1])  # clean the data

            else:
                data = line.strip().split(',')  # the subsequent lines are added to the list of possible vegetables
                veggies = Veggie(data[0], data[1], data[2])
                self.__vegetables.append(veggies)  # I add it to the updated list of possible vegetables

        for i in range(height):  # We create an empty 2D list for the field
            row = []
            for j in range(width):
                row.append(None)
            self.__field.append(row)

        for vegetable in range(GameEngine.NUMBEROFVEGGIES):  # We iterate through that empty 2D list
            chosenVeggie = random.randrange(len(self.__vegetables))  # We get a random veggie
            col = random.randrange(width)  # We generate a random position
            row = random.randrange(height)

            while self.__field[row][col] != None:  # While that position is not empty
                col = random.randrange(width)  # We generate a random position
                row = random.randrange(height)

            self.__field[row][col] = self.__vegetables[chosenVeggie].getInhabitSymbol()

        myFile.close()



