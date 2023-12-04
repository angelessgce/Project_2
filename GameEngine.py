# Author: de las Fuentes Monreal,    Ane
#         Gonzalez Castro,          Maria Angeles
#         Gonzalez Rodriguez,       Daniel
# Date: November 20th 2023
# Description: This program will contain the necessary functions to initialize all the data for the game

import os  # To check if the file exists
import random  # To generate random values

from Veggie import Veggie
from Captain import Captain
from Rabbit import Rabbit


class GameEngine:
    # We initialize the constant values of number of veggies, number of rabbits, and the highest score file
    NUMBEROFVEGGIES = 30
    NUMBEROFRABBITS = 5
    HIGHSCOREFILE = "highscore.data"

    def __init__(self):
        """
        This function defines a constructor to initialize class variables of GameEngine and objects or setup class
        data structures. It takes in and returns nothing.
        """
        self.__field = []  # We initialize the field as an empty list
        self.__rabbits = []  # We initialize the rabbits as an empty list
        self.__captain = None  # We initialize the captain as None
        self.__vegetables = []  # We initialize the vegetables as an empty list
        self.__score = 0  # We initialize the score as zero

    def initVeggies(self):
        """
        This function initializes the veggies. This is, it reads the data from the file, and ads this information
        correctly to the field. It takes in and returns nothing.
        """
        # Variable to get track of the lines
        lineNumber = 0
        height = 0
        width = 0

        # We prompt the user for the name of the file
        filename = input("Please enter the name of the file: ")

        # We check if it exists, keep asking if it does not
        while not os.path.exists(filename):
            filename = input("That file does not exist! Please enter the name of the file: ")

        myFile = open(filename, "r")  # We open the file to access the data

        for line in myFile:  # We iterate through the data and keep it
            lineNumber += 1
            if lineNumber == 1:  # the first line is the size of the grid
                data = line.strip().split(',')
                height = int(data[-2])  # We clean the data
                width = int(data[-1])  # We clean the data

            else:
                data = line.strip().split(',')  # the subsequent lines are added to the list of possible vegetables
                veggies = Veggie(data[0], data[1], int(data[2]))  # We create and instance of Veggie class and
                # associate it
                # with the variable called "veggies"
                self.__vegetables.append(veggies)  # We add it to the updated list of possible vegetables
        myFile.close()  # We close the file

        for i in range(height):  # We create an empty 2D list for the field
            row = []  # We create an empty row
            for j in range(width):
                row.append(None)  # We assign the value none for each space of the field
            self.__field.append(row)  # We append each row

        for vegetable in range(GameEngine.NUMBEROFVEGGIES):  # We iterate through that empty 2D list
            chosenVeggie = random.randrange(len(self.__vegetables))  # We get a random veggie
            col = random.randrange(width)  # We generate a random position
            row = random.randrange(height)  # We generate a random position

            while self.__field[row][col] is not None:  # While that position is not empty
                col = random.randrange(width)  # We generate a random position
                row = random.randrange(height)  # We generate a random position

            self.__field[row][col] = self.__vegetables[chosenVeggie].getInhabitSymbol()  # Row is x and col is y

    def initCaptain(self):
        """
        This function initializes all the values for the Captain. It randomly allocates the captain in the field, and
        it creates an instance of the class captain with its position. It takes in and returns nothing.
        """
        width = len(self.__field[0])
        height = len(self.__field)
        col = random.randrange(width)  # We generate a random position in columns
        row = random.randrange(height)  # We generate a random position in rows

        while self.__field[row][col] is not None:  # While that position is not empty
            col = random.randrange(width)  # We generate a random position in columns
            row = random.randrange(height)  # We generate a random position in rows

        # Now that we found a random empty place to allocate the captain, we first create an instance of the class
        # "Captain"
        captainV = Captain(row, col)
        self.__captain = captainV
        # And now we store in the field the position of the captain writing its symbol
        self.__field[row][col] = captainV.getInhabitSymbol()

    def initRabbits(self):
        """
        This function initializes all the values for the Rabbits. It randomly allocates the rabbits in the field, and
        it creates an instance of the class rabbit with its position. It appends this values to the list rabbits.
        It takes in and returns nothing.
        """
        for rabbit in range(GameEngine.NUMBEROFRABBITS):  # For each rabbit
            width = len(self.__field[0])
            height = len(self.__field)
            # We generate a random position
            col = random.randrange(width)
            row = random.randrange(height)

            while self.__field[row][col] is not None:  # While that position is not empty
                # We generate another random position
                col = random.randrange(width)
                row = random.randrange(height)

            # Once we get an available position, we first create an instance of the class "Rabbit"
            rabbit_i = Rabbit(col, row)
            self.__rabbits.append(rabbit_i)  # Add it to the rabbits list
            self.__field[row][col] = rabbit_i.getInhabitSymbol()  # Associate the symbol

    def initializeGame(self):
        """
        This function will call all the necessary initializing functions. It takes in and returns nothing.
        """
        self.initVeggies()  # Initialize Veggies
        self.initCaptain()  # Initialize Captain
        self.initRabbits()  # Initialize Rabbits

    def remainingVeggies(self):
        remaining = 0
        for j in range(len(self.__field)):
            for i in range(len(self.__field[0])):
                if (self.__field[i][j] is not None) and (self.__field[i][j] != "V") and (self.__field[i][j] != "R"):
                    remaining += 1
        return remaining

    def intro(self):
        """This function will welcome the player to the game, the premise and the goals will be explained, a list of
         possible vegetables is output, including the symbol name and value, the captain Veggie and the Rabbit's symbols
        are output. It takes in and returns nothing.
        """

        # We print a welcome message
        print("""Welcome to Captain Veggie!
You are Captain Veggie, and a bunch of rabbits are trying to feast with your
provisions. Recollect as many as you can before they took it all!
        
The following list shows all the vegetables, and how much they worth:""")

        # We output the vegetables' information
        for i in range(len(self.__vegetables)):  # For each vegetable in the list
            print(f"{self.__vegetables[i].__str__()}")  # Output the string

        # We output the information regarding the symbols of capitan Veggie and the Rabbits
        print(f"\nCaptain Veggie is represented with the symbol: V")
        print(f"The rabbits are represented with the symbol: R")

    def printField(self):
        """ This function will print the field in a user-friendly way: in a 2D grid format with a border around the
        grid. It takes in and returns nothing.
        """
        print("")

        for i in range(len(self.__field[0]) + 2):
            print("#".center(3), end="")
        print("")
        for j in range(len(self.__field)):
            print("#".center(3), end="")
            for i in range(len(self.__field[0])):
                if self.__field[i][j] is None:
                    print(" ".center(3), end="")
                else:
                    print(self.__field[i][j].center(3), end="")
            print("#".center(3))
        for i in range(len(self.__field[0]) + 2):
            print("#".center(3), end="")
        print("\n")

    def getScore(self):
        """
        This function is the getter of the score. It takes in nothing and returns the score.
        """
        return self.__score

    def moveRabbits(self):
        """
        This function will move the Rabbits across the field. It takes in and returns nothing.
        """
        for rabbit in range(GameEngine.NUMBEROFRABBITS):  # For every rabbit
            incrementX = random.randrange(-1, 2, 1)  # We generate a random increment in X: this is: -1, 0, 1
            incrementY = random.randrange(-1, 2, 1)  # We generate a random increment in Y: this is: -1, 0, 1

            X = self.__rabbits[rabbit].getX()  # We get the original value of X
            Y = self.__rabbits[rabbit].getY()  # We get the original value of Y

            newX = X + incrementX  # We find our new X
            newY = Y + incrementY  # We find our new Y

            if 0 <= newX < len(self.__field) and 0 <= newY < len(self.__field[0]):  # I am within limits
                if self.__field[newX][newY] == "V" or self.__field[newX][newY] == "R":  # The place is taken by the
                    # captain or a rabbit, so I do not move
                    newX = X
                    newY = Y
            else:  # I am not within limits, I do not move
                newX = X
                newY = Y

            # We update the values of X and Y

            self.__rabbits[rabbit].setX(newX)
            self.__rabbits[rabbit].setY(newY)

            # We update the values of the previous X and Y
            self.__field[Y][X] = None
            self.__field[newY][newX] = "R"

    def moveCptVertical(self, yMovement):
        """
        """
        # We need the captain current position:
        x = self.__captain.getX()
        y = self.__captain.getY()

        if self.__field[x][y + yMovement] is None:  # if the captain position plus movement goes to an empty slot
            self.__captain.setY(y + yMovement)
            self.__field[x][y + yMovement] = self.__captain.getInhabitSymbol()  # The captain occupies the new slot
            #                        ****Check!!
            self.__field[x][y] = None  # leave the previous slot free

        # if there is a veggie in the next slot:
        elif (self.__field[x][y + yMovement] is not None) and (self.__field[x][y + yMovement] != "V") and (
                self.__field[x][y + yMovement] != "R"):
            self.__captain.setY(y + yMovement)  # update captain position
            # We need to know what veggie was found and access to its name and points:
            vegSymbol = self.__field[x][y + yMovement]
            # We search for the veggie in the list
            for veggie in self.__vegetables:
                if veggie.getInhabitSymbol() == vegSymbol:
                    vegObject = veggie
                    break  # Finish the loop as we do not want to go through all the Onions or Carrots or whatever:
                    # we just want the first one

            print(f"Yummy! A delicious {vegObject.getName()}.")  # output the name of the veggie found

            self.__captain.addVeggie(vegObject)  # add veggie to th captain veggies list
            self.__score += vegObject.getPoints()
            self.__field[x][
                y + yMovement] = self.__captain.getInhabitSymbol()  # The captain occupies the new slot
            #      ***** check!!
            self.__field[x][y] = None  # leave the previous slot free

        elif self.__field[x][y + yMovement] == "R":  # if there is a rabbit in the next slot
            print("Don't step on the bunnies!")

    def moveCptHorizontal(self, xMovement):
        # We need the captain current position:
        x = self.__captain.getX()
        y = self.__captain.getY()

        if self.__field[x + xMovement][y] is None:  # if the captain position plus movement goes to an empty slot
            self.__captain.setX(x + xMovement)
            self.__field[x + xMovement][y] = self.__captain.getInhabitSymbol()  # The captain occupies the new slot
            self.__field[x][y] = None  # leave the previous slot free

        # if there is a veggie in the next slot
        elif (self.__field[x + xMovement][y] is not None) and (self.__field[x + xMovement][y] != "V") and (
                self.__field[x + xMovement][y] != "R"):
            self.__captain.setX(x + xMovement)  # update captain position
            # We need to know what veggie was found and access to its name and points:
            vegSymbol = self.__field[x + xMovement][y]  # First we copy the symbol of the veggie found to search for it
            # Then we search for the veggie in the list
            for veggie in self.__vegetables:
                if veggie.getInhabitSymbol() == vegSymbol:
                    vegObject = veggie  # and we create an object of this veggie found
                    break  # Finish the loop as we do not want to go through all the Onions or Carrots or whatever:
                    # we just want the first one

            print(
                f"Yummy! A delicious {vegObject.getName()}.")  # output the name of the veggie found
            self.__captain.addVeggie(vegObject)  # add veggie to the captain veggies list
            self.__score += vegObject.getPoints()
            self.__field[x + xMovement][
                y] = self.__captain.getInhabitSymbol()  # The captain occupies the new slot               *****CHECK
            self.__field[x][y] = None  # leave the previous slot free

        elif self.__field[x + xMovement][y] == "R":  # if there is a rabbit in the next slot

            print("Don't step on the bunnies!")

    def moveCaptain(self):
        # To simplify the code...
        x = self.__captain.getX()
        y = self.__captain.getY()

        move = input("Would you like to move up(W), down(S), left(A), or right(D):").upper()

        while move not in {"W", "S", "A", "D"}:
            print("That movement does not exist. Please select another choice.")
            move = input("Would you like to move up(W), down(S), left(A), or right(D):").upper()

        if move == "W":
            # Check if the captain can move upwards
            if y > 0:
                self.moveCptVertical(-1)
            else:
                print("The captain cannot move upwards!")

        elif move == "S":
            # Check if the captain can move downwards
            if y < len(self.__field) - 1:
                # this len returns n. rows in the field (height). If the height is 10 rows (0-9), the captain can move
                # downwards if he is not in row 9 = his row is less than (height-1)
                self.moveCptVertical(1)
            else:
                print("The captain cannot move downwards!")

        elif move == "A":
            # Check if the captain can move left
            if x > 0:  # The captain will not move outside the left boundary if he is not in column 0
                # which is the same as while he is in a column higher than 0
                self.moveCptHorizontal(-1)
            else:
                print("The captain cannot move left!")

        elif move == "D":
            # Check if the captain can move right
            if x < len(self.__field[
                           0]) - 1:  # The captain will not move outside the right boundary if he is not in the last
                # column
                # which is the same as while he is in a column less than the last one
                self.moveCptHorizontal(1)
            else:
                print("The captain cannot move right!")

    def gameOver(self):
        """
        This function outputs when the game is finished. It takes in and returns nothing.
        """
        # We print an appropriate message
        print("GAME OVER!")
        print("You managed to harvest the following vegetables:")
        # We iterate through the collected veggies
        for i in self.__captain.getVeggiesCollected():
            print(i.getName())  # print every name
        print(f"Your score was: {self.__score}")  # print the score
