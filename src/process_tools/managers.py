from ..util.objects import Process

class Base_manager(object):
    def __init__(self, processes:list[Process]):
        self.processes = processes
        self.process_history:list[int] = []
        self.current_time = 0
        self.process_job()

    def process_job(self):
        return

    def get_process_history(self) -> list[int]:
        return self.process_history
    
    def is_done(self) -> bool:
        return all([i.completed for i in self.processes])
    
    def get_process_stats(self):
        process_data = []
        for i in self.processes:
            # Get First Work Time
            first_occurance = -1
            for time, process_id in enumerate(self.process_history):
                if process_id == i.id:
                    first_occurance = time
                    break
            
            last_occurance = -1
            for time, process_id in enumerate(reversed(self.process_history)):
                if process_id == i.id:
                    last_occurance = len(self.process_history) - time
                    break
            
            # print(f"Process ID: {i.id:<5} Start: {first_occurance:< 5} End: {last_occurance:<5}")
            process_data.append([f"P{i.id}", last_occurance - i.arrival, last_occurance - i.arrival - i.burst])
        
        turnover_sum = 0
        waiting_sum = 0
        for i in process_data:
            turnover_sum += i[1]
            waiting_sum += i[2]
        
        return {"process_data":process_data, "turnover_sum": turnover_sum, "turnover_average": turnover_sum / len(process_data)
                , "waiting_sum": waiting_sum, "waiting_average": waiting_sum / len(process_data)}
        



class Shortest_job_first_preemptive_manager(Base_manager):
    def __init__(self, processes:list[Process]):
        super().__init__(processes)

    def process_job(self):
        while not self.is_done():
            shortest = min([i for i in self.processes if i.is_available(self.current_time)], key = lambda x: x.get_remaining_time(), default = None)

            if shortest != None:
                shortest.make_progress()
                self.process_history.append(shortest.id)
            else:
                self.process_history.append(0)
            
            self.current_time += 1
        
class Priority_first_preemptive_manager(Base_manager):
    def __init__(self, processes:list[Process]):
        super().__init__(processes)

    def process_job(self):
        while not self.is_done():
            priority = min([i for i in self.processes if i.is_available(self.current_time)], key = lambda x: x.priority, default = None)

            if priority != None:
                priority.make_progress()
                self.process_history.append(priority.id)
            else:
                self.process_history.append(0)
            
            self.current_time += 1    
    
    
    
class Shortest_job_first_manager(Base_manager):
    obssession = None
    def __init__(self, processes:list[Process]):
        super().__init__(processes)

    def process_job(self):
        while not self.is_done():
            if self.obssession == None:
                self.obssession = min([i for i in self.processes if i.is_available(self.current_time)], key = lambda x: x.get_remaining_time(), default = None)

            if self.obssession != None:
                self.obssession.make_progress()
                self.process_history.append(self.obssession.id)

                if self.obssession.completed:
                    self.obssession = None
            else:
                self.process_history.append(0)
            
            self.current_time += 1

class First_come_first_serve_manager(Base_manager):
    def __init__(self, processes:list[Process]):
        super().__init__(processes)
    
    def process_job(self):
        while not self.is_done():
            earliest = min([i for i in self.processes if i.is_available(self.current_time)], key = lambda x: x.get_arrival_time(), default = None)

            if earliest != None:
                earliest.make_progress()
                self.process_history.append(earliest.id)
            else:
                self.process_history.append(0)
            
            self.current_time += 1

        
    
