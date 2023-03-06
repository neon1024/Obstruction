from domain.Human import Human


def get_name():
    name = input("Your Name: ")

    return name


def human_is_player1():
    while True:
        answer = input("Do you want to be player1 ? [y/n]: ")

        if answer == "y":
            return True
        elif answer == "n":
            return False

        print("[!] Invalid answer")


def get_rows():
    while True:
        rows = input("Rows: ")

        if not rows.isnumeric():
            print("[!] Invalid input")
        elif int(rows) > 0:
            return int(rows)
        else:
            print("[!] Invalid input")


def get_columns():
    while True:
        columns = input("Columns: ")

        if not columns.isnumeric():
            print("[!] Invalid input")
        elif int(columns) > 0:
            return int(columns)
        else:
            print("[!] Invalid input")


def print_player_name(player):
    if type(player) is Human:
        print("Your move...")
    else:
        print("Computer's move...")
