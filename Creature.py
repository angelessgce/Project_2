# Author: de las Fuentes Monreal,   Ane
#         Gonzalez Castro,          Maria Angeles
#         Gonzalez Rodriguez,       Daniel
# Date: November 20th 2023
# Description: This file contains the class Creature, subclass of the class FieldInhabitant, which adds the attributes
# of x and y positioning to the attributes which its father class had already.

from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        FieldInhabitant.__init__(self,symbol)
        self._x = x # We decide to use x to represent the row, being 0 the upper row
        self._y = y # We decide to use y to represent the column, being 0 the left row

    def getX(self): #it will return the row
        return self._x

    def setX(self, newX):
        self._x = newX

    def getY(self): #it will return the column
        return self._y

    def setY(self, newY):
        self._y = newY
