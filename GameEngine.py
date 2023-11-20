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

    def getScore(self):
        return self.__score

    def moveRabbits(self):

        for rabbit in range(GameEngine.NUMBEROFRABBITS):
            incrementX = random.randrange(-1, 2, 1)  # this is: -1, 0, 1
            incrementY = random.randrange(-1, 2, 1)

            X = self.__rabbits[rabbit].getX()
            Y = self.__rabbits[rabbit].getY()

            newX = X + incrementX
            newY = Y + incrementY

            if 0 <= newX < len(self.__field) and 0 <= newY < len(self.__field[0]):  # I am within limits
                if self.__field[newX][newY] == "V" or self.__field[newX][newY] == "R":  # The place is taken by the captain or a rabbit, so I do not move
                    newX = X
                    newY = Y
            else:  # I am not within limits, I do not move
                newX = X
                newY = Y

            self.__rabbits[rabbit].setX(newX)
            self.__rabbits[rabbit].setY(newY)

            self.__field[Y][X] = None
            self.__field[newY][newX] = "R"



