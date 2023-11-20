# Author: de las Fuentes Monreal,   Ane
#         Gonzalez Castro,          Maria Angeles
#         Gonzalez Rodriguez,       Daniel
# Date: November 20th 2023
# Description: This file contains the class Creature, subclass of the class FieldInhabitant, which adds the attributes
# of x and y positioning to the attributes which its father class had already.

from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        FieldInhabitant.__init__(symbol)
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def setX(self, newX):
        self._x = newX

    def getY(self):
        return self._y

    def setY(self, newY):
        self._y = newY
