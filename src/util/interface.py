import os
import keyboard
import time
class ListSelector(object):
    def __init__(self, option_list:list[str], message:str = None, confirmation:bool = False):
        self.option_list = option_list
        self.option_index = 0
        self.message = message
        self.confirmation = confirmation

    def activate(self) -> int:
        ready = True

        if self.option_list == [] or self.option_list == None:
            return

        os.system('cls' if os.name == 'nt' else 'clear')
        self.paint()

        while True:
            key_event = keyboard.read_event()

            if key_event.event_type == keyboard.KEY_DOWN and ready and (key_event.name == 'down' or key_event.name == 'right' or key_event.name == 's'):
                if (self.option_index + 1) < len(self.option_list):
                    self.option_index += 1
                    ready = False
            elif key_event.event_type == keyboard.KEY_DOWN and ready and (key_event.name == 'up' or key_event.name == 'left' or key_event.name == 'w'):
                if (self.option_index - 1) >= 0:
                    self.option_index -= 1
                    ready = False
            elif key_event.event_type == keyboard.KEY_DOWN and key_event.name == 'enter':
                flush_input()
                return self.option_index
            
            elif key_event.event_type == keyboard.KEY_UP:
                ready = True
                continue
            else:
                continue

            self.paint()
            

    def paint(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        temp = ""
        if self.message:
            temp += (self.message + "\n" + ("▔" * (len(self.message) + 5)) + "\n")

        for index, option in enumerate(self.option_list):
            if self.option_index == index:
                temp += (f"{'▶':<4}{option}\n")
            else:
                temp += (f" {option}\n")

        print(temp)

def flush_input():
    _ = input()
    