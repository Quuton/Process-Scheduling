from .objects import Process
from itertools import groupby
from .string_tools import *

MINIMUM_SIZE = 6
MAXIMUM_SIZE = 26
SIZE_RANGE = MAXIMUM_SIZE - MINIMUM_SIZE
EMPTY_STRING = ""


def clusterise_process_history(processes:list[int]):
    clusters = []
    current_cluster = [processes[0], 1]

    for i in range(1, len(processes)):
        if processes[i] == current_cluster[0]:
            current_cluster[1] += 1
        else:
            clusters.append(current_cluster)
            current_cluster = [processes[i], 1]

    clusters.append(current_cluster)
    return clusters
        
def create_process_gannt_chart(clsuterised_process_history:list[list], unicode_support:bool = False):
    if unicode_support:
        UPPER_LEFT_CORNER = '┌'
        UPPER_RIGHT_CORNER = '┐'
        MIDDLE_WALL = '│'
        MIDDLE_RBRANCH_CONNECTOR = '├'
        MIDDLE_LBRANCH_CONNECTOR = '┤'
        CROSS_CONNECTOR = '┼'
        T_SHAPE_CONNECTOR = '┬'
        STRAIGHT_CONNECTOR = '─'
    else:
        UPPER_LEFT_CORNER = '+'
        UPPER_RIGHT_CORNER = '+'
        MIDDLE_WALL = '|'
        MIDDLE_RBRANCH_CONNECTOR = '+'
        MIDDLE_LBRANCH_CONNECTOR = '+'
        CROSS_CONNECTOR = '+'
        T_SHAPE_CONNECTOR = '+'
        STRAIGHT_CONNECTOR = '-'

    minimum_time_block = min([i[1] for i in clsuterised_process_history])
    maximum_time_block = max([i[1] for i in clsuterised_process_history])
    
    def calculate_proportion(value, min, max, size_range):
        if (max != min):
            return int((value - min) * size_range/(max - min))
        else:
            return 0

    ceiling = f"{UPPER_LEFT_CORNER}"
    middle = f"{MIDDLE_WALL}"
    bottom = f"{MIDDLE_RBRANCH_CONNECTOR}"
    label = "0"

    # Body of the Gannt Chart
    for i in clsuterised_process_history[:-1]:
        difference = calculate_proportion(i[1], minimum_time_block, maximum_time_block, SIZE_RANGE)
        ceiling += f"{STRAIGHT_CONNECTOR * MINIMUM_SIZE}{EMPTY_STRING:{STRAIGHT_CONNECTOR}<{difference}}{T_SHAPE_CONNECTOR}"
        bottom += f"{STRAIGHT_CONNECTOR * MINIMUM_SIZE}{EMPTY_STRING:{STRAIGHT_CONNECTOR}<{difference}}{CROSS_CONNECTOR}"

    time_count = 0
    for i in clsuterised_process_history:
        difference = calculate_proportion(i[1], minimum_time_block, maximum_time_block, SIZE_RANGE)
        if (i[0] == 0):
            middle += f"{'IDLE':^{MINIMUM_SIZE + difference}}{MIDDLE_WALL}"
        else:
            middle += f"{'P' + str(i[0]):^{MINIMUM_SIZE + difference}}{MIDDLE_WALL}"



        time_count += i[1]
        label += f"{time_count:>{MINIMUM_SIZE + difference + 1}}"


    # Closing of the Gannt Chart
    difference = calculate_proportion(clsuterised_process_history[-1][-1], minimum_time_block, maximum_time_block, SIZE_RANGE)
    ceiling += f"{STRAIGHT_CONNECTOR * MINIMUM_SIZE}{EMPTY_STRING:{STRAIGHT_CONNECTOR}<{difference}}{UPPER_RIGHT_CORNER}"
    bottom += f"{STRAIGHT_CONNECTOR * MINIMUM_SIZE}{EMPTY_STRING:{STRAIGHT_CONNECTOR}<{difference}}{MIDDLE_LBRANCH_CONNECTOR}"

    return join_all_strings(ceiling, middle, bottom, label)

def list_process_values(processes:list[Process]) -> str:
    string_data = ""
    string_data += (f"No. of Processes: {len(processes)}\n")
    string_data += ("Arrival Time: \n")
    for process in processes:
        string_data += (f"P{process.id}: {process.arrival}\n")
    string_data += ("\n")

    string_data += ("Burst Time: \n")
    for process in processes:
        string_data += (f"P{process.id}: {process.burst}\n")
    string_data += ("\n")

    string_data += ("Priority Number: \n")
    for process in processes:
        string_data += (f"P{process.id}: {process.priority}\n")
    string_data += ("\n")

    return string_data