import unittest
from unittest.mock import patch
# import app
import compare_nums

class TestInput(unittest.TestCase):

    def test_equal(self):
        result = compare_nums.compare_nums(2,2)
        self.assertEqual(result,True)
    
    # def test_input(self):
    #     assert(int(app.getInput()) == 1)

if __name__ == '__main__':
    unittest.main()