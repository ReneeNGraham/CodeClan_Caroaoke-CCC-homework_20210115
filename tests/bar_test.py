import unittest 
from src.bar import Bar
from src.guest import Guest

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar("TikiBar", 0)
    
    def test_bar_has_name(self):
        self.assertEqual("TikiBar", self.bar.name)

    def test_bar_has_tab(self):
        self.assertEqual(0, self.bar.tab)

  



    