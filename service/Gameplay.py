class Gameplay:

    def __init__(self, grid, computer_strategy):
        self.__grid = grid
        self.__computer_strategy = computer_strategy
        self.__EMPTY_CELL = "_"
        self.__MARKING_SYMBOL = "#"

    def game_over(self):
        # game is over if there are no more empty cells
        grid = list(self.__grid.get_grid())

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == self.__EMPTY_CELL:  # game not over
                    return False

        return True

    def mark(self, row, column, symbol):
        grid = list(self.__grid.get_grid())

        ROWS = len(grid)  # number of rows
        COLUMNS = len(grid[0])  # number of columns

        if row == -1 and column == -1:
            row, column = self.__computer_strategy.get_coordinates(grid)

        grid[row][column] = symbol

        if row - 1 >= 0 and column - 1 >= 0:
            if grid[row - 1][column - 1] == self.__EMPTY_CELL:
                grid[row - 1][column - 1] = self.__MARKING_SYMBOL

        if row - 1 >= 0:
            if grid[row - 1][column] == self.__EMPTY_CELL:
                grid[row - 1][column] = self.__MARKING_SYMBOL

        if row - 1 >= 0 and column + 1 < COLUMNS:
            if grid[row - 1][column + 1] == self.__EMPTY_CELL:
                grid[row - 1][column + 1] = self.__MARKING_SYMBOL

        if column - 1 >= 0:
            if grid[row][column - 1] == self.__EMPTY_CELL:
                grid[row][column - 1] = self.__MARKING_SYMBOL

        if column + 1 < COLUMNS:
            if grid[row][column + 1] == self.__EMPTY_CELL:
                grid[row][column + 1] = self.__MARKING_SYMBOL

        if row + 1 < ROWS and column - 1 >= 0:
            if grid[row + 1][column - 1] == self.__EMPTY_CELL:
                grid[row + 1][column - 1] = self.__MARKING_SYMBOL

        if row + 1 < ROWS:
            if grid[row + 1][column] == self.__EMPTY_CELL:
                grid[row + 1][column] = self.__MARKING_SYMBOL

        if row + 1 < ROWS and column + 1 < COLUMNS:
            if grid[row + 1][column + 1] == self.__EMPTY_CELL:
                grid[row + 1][column + 1] = self.__MARKING_SYMBOL

        self.__grid.save(grid)
