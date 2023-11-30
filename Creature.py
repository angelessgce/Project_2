# Author: de las Fuentes Monreal,   Ane
#         Gonzalez Castro,          Maria Angeles
#         Gonzalez Rodriguez,       Daniel
# Date: November 20th 2023
# Description: This file contains the class Creature, subclass of the class FieldInhabitant, which adds the attributes
# of x and y positioning to the attributes which its father class had already.

from FieldInhabitant import FieldInhabitant  # We import the superclass


class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        """
        This function defines a constructor to initialize class variables of Creature and objects or setup class data
        structures.
        :param x: determines the position x
        :type x: int
        :param y: determines the position y
        :type y: int
        :param symbol: it associates each inhabitant with each corresponding symbol. For example, "R" for Rabbit or "V"
        for Captain Veggie
        :type symbol: str
        """
        FieldInhabitant.__init__(self, symbol)  # We initialize said symbol
        self._x = x  # We decide to use x to represent the row, being 0 the upper row
        self._y = y  # We decide to use y to represent the column, being 0 the left row

    def getX(self):
        """
        This function is a getter function of the coordinate x. It takes in nothing and returns the coordinate x,
        this is, the row.
        :return: coordinate x, meaning the row of the field, starting at 0
        """
        return self._x

    def setX(self, newX):
        """
        This function is a setter of the coordinate x. It takes in the new value of x, and returns nothing.
        :param newX: new coordinate x
        :type newX: int
        """
        self._x = newX  # We associate the new value of x

    def getY(self):
        """
        This function is a getter function of the coordinate y. It takes in nothing and returns the coordinate y,
        this is, the column.
        :return: coordinate y, meaning the column of the field, starting at 0
        """
        return self._y

    def setY(self, newY):
        """
        This function is a setter of the coordinate y. It takes in the new value of y, and returns nothing.
        :param newY: new coordinate y
        :type newY: int
        """
        self._y = newY  # We associate the new value of y
