from python import compare_nums


input_phone = "+254799980846"


# #Check if answer == input; return True
# def test_equal():
#     result = compare_nums.compare_nums(2,2)
#     assertEqual(result,True)


# # Check if input != answer
# def test_not_equal():
#     result = compare_nums.compare_nums(1,2)
#     assertEqual(result, None)


# #Check if input > answer
# def test_greater_than():
#     result = compare_nums.is_greater_than(4,3)
#     assertTrue(result,False)


# def test_lesser_than():
#     result = compare_nums.is_greater_than(3,4)
#     assertFalse(result, False)


# # Check decrement func
# def test_decrement():
#     result = compare_nums.decrement(5)
#     assert(4,4)


# def test_input_pass():
#     assert(int(input("Input greater than or equal to 0: ")) >= 0)


# def test_input_fail():
#     assert(int(input("Input lesser than 0: ")) < 0)


#Check phone number length
def test_phone_number_length():
    assert(len(input_phone) == 13)

#Check if phone number digits
def test_phone_number_digits():
    phone = "254799980846"
    assert(input_phone[1:]==phone)
    assert(phone.isdigit() == True)
