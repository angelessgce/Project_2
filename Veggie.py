# Author: de las Fuentes Monreal,    Ane
#         Gonzalez Castro,          Maria Angeles
#         Gonzalez Rodriguez,       Daniel
# Date: November 20th 2023
# Description: This is the definition of the class Veggie, subclass of FieldInhabitant

from FieldInhabitant import FieldInhabitant

class Veggie (FieldInhabitant):
    def __init__(self, vegName, vegSymbol, vegPoints):
        FieldInhabitant.__init__(self, vegSymbol)
        self.__name = vegName
        self.__points = vegPoints

    def __str__(self):
        #Output example "G: Garlic 5 points"
        return str(f"{FieldInhabitant.getInhabitSymbol(self)}: {self.__name} {self.__points} points")

    def getName(self):
        return self.__name

    def getPoints(self):
        return self.__points

    def setName(self, newName):
      self.__name=newName

    def setPoints(self, newPoints):
        self.__points = newPoints
