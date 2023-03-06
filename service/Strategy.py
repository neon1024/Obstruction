import random


class Strategy:

    def __init__(self, grid):
        self.__grid = grid
        self.__EMPTY_CELL = "_"

    def get_coordinates(self, grid):
        return self.get_coordinates_that_marks_the_most_positions(grid)

    def get_random_coordinates(self, grid):
        ROWS = len(grid)  # number of rows
        COLUMNS = len(grid[0])  # number of columns

        while True:
            row = random.randint(0, ROWS - 1)
            column = random.randint(0, COLUMNS - 1)

            if grid[row][column] == self.__EMPTY_CELL:
                return row, column

    def get_number_of_surrounding_empty_cells(self, grid, row, column):
        ROWS = len(grid)  # number of rows
        COLUMNS = len(grid[0])  # number of columns

        number_of_surrounding_empty_cells = 0

        if row - 1 >= 0 and column - 1 >= 0:
            if grid[row - 1][column - 1] == self.__EMPTY_CELL:
                number_of_surrounding_empty_cells += 1

        if row - 1 >= 0:
            if grid[row - 1][column] == self.__EMPTY_CELL:
                number_of_surrounding_empty_cells += 1

        if row - 1 >= 0 and column + 1 < COLUMNS:
            if grid[row - 1][column + 1] == self.__EMPTY_CELL:
                number_of_surrounding_empty_cells += 1

        if column - 1 >= 0:
            if grid[row][column - 1] == self.__EMPTY_CELL:
                number_of_surrounding_empty_cells += 1

        if column + 1 < COLUMNS:
            if grid[row][column + 1] == self.__EMPTY_CELL:
                number_of_surrounding_empty_cells += 1

        if row + 1 < ROWS and column - 1 >= 0:
            if grid[row + 1][column - 1] == self.__EMPTY_CELL:
                number_of_surrounding_empty_cells += 1

        if row + 1 < ROWS:
            if grid[row + 1][column] == self.__EMPTY_CELL:
                number_of_surrounding_empty_cells += 1

        if row + 1 < ROWS and column + 1 < COLUMNS:
            if grid[row + 1][column + 1] == self.__EMPTY_CELL:
                number_of_surrounding_empty_cells += 1

        return number_of_surrounding_empty_cells

    def get_coordinates_that_marks_the_most_positions(self, grid):
        # traverse the grid, check how many empty cells surround the current position, save the number into a variable
        # update the maximum after each position traversed, save the position
        maximum_number_of_surrounding_empty_cells = 0
        target_position = {"row": 0, "column": 0}

        ROWS = len(grid)  # number of rows
        COLUMNS = len(grid[0])  # number of columns

        for row in range(ROWS):
            for column in range(COLUMNS):
                number_of_surrounding_empty_cells = self.get_number_of_surrounding_empty_cells(grid, row, column)
                if number_of_surrounding_empty_cells > maximum_number_of_surrounding_empty_cells:
                    maximum_number_of_surrounding_empty_cells = number_of_surrounding_empty_cells
                    target_position["row"] = row
                    target_position["column"] = column

        return target_position["row"], target_position["column"]
