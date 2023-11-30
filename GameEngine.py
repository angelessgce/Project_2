# Author: de las Fuentes Monreal,    Ane
#         Gonzalez Castro,          Maria Angeles
#         Gonzalez Rodriguez,       Daniel
# Date: November 20th 2023
# Description: This program will contain the necessary functions to initialize all the data for the game

import os  # To check if the file exists
import random

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
                veggies = Veggie(data[0], data[1], data[2])  # We create and instance of Veggie class and associate it
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

            while self.__field[row][col] != None:  # While that position is not empty
                col = random.randrange(width)  # We generate a random position
                row = random.randrange(height)  # We generate a random position

            self.__field[row][col] = self.__vegetables[chosenVeggie].getInhabitSymbol() # Row is x and col is y

    def initCaptain(self):
        """
        This function initializes all the values for the Captain
        :return:
        """
        width= len(self.__field[0])
        height= len(self.__field)
        col = random.randrange(width)  # We generate a random position
        row = random.randrange(height)

        while self.__field[row][col] != None:  # While that position is not empty
            col = random.randrange(width)  # We generate a random position
            row = random.randrange(height)

        #Now that we found a random empty place to allocate the captain, we first create an instance of the class "Captain"
        captainV = Captain(row,col) #                                                                                             check this!
        self.__captain=captainV
        #And now we store in the field the position of the captain writing its symbol
        self.__field[row][col] = captainV.getInhabitSymbol()

    def initRabbits(self):
        for rabbit in range(GameEngine.NUMBEROFRABBITS):  # For each rabbit
            width = len(self.__field[0])
            height = len(self.__field)
            col = random.randrange(width)  # We generate a random position
            row = random.randrange(height)

            while self.__field[row][col] != None:  # While that position is not empty
                col = random.randrange(width)  # We generate another random position
                row = random.randrange(height)

            rabbit_i = Rabbit(col, row)
            self.__rabbits.append(rabbit_i)
            self.__field[row][col] = rabbit_i.getInhabitSymbol()

    def initializeGame(self):
        self.initVeggies()
        self.initCaptain()
        #print (f"The captain is located in {self.__captain.getX()}, {self.__captain.getY()}")
        self.initRabbits()

    def remainingVeggies(self):
        remaining = 0
        for j in range(len(self.__field)):
            for i in range(len(self.__field[0])):
                if (self.__field[i][j] != None) and (self.__field[i][j] != "V") and (self.__field[i][j] != "R"):
                    remaining += 1
        return remaining

    def intro(self):
        print("""Welcome to Captain Veggie!
You are Captain Veggie, and a bunch of rabbits are trying to feast with your
provisions. Recolect as many as you can before they took it all!
        
The following list shows all the vegetables, and how much they worth:""")

        for i in range(len(self.__vegetables)): #for each vegetable in the list
            print(f"{self.__vegetables[i].__str__()}") #output the string

        print(f"\nCaptain Veggie is represented with the symbol: V")
        print(f"The rabbits are represented with the symbol: R")

    def printField(self):
        print("")
        for i in range(len(self.__field[0]) + 2):
            print("#".center(3), end="")
        print("")
        for j in range(len(self.__field)):
            print("#".center(3), end="")
            for i in range(len(self.__field[0])):
                if self.__field[i][j] == None:
                    print(" ".center(3), end="")
                else:
                    print(self.__field[i][j].center(3), end="")
            print("#".center(3))
        for i in range(len(self.__field[0]) + 2):
            print("#".center(3), end="")
        print("\n")

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

    def moveCptVertical(self, yMovement):
        print(
            "You have entered the function moveCptVertical!")  # This should be deleted or commented before submiting, DEBUGGING
        # We need the captain current position:
        x = self.__captain.getX()
        y = self.__captain.getY()

        if self.__field[x][y+yMovement]== None: #if the captain position plus movement goes to an empty slot
            self.__captain.setY(y+yMovement)
            self.__field[x][y+yMovement]=self.__captain.getInhabitSymbol() #The captain occupies the new slot                               ****Check!!
            self.__field[x][y] = None #leave the previous slot free

        #if there is a veggie in the next slot:
        elif (self.__field[x][y+yMovement] != None) and (self.__field[x][y+yMovement] != "V") and (self.__field[x][y+yMovement] != "R"):
            self.__captain.setY(y + yMovement) # update captain position
            # We need to know what veggie was found and access to its name and points:
            vegSymbol = self.__field[x][y+yMovement]
            #We search for the veggie in the list
            for veggie in self.__vegetables:
                if veggie.getInhabitSymbol() == vegSymbol:
                    vegObject = veggie
                    break #Finish the loop as we do not want to go through all the Onions or Carrots or whatever: we just want the first one

            print(f"Yummy! A delicious {vegObject.getName()}.") #output the name of the veggie found

            self.__captain.addVeggie(vegObject) #add veggie to th captain veggies list
            self.__score+=vegObject.getPoints()
            self.__field[x][y + yMovement] = self.__captain.getInhabitSymbol()  # The captain occupies the new slot                    ***** check!!
            self.__field[x][y] = None  # leave the previous slot free

        elif self.__field[x][y+yMovement]== "R": #if there is a rabbit in the next slot
            print("Don't step on the bunnies!")

    def moveCptHorizontal(self, xMovement):
        # We need the captain current position:
        x = self.__captain.getX()
        y = self.__captain.getY()

        if self.__field[x+xMovement][y] == None:  # if the captain position plus movement goes to an empty slot
            self.__captain.setX(x + xMovement)
            self.__field[x + xMovement][y] = self.__captain.getInhabitSymbol()  # The captain occupies the new slot
            self.__field[x][y] = None  # leave the previous slot free

        # if there is a veggie in the next slot
        elif (self.__field[x+xMovement][y] != None) and (self.__field[x+xMovement][y] != "V") and (self.__field[x+xMovement][y] != "R"):
            self.__captain.setX(x + xMovement)  # update captain position
            #We need to know what veggie was founf and access to its name and points:
            vegSymbol = self.__field[x+xMovement][y] #First we copy the symbol of the veggie found to search for it
            # Then we search for the veggie in the list
            for veggie in self.__vegetables:
                if veggie.getInhabitSymbol() == vegSymbol:
                    vegObject = veggie #and we create an object of this veggie found
                    break  # Finish the loop as we do not want to go through all the Onions or Carrots or whatever: we just want the first one

            print(
                f"Yummy! A delicious {vegObject.getName()}.")  # output the name of the veggie found
            self.__captain.addVeggie(vegObject)  # add veggie to the captain veggies list
            self.__score += vegObject.getPoints()
            self.__field[x+xMovement][y] = self.__captain.getInhabitSymbol()  # The captain occupies the new slot               *****CHECK
            self.__field[x][y] = None  # leave the previous slot free

        elif self.__field[x+xMovement][y] == "R":  # if there is a rabbit in the next slot

            print("Don't step on the bunnies!")

    def moveCaptain(self):
        #To simplify the code...
        x = self.__captain.getX()
        y = self.__captain.getY()

        move = input("Would you like to move up(W), down(S), left(A), or right(D):").upper()

        while move not in {"W", "S", "A", "D"}:
            print("That movement does not exist. Please select another choice.")
            move = input("Would you like to move up(W), down(S), left(A), or right(D):").upper()

        if move == "W":
            #Check if the captain can move upwards
            if y>0:
                self.moveCptVertical(-1)
            else:
                print("The captain cannot move upwards!")

        elif move=="S":
            #Check if the captain can move downwards
            if y < len(self.__field)-1:
                #this len returns n. rows in the field (height). If the height is 10 rows (0-9), the captain can move
                #dowwards if he is not in row 9 = his row is less than (height-1)
               self.moveCptVertical(1)
            else:
                print("The captain cannot move downwards!")

        elif move=="A":
            #Check if the captain can move left
            if x > 0 : # The captain will not move outside the left boundary if he is not in column 0
                # which is the same as while he is in a column higher than 0
                self.moveCptHorizontal(-1)
            else:
                print("The captain cannot move left!")

        elif move=="D":
            #Check if the captain can move right
            if x < len(self.__field[0])-1 : # The captain will not move outside the right boundary if he is not in the last column
                # which is the same as while he is in a column less than the last one
                self.moveCptHorizontal(1)
            else:
                print("The captain cannot move right!")


    def gameOver(self):
        print("GAME OVER!")
        print("You managed to harvest the following vegetables:")
        for i in self.__captain.getVeggiesCollected():
            print (i.getName())
        print(f"Your score was: {self.__score}")
