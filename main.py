from src.process_tools.managers import *
from src.util.objects import Process
from src.util.display import *
from tabulate import tabulate
from src.util.interface import *
from src.app import start
import time
import random



def main():
    while True:
        start()

        choice = input("Do you want to retry? [Y/N]")

        while True:
            if (choice == 'Y' or choice == 'y'):
                break
            elif (choice == 'N' or choice == 'n'):
                exit()
            else:
                print("Choice invalid")
                continue
    



if __name__ == "__main__":
    main()