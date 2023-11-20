# Author: de las Fuentes Monreal,   Ane
#         Gonzalez Castro,          Maria Angeles
#         Gonzalez Rodriguez,       Daniel
# Date: November 20th 2023
# Description: This file contains the class Captain, which is a subclass of the class Creature. It inherits all the
# attributes of its father class, and adds the attribute veggiesCollected, which stores a list that will be used for
# saving every object of the class Veggie that the captain will collect. It also has the function addVeggie, for
# appending a new collected veggie to the list veggiesCollected, a setter function for changing the list to a new one,
# and a getter function that returns the list.

from Creature import Creature

class Captain(Creature):
    def __init__(self, x, y):
        Creature.__init__(x, y, "V")
        self.__veggiesCollected = []

    def addVeggie(self, Veggie):
        self.__veggiesCollected.append(Veggie)

    def getVeggiesCollected(self):
        return self.__veggiesCollected

    def setVeggiesCollected(self, newVeggiesCollected):
        # receiving a new list and replacing veggiesCollected
        # clean the initial list
        self.__veggiesCollected.clear()
        # create the new list
        for item in range(len(newVeggiesCollected)):
            self.__veggiesCollected.append(newVeggiesCollected[item])
