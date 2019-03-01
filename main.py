#importes
import sys, exercise1, exercise2, exercise3, exercise4, exercise5
from easygui import *


def main_menu():
    while True:
        option = buttonbox("1. Analize one sequence\n\n2. Analize several sequences\n\n3. Align sequences"
                           "\n\n4. Operation with files containing sequences\n\n5. Visualize","Main Menu",
                           choices=["1", "2", "3", "4", "5", "Exit"])
        if option == "1": exercise1.menu_exercise_1()
        if option == "2": print("ir po menu 1")
        if option == "3": print("ir po menu 1")
        if option == "4": print("ir po menu 1")
        if option == "5": print("ir po menu 1")
        if option == "Exit": sys.exit()


if __name__ == '__main__':
    main_menu()