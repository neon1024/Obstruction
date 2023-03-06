class Computer:

    def __init__(self, symbol, name):
        self.__symbol = symbol
        self.__name = name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def name(self):
        return self.__name
