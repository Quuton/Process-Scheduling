from src.process_tools.managers import *
from src.util.objects import Process
from src.util.display import *
from tabulate import tabulate
from src.util.interface import *
from src.util.io import load_process_configuration
import time
import random

AUTHOR_NAME = "David Matthew Antonio"
AUTHOR_SECTION = "BM2"
EXCERCISE_DETAILS = "MP01 - SJF Preemptive"
MPO_FILE_PATH = "MP01 Checker.txt"


def start():
    processes = []
    # Debug stuff
    # processes = [
    #             Process(1, 2, 4, 4),
    #             Process(2, 5, 7, 3),
    #             Process(3, 8, 3, 2),
    #             Process(4, 9, 2, 1),]

    # Im not using this code since i may get grade deduction
    # Ill re-integrate this code once im out of OS LAB

    # selector = ListSelector(["Read from a text file", "Create my processes", "Randomly generate processes"], "Choose an option for setup")
    # choice = selector.activate()

    # if (choice == 0):
    #     processes = [
    #             Process(1, 0, 7, 4),
    #             Process(2, 2, 4, 3),
    #             Process(3, 4, 1, 2),
    #             Process(4, 5, 4, 1),]
    # elif (choice == 1):
    #     print("How many processes do you want to create?")
    # elif (choice == 2):
    #     process_number = numerical_input("How many processes do you want to randomly generate?", 0)
    #     arrival_selector = ListSelector(["Fully Random", "Processes tend to arrive in batches", "All processes arrive at the same time"], "How do you want processes to arrive?")
    #     arrival_config = arrival_selector.activate()
    #     burst_selector = ListSelector(["Fully Random", "Late arival processes tend to take longer", 
    #                                  "Early processes tend to take longer", "Most processes are short but a few are large outliers", 
    #                                  "All processes take the same amount of time"], "How long should processes take?")
    #     burst_config = burst_selector.activate()  

    #     arrival_values = [0]
    #     if (arrival_config == 0):
    #         for i in range(process_number - 1):
    #             arrival_values.append(random.randint(0,20))
    #     elif (arrival_config == 1):
    #         for i in range(process_number - 1):
    #             if (bool(random.getrandbits(1))):
    #                 arrival_values.append(arrival_values[i])
    #             else:
    #                 arrival_values.append(arrival_values[i] + random.randint(0,5))
    #     else:
    #         for i in range(process_number - 1):
    #             arrival_values.append(0)


    #     burst_values = []
    #     if (burst_config == 0):
    #         for i in range(process_number):
    #             burst_values.append(random.randint(1,10))
    #     elif (burst_config == 1):
    #         burst_values.append(random.randint(1,3))
    #         for i in range(process_number - 1):
    #             burst_values.append(burst_values[i] + random.randint(1,3))
    #     elif (burst_config == 2):
    #         burst_values.append(int(random.randint(3,5) * process_number + random.randint(0,5)))
    #         for i in range(process_number - 1):
    #             burst_values.append(int(burst_values[i] * random.randint(0, 5) * 0.1))
    #     else:
    #         for i in range(process_number):
    #             burst_values.append(5)

    #     processes = [Process(i+1, arrival_values[i], burst_values[i]) for i in range(process_number)]
    
    processes = load_process_configuration(MPO_FILE_PATH)
    print(f"Programmed by: {AUTHOR_NAME}")
    print(EXCERCISE_DETAILS)
    print('\n', end=None)

    print(list_process_values(processes))
    
    manager = Shortest_job_first_preemptive_manager(processes)


    clustered_history = clusterise_process_history(manager.get_process_history())
    print("Gannt Chart")
    print(create_process_gannt_chart(clustered_history, True))
    stats = manager.get_process_stats()
    table_data = stats.get("process_data")
    table_data.append(["TOTAL", stats.get('turnover_sum', 0), stats.get('waiting_sum', 0)])
    table_data.append(["AVERAGE", stats.get('turnover_average', 0), stats.get('waiting_average', 0)])
    print("Table")
    print(tabulate(table_data, headers = ["PROCESS", "TURNAROUND TIME", "WAITING TIME"], tablefmt = "simple_grid", colalign = ["center", "center", "center"]))
    # print(f"Total Turnover Time: {stats.get('turnover_sum', 0)}")
    # print(f"Average Turnover Time: {stats.get('turnover_average', 0)}")
    # print(f"Total Waiting Time: {stats.get('waiting_sum', 0)}")
    # print(f"Average Waiting Time: {stats.get('waiting_average', 0)}")




    # Set the content to write to MPO Checker
    processs_config = get_mpo_process_lines(MPO_FILE_PATH)
    header = f"Programmed by: {AUTHOR_NAME}\n{EXCERCISE_DETAILS}"
    process_information = list_process_values(processes)



    gannt_chart_text = "Gannt Chart\n" + create_process_gannt_chart(clustered_history) 
    table_text = "Table\n" + tabulate(table_data, headers = ["PROCESS", "TURNAROUND TIME", "WAITING TIME"], tablefmt = "grid", colalign = ["center", "center", "center"])

    mpo_checker_output(MPO_FILE_PATH, processs_config, header, process_information, gannt_chart_text, table_text)