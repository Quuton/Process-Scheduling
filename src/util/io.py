from msvcrt import getch,kbhit
from src.util.objects import Process
import time

def flush_input():
    # _ = input()
    while kbhit(): 
        getch()

def load_process_configuration(path:str) ->  list[Process]:
    processes = []
    string_data = []
    try:
        with open(path, 'r') as file:
            string_data = [line.strip() for line in file.readlines()]
        
        arrival_values = [int(i) for i in string_data[1].split(' ')]
        burst_values = [int(i) for i in string_data[2].split(' ')]
        priority_values = [int(i) for i in string_data[3].split(' ')]

        for index in range(int(string_data[0])):
            processes.append(Process(index+1, arrival_values[index], burst_values[index], priority_values[index]))

    except Exception:
        print("There is something wrong with the file format, aborting...")
        time.sleep(2)
        exit()
    
    return processes

def get_mpo_process_lines(path:str) -> str:
    string_list = []
    string_data = ""
    
    with open(path, 'r') as file:
        string_list = [line for line in file.readlines()]
        string_list = string_list[:4]

    for i in string_list:
        string_data += i
    
    return string_data
    

def mpo_checker_output(path:str, *args:str):
    string_data = ""
    for i in args:
        string_data += (i + '\n')
    
    with open(path, 'w') as file:
        file.write(string_data)





