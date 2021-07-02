import compare_nums

input_phone = "+254799980846"

#Check if answer == input; return True
def test_equal():
    result = compare_nums.compare_nums(2,2)
    assert(result == True)


# Check if input != answer
def test_not_equal():
    result = compare_nums.compare_nums(1,2)
    assert(result == False)


#Check if input > answer
def test_greater_than():
    result = compare_nums.is_greater_than(4,3)
    assert(result == True)


def test_lesser_than():
    result = compare_nums.is_greater_than(3,4)
    assert(result == False)


# Check decrement func
def test_decrement():
    result = compare_nums.decrement(5)
    assert(result == 4)

#Check phone number length
def test_phone_number_length():
    assert(len(compare_nums.get_phone_number(input_phone)) == 13)

#Check if phone number digits
def test_phone_number_digits():
    phone = "254799980846"
    no = compare_nums.get_phone_number(input_phone)
    no = no[1:]
    assert(no==phone)

def test_phone_is_digit():
    no = compare_nums.get_phone_number(input_phone)
    no = no.isdigit()
    assert(no == True)


def test_phone_country_code():
    assert(input_phone[:4] == "+254")



