import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Where do you go to my lovely", "Peter Sarsted") 

    def test_song_has_a_name(self):
        self.assertEqual ("Where do you go to my lovely", self.song.name)

    def test_artist_has_an_artist(self):
        self.assertEqual ("Peter Sarsted", self.song.artist)