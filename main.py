from src.process_tools.managers import *
from src.util.display import *
from src.util.interface import *
from src.app import start



def main():
    while True:
        start()

    
        while True:
            choice = input("Do you want to retry? [Y/N]")
            if (choice == 'Y' or choice == 'y'):
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            elif (choice == 'N' or choice == 'n'):
                exit()
            else:
                print("Choice invalid")
                continue
    



if __name__ == "__main__":
    main()