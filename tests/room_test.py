import unittest

from src.room import Room
from src.guest import Guest 
from src.song import Song 

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Singalong Room", 10.00, 4)
        self.guest = Guest("Benjamin Button", 20.00, "Simply The Best")
        self.fav_song = Song("Simply The Best", "Tina Turner")

    def test_room_has_a_name(self):
        self.assertEqual ("Singalong Room", self.room.name)

    def test_room_a_capacity(self):
        self.assertEqual(4,self.room.room_capacity)

    def test_start_room_no_guests(self):
        self.assertEqual(0, len(self.room.guests))

    def test_add_a_guest_to_room(self):
        self.room.add_guest(self.guest)
        self.assertEqual (1, len(self.room.guests))

    def test_remove_guest_from_room(self):
        self.room.add_guest(self.guest)
        self.room.remove_guest(self.guest)
        self.assertEqual (0, len (self.room.guests))

    def test_start_room_with_no_songs(self):
        self.assertEqual(0, len(self.room.songs))

    def add_songs_to_room(self):
        self.song = Song("Where do you go to my lovely", "Peter Sarstedt")
        self.room.add_song(self.song)
        self.assertEqual (1, len(self.room.songs))
    
    def test_room_has_entrance_price(self):
        self.assertEqual(10.00, self.room.price)
    
    def test_guest_cannot_enter_if_room_capacity_reached(self):
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest)
        self.assertEqual(4, self.room.guest_count())

    def test_play_fav_song(self):
        self.room.add_song(self.fav_song)
        self.assertEqual("Simply The Best", self.guest.fav_song)

    
