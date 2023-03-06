from domain.Human import Human
from error.custom_errors import CellNotEmptyError, InvalidCoordinatesError
from ui.functions import print_player_name, get_rows, get_columns


class Game:

    def __init__(self, gameplay, grid, player1, player2):
        self.__gameplay = gameplay
        self.__grid = grid
        self.__EMPTY_CELL = "_"
        self.__player1 = player1
        self.__player2 = player2
        self.__last_move = 2
        self.__winner = None

    def __display_game_progress(self):
        grid = list(self.__grid.get_grid())

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                print(grid[row][column], end=" ")
            print()
        print()

    def __display_game_results(self):
        print("Winner: " + self.__winner.name)

        grid = list(self.__grid.get_grid())

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                print(grid[row][column], end=" ")
            print()
        print()

    def __get_coordinates(self):
        grid = list(self.__grid.get_grid())

        ROWS = len(grid)        # number of rows
        COLUMNS = len(grid[0])  # number of columns

        while True:
            try:
                row = get_rows()
                column = get_columns()

                row -= 1
                column -= 1

                if row < ROWS and column < COLUMNS:
                    if grid[row][column] == self.__EMPTY_CELL:
                        return row, column
                    else:
                        raise CellNotEmptyError()
                else:
                    raise InvalidCoordinatesError()
            except CellNotEmptyError as cne:
                print(str(cne))
            except InvalidCoordinatesError as ic:
                print(str(ic))

    def play(self):
        while not self.__gameplay.game_over():
            self.__display_game_progress()

            if self.__last_move == 1:
                print_player_name(self.__player2)

                if type(self.__player2) is Human:
                    row, column = self.__get_coordinates()
                else:
                    row, column = -1, -1

                self.__gameplay.mark(row, column, self.__player2.symbol)
                self.__last_move = 2
            else:
                print_player_name(self.__player1)

                if type(self.__player1) is Human:
                    row, column = self.__get_coordinates()
                else:
                    row, column = -1, -1

                self.__gameplay.mark(row, column, self.__player1.symbol)
                self.__last_move = 1

        if self.__last_move == 1:
            self.__winner = self.__player1
        else:
            self.__winner = self.__player2

        self.__display_game_results()
