import unittest

from repository.Grid import Grid


class TestGrid(unittest.TestCase):

    def setUp(self) -> None:
        self.__grid = Grid(5, 5)

    def tearDown(self) -> None:
        del self.__grid

    def test_build_grid(self):
        grid = list(self.__grid.get_grid())

        for line in grid:
            print(line)
