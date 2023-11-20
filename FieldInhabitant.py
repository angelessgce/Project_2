# Author: de las Fuentes Monreal,   Ane
#         Gonzalez Castro,          Maria Angeles
#         Gonzalez Rodriguez,       Daniel
# Date: November 20th 2023
# Description:

class FieldInhabitant ():
    def __init__(self, symbol):
        self._inhabitSymbol=symbol

    def getInhabitSymbol(self):
        return self._inhabitSymbol

    def setInhabitSymbol(self, newSymbol):
        self._inhabitSymbol=newSymbol