from ..util.objects import Process

class Base_manager():
    def __init__(self, processes:list[Process]):
        self.processes = processes
    

class Shortest_job_first_manager(Base_manager):
    def __init__(self, processes:list[Process]):
        super(processes)

    def process_job(self) -> int:
        shortest = min(self.processes, key = lambda x: x.get_remaining_time())
        shortest.make_progress()
        return shortest.id
    
