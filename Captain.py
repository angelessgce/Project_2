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
        """
        This function defines a constructor to initialize class variables of Captain and objects or setup class data
        structures. It takes the coordinates x and y, and returns nothing
        :param x: determines the position x
        :type x: int
        :param y: determines the position y
        :type y: int
        """
        Creature.__init__(self, x, y, "V")  # We initialize said variables
        self.__veggiesCollected = []  # We initialize the veggies collected as an empty list

    def addVeggie(self, Veggie):
        """
        This function that takes in a Veggie object as a parameter, returns
        nothing, and adds the object to the List of Veggie objects.
        :param Veggie: object to add to the list
        :type Veggie: object
        """
        self.__veggiesCollected.append(Veggie)  # We add the new veggies by appending the new list to the old list

    def getVeggiesCollected(self):
        """
        This function is a getter function of the collected veggies. It takes in nothing and returns said Collected
        Veggies.
        :return : list containing the veggies collected
        """
        return self.__veggiesCollected

    def setVeggiesCollected(self, newVeggiesCollected):
        """
        This function is a setter of the new collected veggies. It takes the new collected veggies and returns nothing.
        :param newVeggiesCollected: list containing the new veggies collected
        :type newVeggiesCollected: list
        """
        # receiving a new list and replacing veggiesCollected
        # clean the initial list

        
        self.__veggiesCollected.clear()
        # create the new list
        for item in range(len(newVeggiesCollected)):
            self.__veggiesCollected.append(newVeggiesCollected[item])  # We add the new elements
