from msvcrt import getch,kbhit
from src.util.objects import Process

def flush_input():
    # _ = input()
    while kbhit(): 
        getch()

def load_process_configuration(path:str) ->  list[Process]:
    processes = []
    string_data = []
    with open(path, 'r') as file:
        string_data = [line.strip() for line in file.readlines()]
    
    burst_values = [int(i) for i in string_data[1].split(' ')]
    arrival_values = [int(i) for i in string_data[2].split(' ')]
    priority_values = [int(i) for i in string_data[3].split(' ')]

    for index in range(int(string_data[0])):
        processes.append(Process(index+1, arrival_values[index], burst_values[index], priority_values[index]))

    return processes