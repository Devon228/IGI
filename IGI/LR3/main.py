'''
Laboratory work number: 3. Standard data types, collections, functions, modules.
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.03.2026.

This module contains main menu allowing to select task from laboratory work.
'''



import task1
import task2
import task3
import task4
import task5
import ui


def show_menu():
    '''
    Shows main menu of program.
    '''
    print('-' * 70)
    print('Main menu of lab work 3'.center(70))
    print('-'*70)
    print("1. Task 1 = ln(1 - x) approximation")
    print("2. Task 2 = loop for subtraction")
    print("3. Task 3 = Count \' \' and \',\' in string")
    print("4. Task 4 = Text analysis")
    print("5. Task 5 = List analysis")
    print("0. Exit")


def main():
    '''
    Entry point of all tasks, allows to choose a task.
    '''
    while True:
        show_menu()
        option = ui.read_int("Enter a number of option to run\n", min=0, max=5)
        match option:
            case 1:
                task1.main()
            case 2:
                task2.main()
            case 3:
                task3.main()
            case 4:
                task4.main()
            case 5:
                task5.main()
            case 0:
                print("Goodbye.")
                break


if __name__ == "__main__":
    main()