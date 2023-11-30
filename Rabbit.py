# Author: de las Fuentes Monreal,   Ane
#         Gonzalez Castro,          Maria Angeles
#         Gonzalez Rodriguez,       Daniel
# Date: November 20th 2023
# Description: This file contains the class Rabbit, a subclass of Creature. Rabbit is a creature in the position (x,y)
# and specifies the symbol "R"

from Creature import Creature

class Rabbit(Creature):
    def __init__(self, x, y):
        """
        This function defines a constructor to initialize class variables of Rabbit and objects or setup class data
        structures. It takes in the coordinates x and y, and returns nothing
        :param x: determines the position x
        :type x: int
        :param y: determines the position y
        :type y: int
        """
        Creature.__init__(self, x, y, "R")  # We initialize said coordinates and associate the symbol "R" to
        # the inhabitant rabbit
