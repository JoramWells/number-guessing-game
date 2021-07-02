import compare_nums


input_phone = "+254799980846"


#Check if answer == input; return True
def test_equal(self):
    result = compare_nums.compare_nums(2,2)
    self.assertEqual(result,True)


# Check if input != answer
def test_not_equal(self):
    result = compare_nums.compare_nums(1,2)
    self.assertEqual(result, None)


#Check if input > answer
def test_greater_than(self):
    result = compare_nums.is_greater_than(4,3)
    self.assertTrue(result,False)


def test_lesser_than(self):
    result = compare_nums.is_greater_than(3,4)
    self.assertFalse(result, False)


# Check decrement func
def test_decrement(self):
    result = compare_nums.decrement(5)
    self.assertEqual(4,4)


def test_input_pass(self):
    assert(int(input("Input greater than or equal to 0: ")) >= 0)


def test_input_fail(self):
    assert(int(input("Input lesser than 0: ")) < 0)


#Check phone number length
def test_phone_number_length(self):
    assert(len(input_phone) == 13)

#Check if phone number digits
def test_phone_number_digits(self):
    phone = "254799980846"
    assert(input_phone[1:]==phone)
    assert(phone.isdigit() == True)

if __name__ == '__main__':
    unittest.main()
