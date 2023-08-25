class Process():
    def __init__(self, id:int, arrival:int, burst:int):
        self.id = id
        self.arrival = arrival
        self.burst = burst
        self.completed = False    
        self.progress = 0

    def terminate(self):
        self.completed = True

    def get_remaining_time(self):
        return self.burst - self.progress

    def make_progress(self):
        if self.progress < self.burst:
            self.progress += 1
        
        if self.progress >= self.burst:
            self.completed = True

    

    