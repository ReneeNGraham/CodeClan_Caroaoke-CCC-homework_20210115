class Room:

    def __init__(self, name, price, room_capacity):
        self.name = name
        self.guests = []
        self.songs = []
        self.price = price 
        self.room_capacity = room_capacity
     
    def add_guest(self, guest):
        self.guests.append(guest)
 
    def remove_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)

    def guest_count(self):
        return len(self.guests)

    def room_capacity(self):
      if guest_count < 4:
          return "There is still room here"
      elif guest_count >= 4:
         retrun: "room capcity reached"

    def play_fav_song(self):
      fav_song = "Simply The Best", "Tina Turner"
      if song == fav_song:
           return "Whoo"
      else:
            "Try again"


    