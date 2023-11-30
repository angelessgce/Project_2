# Author: de las Fuentes Monreal,    Ane Gonzalez Castro,          Maria Angeles Gonzalez Rodriguez,
# Daniel Date: November 20th 2023 Description: This is the definition of the class Veggie, subclass of
# FieldInhabitant. A veggie is an Inhabitant that apart from a symbol has a name and represent a defined number of
# points.

from FieldInhabitant import FieldInhabitant


class Veggie(FieldInhabitant):
    def __init__(self, vegName, vegSymbol, vegPoints):
        """
        This function defines a constructor to initialize class variables of Veggie and objects or setup class data
        structures. It takes the name, symbol, and points of each veggie. It returns nothing.
        :param vegName: name of the veggie
        :type vegName: str
        :param vegSymbol: symbol of the veggie. For example, "C" for carrot or "T" for tomato.
        :type vegSymbol: str
        :param vegPoints: points of each veggie
        :type vegPoints: int
        """
        FieldInhabitant.__init__(self, vegSymbol)  # We associate the symbol
        self.__name = vegName  # We associate the name
        self.__points = vegPoints  # We associate the points

    def __str__(self):
        """ This function modifies the output on an object when it is printed. In this case, for example, for each
        veggie we will follow the following format: "G: Garlic 5 points". It takes nothing, and returns said string.
        :return : the formatted string to get a user-friendly output when printed.
        """
        return str(f"{FieldInhabitant.getInhabitSymbol(self)}: {self.__name} {self.__points} points")

    def getName(self):
        """
        This function is a getter of the name of the veggie. It takes in nothing and returns the veggie's name.
        :return: the name of the veggie
        """
        return self.__name

    def getPoints(self):
        """
        This function is a getter of the veggie's point. It takes in nothing and returns the veggie's points.
        :return: the points corresponding to the veggie
        """
        return self.__points

    def setName(self, newName):
        """
        This function is a setter of the name of the veggie. It takes in the new name, and returns nothing.
        :param newName: name of the veggie
        :type newName: str
        """
        self.__name = newName  # We associate the new name

    def setPoints(self, newPoints):
        """
        This function is a setter of the points of each veggie. It takes in the points, and returns nothing.
        :param newPoints: points of the veggie
        :type newPoints: int
        """
        self.__points = newPoints  # We associate the new points
