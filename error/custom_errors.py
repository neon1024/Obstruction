class CellNotEmptyError(BaseException):

    def __init__(self):
        self.__message = "[!] Cell not empty"
        super(CellNotEmptyError, self).__init__(self.__message)


class InvalidCoordinatesError(BaseException):

    def __init__(self):
        self.__message = "[!] Invalid coordinates"
        super(InvalidCoordinatesError, self).__init__(self.__message)
