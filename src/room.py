class Room:

    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs = []
     
    def add_guest(self, guest):
        self.guests.append(guest)
 
    def remove_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)