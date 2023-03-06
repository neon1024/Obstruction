from domain.Computer import Computer
from domain.Human import Human
from repository.Grid import Grid
from service.Gameplay import Gameplay
from service.Strategy import Strategy
from ui.Game import Game
from ui.functions import get_name, human_is_player1, get_rows, get_columns


def main():
    PLAYER1_SYMBOL = "X"
    PLAYER2_SYMBOL = "0"
    COMPUTER_NAME = "Computer"

    name = get_name()

    if human_is_player1():
        player1 = Human(PLAYER1_SYMBOL, name)
        player2 = Computer(PLAYER2_SYMBOL, COMPUTER_NAME)
    else:
        player1 = Computer(PLAYER1_SYMBOL, COMPUTER_NAME)
        player2 = Human(PLAYER2_SYMBOL, name)

    print("Generating the grid...")
    rows = get_rows()
    columns = get_columns()

    grid = Grid(rows, columns)
    strategy = Strategy(grid)
    gameplay = Gameplay(grid, strategy)
    game = Game(gameplay, grid, player1, player2)
    game.play()


if __name__ == "__main__":
    main()
