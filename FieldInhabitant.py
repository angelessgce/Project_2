# Author: de las Fuentes Monreal,   Ane
#         Gonzalez Castro,          Maria Angeles
#         Gonzalez Rodriguez,       Daniel
# Date: November 20th 2023
# Description: This is the file containing the class FieldInhabitant

class FieldInhabitant():
    def __init__(self, symbol):
        """
        This function defines a constructor to initialize class variables of FieldInhabitant and objects or setup class
        data structures. It takes the symbol, and returns nothing.
        :param symbol: symbol representing each inhabitant. For example, "R" for Rabbit or "V" for Captain Veggie
        :type symbol: str
        """
        self._inhabitSymbol = symbol  # We initialize the symbol

    def getInhabitSymbol(self):
        """
        This function is a getter function of the inhabitant's symbol. It takes in nothing, and returns said symbol.
        :return: string containing a symbol
        """
        return self._inhabitSymbol

    def setInhabitSymbol(self, newSymbol):
        """
        This function is a setter of the inhabitant's symbol. It takes in said symbol, and returns nothing.
        :param newSymbol: new symbol of the inhabitant
        :type newSymbol: str
        """
        self._inhabitSymbol = newSymbol  # We associate the new symbol
