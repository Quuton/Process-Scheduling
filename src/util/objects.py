class Process():
    def __init__(self, id:int, arrival:int, burst:int, priority:int = -1):
        self.id = id
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.completed = False    
        self.progress = 0

    def terminate(self):
        self.completed = True

    def get_remaining_time(self):
        return self.burst - self.progress
    
    def get_arrival_time(self):
        return self.arrival

    def make_progress(self):
        # The redundancy looks ugly, how to fix this?
        if self.progress < self.burst:
            self.progress += 1
        else:
            self.completed = True
            
        if self.progress >= self.burst:
            self.completed = True

    def is_available(self, current_time:int) -> bool:
        return ((not self.completed) and (self.arrival <= current_time))

    

    