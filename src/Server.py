from collections import deque

class Server:
    def __init__(self, name: str, language: str):
        self.name = name
        self.language = language
        self.events = deque()
        self.paid = False
    
    def addEvent(self, event: str):
        self.events.append(event)
