# Author: de las Fuentes Monreal,    Ane
#         Gonzalez Castro,          Maria Angeles
#         Gonzalez Rodriguez,       Daniel
# Date: November 20th 2023
# Description: This program will contain the necessary functions to initialize all the data for the game

import os  # To check if the file exists
import random  # To generate random values
import pickle  # To unpickle a file

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

        lineNumber = 0  # Variable to get track of the lines
        # Field size
        height = 0  # This variable will store the number of rows of the grid
        width = 0  # This variable will store the number of columns of the grid

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

        # We create an empty 2D list for the field
        for i in range(height):  # For each row in the grid
            row = []  # We create an empty row
            for j in range(width):  # For each column in that row
                row.append(None)  # We assign the value none for each space of the field
            self.__field.append(row)  # We append each row

        # We iterate through that empty 2D list to allocate the assigned vegetables
        for vegetable in range(GameEngine.NUMBEROFVEGGIES):  # For each vegetable to be created
            chosenVeggie = random.randrange(len(self.__vegetables))  # Get random one from the list of possible veggies
            col = random.randrange(width)  # We generate a random horizontal position between the limits
            row = random.randrange(height)  # We generate a random vertical position between the limits

            # if the position chosen is already occupied, we look for another one until we find an empty slot
            while self.__field[row][col] is not None:  # While that position is not empty
                col = random.randrange(width)  # We generate a random horizontal position
                row = random.randrange(height)  # We generate a random vertical position

            self.__field[row][col] = self.__vegetables[
                chosenVeggie].getInhabitSymbol()  # Writing the symbol in the field

    def initCaptain(self):
        """
        This function initializes all the values for the Captain. It randomly allocates the captain in the field, and
        it creates an instance of the class captain with its position. It takes in and returns nothing.
        """
        width = len(self.__field[0])  # Extracting number of columns
        height = len(self.__field)  # Extracting number of rows

        col = random.randrange(width)  # We generate a random position in columns
        row = random.randrange(height)  # We generate a random position in rows

        while self.__field[row][col] is not None:  # While that position is not empty
            col = random.randrange(width)  # We generate a random position in columns
            row = random.randrange(height)  # We generate a random position in rows

        # Now that we found a random empty place to allocate the captain, we first create an instance of the class
        # "Captain"
        captainV = Captain(row, col)  # Row is the creature x member value, and column is the y as we decided.
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
            width = len(self.__field[0])  # Number of columns
            height = len(self.__field)  # Number of rows

            # We generate a random position
            col = random.randrange(width)
            row = random.randrange(height)

            while self.__field[row][col] is not None:  # While that position is not empty
                # We generate another random position
                col = random.randrange(width)
                row = random.randrange(height)

            # Once we get an available position, we first create an instance of the class "Rabbit"
            rabbit_i = Rabbit(row, col)
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

        for row in range(len(self.__field)):  # For each row of the field
            for col in range(len(self.__field[0])):  # For each position in that row (column)r
                if (self.__field[row][col] is not None) and (self.__field[row][col] != "V") and (
                        self.__field[row][col] != "R"):
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
        """
        This function will print the field in a user-friendly way: in a 2D grid format with a border around the
        grid. It takes in and returns nothing.
        """
        print("")  # Printing an empty line to separate

        # First, we print the upper border
        for i in range(len(self.__field[0]) + 2):  # For a length of a line of the grid plus the borders...
            print("#".center(3), end="")  # Print a symbol # in a space of three characters, centered

        print("")  # Print separator

        # Now, we print each line of the grid, leaving blank spaces for the empty slots
        # Two lateral borders are also printed, adding # at the beginning and end of each line
        for row in range(len(self.__field)):  # For each row in the grid
            print("#".center(3), end="")  # We first print the left border
            for col in range(len(self.__field[0])):  # For each slot (column) in a row
                if self.__field[row][col] is None:  # if the slot is empty, print a blank space of width 3
                    print(" ".center(3), end="")
                else:
                    print(self.__field[row][col].center(3), end="")  # If it is not empty, print the symbol
            print("#".center(3))  # Print the right border

        # Finally, we print the lower border
        for i in range(len(self.__field[0]) + 2):
            print("#".center(3), end="")

        print("\n")  # Printing two separators

    def getScore(self):
        """
        This function is the getter of the score. It takes in nothing and returns the score.
        """
        return self.__score

    def moveRabbits(self):
        """
        This function will move the Rabbits across the field. It takes in and returns nothing.
        """
        # NOTE: the convention used is x for row and y for column
        for rabbit in range(GameEngine.NUMBEROFRABBITS):  # For every rabbit
            incrementX = random.randrange(-1, 2, 1)  # We generate a random increment in X: this is: -1, 0, 1
            incrementY = random.randrange(-1, 2, 1)  # We generate a random increment in Y: this is: -1, 0, 1

            X = self.__rabbits[rabbit].getX()  # We get the original value of X
            Y = self.__rabbits[rabbit].getY()  # We get the original value of Y

            newX = X + incrementX  # We find our new X (row)
            newY = Y + incrementY  # We find our new Y (column)

            if 0 <= newX < len(self.__field) and 0 <= newY < len(self.__field[0]):  # I am within limits =
                # If the new row is inside the height of the field and the new column inside the width
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
            self.__field[X][Y] = None
            self.__field[newX][newY] = "R"

    def moveCptHorizontal(self, deltaY):
        """
        This function is in charge of the horizontal movement of the captain, which corresponds to the change of columns
        in the field.
        :param deltaY: A number that determines the horizontal movement of the captain, +1 to go right or -1
        to go left in the grid
        :type deltaY: int
        """
        # We need the captain current position:
        x = self.__captain.getX()  # row
        y = self.__captain.getY()  # column

        if self.__field[x][y + deltaY] is None:  # If the captain position plus movement goes to an empty slot
            self.__captain.setY(y + deltaY)
            self.__field[x][y + deltaY] = self.__captain.getInhabitSymbol()  # The captain occupies the new slot
            self.__field[x][y] = None  # Leave the previous slot free

        # If there is a veggie in the next slot:
        elif (self.__field[x][y + deltaY] is not None) and (self.__field[x][y + deltaY] != "V") and (
                self.__field[x][y + deltaY] != "R"):
            self.__captain.setY(y + deltaY)  # update captain position
            # We need to know what veggie was found and access to its name and points:
            vegSymbol = self.__field[x][y + deltaY]
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
                y + deltaY] = self.__captain.getInhabitSymbol()  # The captain occupies the new slot
            #      ***** check!!
            self.__field[x][y] = None  # leave the previous slot free

        elif self.__field[x][y + deltaY] == "R":  # if there is a rabbit in the next slot
            print("Don't step on the bunnies!")

    def moveCptVertical(self, deltaX):
        """
        This function is in charge of the vertical movement of the captain, which corresponds to the change of columns
        in the field.
        :param deltaX: A number that determines the vertical movement of the captain, +1 to go up or -1
        to go down in the grid
        :type deltaX: int
        """
        # We need the captain current position:
        x = self.__captain.getX()
        y = self.__captain.getY()

        if self.__field[x + deltaX][y] is None:  # if the captain position plus movement goes to an empty slot
            self.__captain.setX(x + deltaX)
            self.__field[x + deltaX][y] = self.__captain.getInhabitSymbol()  # The captain occupies the new slot
            self.__field[x][y] = None  # leave the previous slot free

        # if there is a veggie in the next slot
        elif (self.__field[x + deltaX][y] is not None) and (self.__field[x + deltaX][y] != "V") and (
                self.__field[x + deltaX][y] != "R"):
            self.__captain.setX(x + deltaX)  # update captain position
            # We need to know what veggie was found and access to its name and points:
            vegSymbol = self.__field[x + deltaX][y]  # First we copy the symbol of the veggie found to search for it
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
            self.__field[x + deltaX][
                y] = self.__captain.getInhabitSymbol()  # The captain occupies the new slot               *****CHECK
            self.__field[x][y] = None  # leave the previous slot free

        elif self.__field[x + deltaX][y] == "R":  # if there is a rabbit in the next slot
            print("Don't step on the bunnies!")

    def moveCaptain(self):
        """
        This function is in charge of the movement of the captain. the captain can move upwards, downwards, right or
        left. This function prompts the user for a choice of movement and calls the corresponding function.
        """
        x = self.__captain.getX()  # row
        y = self.__captain.getY()  # column

        # Prompt the user for the captain movement desired
        move = input("Would you like to move up(W), down(S), left(A), or right(D):").upper()

        while move not in {"W", "S", "A", "D"}:  # Making sure the user selects a feasible movement for the captain
            print("That movement does not exist. Please select another choice.")
            move = input("Would you like to move up(W), down(S), left(A), or right(D):").upper()

        if move == "W":  # If the user wants the captain to move upwards:
            # Check if the captain can move upwards
            if x > 0:  # if the row is not the upper one (row 0)
                self.moveCptVertical(-1)
            else:  # If the row is the upper one, the captain cannot move upwards
                print("The captain cannot move upwards!")

        elif move == "S":  # If the user wants the captain to move downwards:
            # Check if the captain can move downwards
            if x < len(self.__field) - 1:
                # this len returns n. rows in the field (height). If the height is 10 rows (0-9), the captain can move
                # downwards if he is not in row 9 = his row is less than (height-1)
                self.moveCptVertical(1)
            else:
                print("The captain cannot move downwards!")

        elif move == "A":  # If the user wants the captain to move left:
            # Check if the captain can move left
            if y > 0:  # The captain will not move outside the left boundary if he is not in column 0
                # which is the same as while he is in a column higher than 0
                self.moveCptHorizontal(-1)
            else:
                print("The captain cannot move left!")

        elif move == "D":
            # Check if the captain can move right
            if y < len(self.__field[
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
            print(i.getName())  # Print every name
        print(f"Your score was: {self.__score}")  # Print the score

    def highScore(self):
        """
        This function prompts the user for their initials and reads the file that contains the previous scores. It saves
        the users score and its initials in the correct position of the list (descending order of points), and shows the
        complete list on screen.
        """
        lPlayers = []  # Creating the list that will contain the scores
        if os.path.exists(self.HIGHSCOREFILE):  # If the file exists
            myFile = open(self.HIGHSCOREFILE, "rb")  # We open the file to access the data
            lPlayers = pickle.load(myFile)  # We unpickle the file and store the scores list in the variable lPlayers
            myFile.close()  # We close the file
            initials = input("Write your initials: ")  # Input the player initials
            initials = initials[0:3]  # Taking only the first three initials of the player
            if len(lPlayers[0]) == 0:  # If the list is empty: append the first score
                firstScore = (initials, self.__score)
                lPlayers.append(firstScore)
            else: # the list has scores already: search on the list the position of the new score
                for i in range(len(lPlayers)):
                    if self.__score > lPlayers[i][1]:  # the new score is the best or better than some of the saved ones
                        newScore = (initials, self.__score)
                        lPlayers.insert(i, newScore)  # insert the new score
                        break
                    if i == (len(lPlayers)-1) and self.__score <= lPlayers[i][1]:  # the new score is the worst for now
                        newScore = (initials, self.__score)
                        lPlayers.append(newScore)  # append the new score
        else:  # If the file does not exist
            myFile = open(self.HIGHSCOREFILE, "wb") # We open the file for writing to create it
            myFile.close()  # We close the file
            initials = input("Write your initials: ")  # Input the player initials
            initials = initials[0:3]  # Taking only the first three initials of the player
            firstScore = (initials, self.__score)
            lPlayers.append(firstScore)  # Append the first score
        print("Highest scores:")  # Scores header
        for i in range(len(lPlayers)):  # Printing the scores list
            print(f"\t{lPlayers[i][0]}:\t{lPlayers[i][1]}")
        myFile = open(self.HIGHSCOREFILE, "wb")  # We open the file to write the data
        pickle.dump(lPlayers, myFile)  # We pickle the list lPlayers into the file
        myFile.close()  # We close the file

