class Room:

    def __init__(self, name):
        self.name = name
        self.guests = []
     
    def add_guest(self, guest):
        self.guests.append(guest)
 

