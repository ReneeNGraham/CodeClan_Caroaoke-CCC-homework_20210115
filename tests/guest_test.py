import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Ben Ramone")
      
    def test_guest_has_a_name(self):
        self.assertEqual ("Ben Ramone", self.guest.name)
