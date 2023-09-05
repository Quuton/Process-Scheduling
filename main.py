from src.process_tools.managers import *
from src.util.objects import Process
from src.util.display import *
from tabulate import tabulate
from src.util.interface import *
import time
import random

AUTHOR_NAME = "David Matthew Antonio"
AUTHOR_SECTION = "BM2"

def main():
    processes = []
    print(f"Author Name: {AUTHOR_NAME}, Section: {AUTHOR_SECTION}")

    selector = ListSelector(["Read from a text file", "Create my processes", "Randomly generate processes"], "Choose an option for setup")
    choice = selector.activate()

    if (choice == 0):
        processes = [
                Process(1, 0, 10, 2),
                Process(2, 3, 10, 3),
                Process(3, 6, 10, 4),
                Process(4, 12, 10, 5),
                Process(5, 16, 10, 6),
                Process(6, 21, 10, 7)]
    elif (choice == 1):
        print("How many processes do you want to create?")
    elif (choice == 2):
        process_number = numerical_input("How many processes do you want to randomly generate?", 0)
        arrival_selector = ListSelector(["Fully Random", "Processes tend to arrive in batches", "All processes arrive at the same time"], "How do you want processes to arrive?")
        arrival_config = arrival_selector.activate()
        burst_selector = ListSelector(["Fully Random", "Late arival processes tend to take longer", 
                                     "Early processes tend to take longer", "Most processes are short but a few are large outliers", 
                                     "All processes take the same amount of time"], "How long should processes take?")
        burst_config = burst_selector.activate()  

        arrival_values = [0]
        if (arrival_config == 0):
            for i in range(process_number - 1):
                arrival_values.append(random.randint(0,20))
        elif (arrival_config == 1):
            for i in range(process_number - 1):
                if (bool(random.getrandbits(1))):
                    arrival_values.append(arrival_values[i])
                else:
                    arrival_values.append(arrival_values[i] + random.randint(0,5))
        else:
            for i in range(process_number - 1):
                arrival_values.append(0)


        burst_values = []
        if (burst_config == 0):
            for i in range(process_number):
                burst_values.append(random.randint(1,10))
        elif (burst_config == 1):
            burst_values.append(random.randint(1,3))
            for i in range(process_number - 1):
                burst_values.append(burst_values[i] + random.randint(1,3))
        elif (burst_config == 2):
            burst_values.append(int(random.randint(3,5) * process_number + random.randint(0,5)))
            for i in range(process_number - 1):
                burst_values.append(int(burst_values[i] * random.randint(0, 5) * 0.1))
        else:
            for i in range(process_number):
                burst_values.append(5)

        processes = [Process(i+1, arrival_values[i], burst_values[i]) for i in range(process_number)]




    # TEMPORARY TESTING, REMOVE THIS SHIT
    
    manager = Priority_first_preemptive_manager(processes)


    clustered_history = clusterise_process_history(manager.get_process_history())
    print(create_process_gannt_chart(clustered_history)) 
    stats = manager.get_process_stats()
    print(tabulate(stats.get("process_data"), headers = ["Process ID", "Turnover Time", "Waiting Time"], tablefmt = "rounded_grid", colalign = ["center", "center", "center"]))
    print(f"Total Turnover Time: {stats.get('turnover_sum', 0)}")
    print(f"Average Turnover Time: {stats.get('turnover_average', 0)}")
    print(f"Total Waiting Time: {stats.get('waiting_sum', 0)}")
    print(f"Average Waiting Time: {stats.get('waiting_average', 0)}")



if __name__ == "__main__":
    main()