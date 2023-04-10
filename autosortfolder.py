from repeatedtimer import RepeatedTimer
from sortingmethod import SortingMethod
from filesorter import FileSorter
from helpers import check_for_directory
from os import listdir
from sys import exit
from sortingalgorithms import SORTING_METHODS

class AutoSortFolder:
    def __init__(self, root:str, update_interval:int=1):
        self.root       = root
        self._timer     = RepeatedTimer(update_interval, self._root_update)
        self._sorter    = FileSorter(self.root)

    def print_methods(self):
        print("--SORTING METHODS--")
        for i, method in enumerate(SORTING_METHODS):
            print(f"{i+1}) {method.name}")
        print(f"{i+2}) Back")

    def main_menu(self):
        while True:
            print("--MAIN MENU--\n1) Select Sorting Method\n2) Start\n3) Quit")
            userInput = input(">> ")
            match (userInput):
                case "1":
                    self.menu_sorting_methods()
                case "2":
                    if self._sorter.method != None:
                        break
                    else:
                        print("ERROR: No sorting method selected.")
                case "3":
                    exit()
                case _:
                    print("ERROR: Please choose one of the options above.")
    
    def menu_sorting_methods(self):
        self.print_methods()
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
                    self.menu_custom_sorting()
                    self._sorter.method = SORTING_METHODS[3]
                    break
                case "5":
                    break
                case _:
                    print("ERROR: Please choose one of the options above.")

        # Create Main Method Folder
        if self._sorter.method != None:
            check_for_directory(f"{self.root}/{self._sorter.method.name.lower()}")
    
    def menu_custom_sorting(self):
        pass

    def _root_update(self):
        for file in listdir(self.root):
            if not self._sorter.sort_file(self.root, f"{self.root}/{file}"):
                print("Attempted to sort off-limits file.")
            else:
                print(f"Sorted file '{file}'.")

        print("Updated root!")

    def run(self):
        self.main_menu()    # Start the menu of the program
        print(f"Sorting by: {self._sorter.method.name}")

        self._timer.start() # Start the update timer