from msvcrt import getch,kbhit

def flush_input():
    # _ = input()
    while kbhit(): 
        getch()