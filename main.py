from src.process_tools.managers import *
from src.util.objects import Process
from src.util.display import *
from tabulate import tabulate
from src.util.interface import *
from src.app import start
import time
import random

AUTHOR_NAME = "David Matthew Antonio"
AUTHOR_SECTION = "BM2"

def main():
    print(f"Author Name: {AUTHOR_NAME}, Section: {AUTHOR_SECTION}")
    start()
    _ = input("Press enter to exit")



if __name__ == "__main__":
    main()