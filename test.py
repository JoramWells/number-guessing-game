import unittest
from unittest.mock import patch
import app

class TestInput(unittest.TestCase):
    
    def test_input(self):
        assert(int(app.getInput()) == 1)