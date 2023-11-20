# Author: de las Fuentes Monreal,   Ane
#         Gonzalez Castro,          Maria Angeles
#         Gonzalez Rodriguez,       Daniel
# Date: November 20th 2023
# Description: This file contains the class Rabbit, a subclass of Creature. Rabbit is a creature in the position (x,y)
# and specifies the symbol "R"

from Creature import Creature

class Rabbit(Creature):
    def __init__(self,x,y):
        Creature.__init__(self, x, y, "R")

