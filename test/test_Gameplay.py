import unittest

from repository.Grid import Grid
from service.Gameplay import Gameplay
from service.Strategy import Strategy


class TestGameplay(unittest.TestCase):

    def setUp(self) -> None:
        self.__ROWS = 5
        self.__COLUMNS = 5

        self.__strategy = Strategy()
        self.__grid = Grid(self.__ROWS, self.__COLUMNS)
        self.__gameplay = Gameplay(self.__grid, self.__strategy)

    def tearDown(self) -> None:
        del self.__ROWS
        del self.__COLUMNS
        del self.__grid
        del self.__gameplay

    def test_game_over(self):
        self.assertEqual(self.__gameplay.game_over(), False)

        grid = list(self.__grid.get_grid())

        for row in range(self.__ROWS):
            for column in range(self.__COLUMNS):
                grid[row][column] = "*"

        self.__grid.save(grid)

        self.assertEqual(self.__gameplay.game_over(), True)

    def test_mark(self):
        self.__gameplay.mark(2, 2, "*")

        grid = list(self.__grid.get_grid())

        expected_grid1 = [["_", "_", "_", "_", "_"],
                          ["_", "#", "#", "#", "_"],
                          ["_", "#", "*", "#", "_"],
                          ["_", "#", "#", "#", "_"],
                          ["_", "_", "_", "_", "_"]]

        self.assertEqual(grid, expected_grid1)

        self.__gameplay.mark(0, 0, "*")

        grid = list(self.__grid.get_grid())

        expected_grid2 = [["*", "#", "_", "_", "_"],
                          ["#", "#", "#", "#", "_"],
                          ["_", "#", "*", "#", "_"],
                          ["_", "#", "#", "#", "_"],
                          ["_", "_", "_", "_", "_"]]

        self.assertEqual(grid, expected_grid2)
