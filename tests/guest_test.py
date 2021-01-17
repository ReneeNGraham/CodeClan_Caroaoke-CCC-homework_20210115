import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Ben Ramone", 20.00, "Simply The Best")
        self.room = Room("Singalong Room", 10.00, 4)


    def test_guest_has_a_name(self):
        self.assertEqual("Ben Ramone", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(20.00, self.guest.wallet)

    def test_guest_has_fav_song(self):
        self.assertEqual("Simply The Best", self.guest.fav_song)
    
    def test_guest_can_pay_entrance_fee(self):
        room = Room("Singalong Room", 10, 4)
        self.guest.pay_room(room)
        self.assertEqual(10, self.guest.wallet)
     

        
