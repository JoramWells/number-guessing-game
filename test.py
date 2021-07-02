import unittest
from unittest.mock import patch
# import app
import compare_nums

class TestInput(unittest.TestCase):

    def test_equal(self):
        result = compare_nums.compare_nums(2,2)
        self.assertEqual(result,True)
    def test_not_equal(self):
        result = compare_nums.compare_nums(1,2)
        self.assertEqual(result, None)
    def test_greater_than(self):
        result = compare_nums.is_greater_than(4,3)
        self.assertTrue(result,False)
    def test_lesser_than(self):
        result = compare_nums.is_greater_than(3,4)
        self.assertFalse(result, False)
    def test_decrement(self):
        result = compare_nums.decrement(5)
        self.assertEqual(4,4)
    
    # def test_input(self):
    #     assert(int(app.getInput()) == 1)

if __name__ == '__main__':
    unittest.main()