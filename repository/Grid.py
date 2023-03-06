class Grid:

    def __init__(self, rows, columns):
        self.__grid = self.__build_grid(rows, columns)

    @staticmethod
    def __build_grid(rows, columns):
        grid = []

        for row in range(rows):
            line = []
            for column in range(columns):
                line.append("_")
            grid.append(line[:])

        return grid

    def save(self, updated_grid):
        self.__grid = updated_grid

    def get_grid(self):
        return self.__grid
