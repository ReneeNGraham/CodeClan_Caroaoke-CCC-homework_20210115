class Guest:

    def __init__(self, name, wallet, fav_song):
        self.name = name 
        self.wallet = wallet 
        self.fav_song = fav_song
  
    def pay_room(self,room):
        self.wallet -= room.price
