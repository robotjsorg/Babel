class Server:
    def __init__(self, name, paid=False):
        self.name = name
        self.paid = False
    
    def payMonthly(self) -> bool:
        # api call with stripe perhaps
        if pay $5 monthly:
            self.paid = True
        
        if self.paid:
            return True
        else:
            return False
