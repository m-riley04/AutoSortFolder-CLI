from repeatedtimer import RepeatedTimer
from sortingmethod import SortingMethod
from filesorter import FileSorter
from helpers import check_for_directory
from os import listdir
from sys import exit
from sortingalgorithms import SORTING_METHODS
import logging

class AutoSortFolder:
    def __init__(self, root:str, update_interval:int=1):
        self.root       = root
        self._timer     = RepeatedTimer(update_interval, self._root_update)
        self._sorter    = FileSorter(self.root)

    def _print_methods(self):
        print("--SORTING METHODS--")
        for i, method in enumerate(SORTING_METHODS):
            print(f"{i+1}) {method.name}")
        print(f"{i+2}) Back")

    def _main_menu(self):
        while True:
            print("--MAIN MENU--\n1) Select Sorting Method\n2) Start\n3) Quit")
            userInput = input(">> ")
            match (userInput):
                case "1":
                    self._menu_sorting_methods()
                case "2":
                    if self._sorter.method != None:
                        break
                    else:
                        print("ERROR: No sorting method selected.")
                case "3":
                    exit()
                case _:
                    print("ERROR: Please choose one of the options above.")
    
    def _menu_sorting_methods(self):
        self._print_methods()
        while True:
            userInput = input(">> ")
            match (userInput):
                case "1":
                    self._sorter.method = SORTING_METHODS[0]
                    break
                case "2":
                    self._sorter.method = SORTING_METHODS[1]
                    break
                case "3":
                    self._sorter.method = SORTING_METHODS[2]
                    break
                case "4":
                    self._menu_custom_sorting()
                    self._sorter.method = SORTING_METHODS[3]
                    break
                case "5":
                    break
                case _:
                    print("ERROR: Please choose one of the options above.")

        # Create Main Method Folder
        if self._sorter.method != None:
            check_for_directory(f"{self.root}/{self._sorter.method.name.lower()}")
    
    def _menu_custom_sorting(self):
        pass

    def _root_update(self):
        '''Updates the root directory'''
        for file in listdir(self.root):
            if not self._sorter.sort_file(self.root, f"{self.root}/{file}"):
                logging.debug(msg="Attempted to sort off-limits file.")
            else:
                logging.debug(msg=f"Sorted file '{file}'.")

        logging.debug("Updated root!")

    def run(self):
        self._main_menu()    # Start the menu of the program
        print(f"Sorting by: {self._sorter.method.name}")

        self._timer.start() # Start the update timer