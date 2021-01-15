import unittest

from src.room import Room
from src.guest import Guest 
from src.song import Song 

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("funky Baby")
        self.guest = Guest("Benjamin Button")
      

    def test_room_has_a_name(self):
        self.assertEqual ("funky Baby", self.room.name)

    def test_start_room_no_guests(self):
        self.assertEqual(0, len(self.room.guests))

    def test_add_a_guest_to_room(self):
        self.room.add_guest(self.guest)
        self.assertEqual (1, len(self.room.guests))
