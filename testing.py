import calculator

calculator = calculator.Calculator()

def test_multiply_two_numbers():
    assert calculator.calculate('2*4')==8

def test_add_two_numbers():
    assert calculator.calculate('5+2')==7

def test_subtract_two_numbers():
    assert calculator.calculate('12-10')==2

def test_divide_two_numbers():
    assert calculator.calculate('27/3')==9

def test_bad_input():
    assert calculator.calculate('foo')=="Invalid input"

def test_string_tokenizer():
    assert calculator.string_tokenizer('3+4*5')==[3, '+', 4, '*', 5]
    assert calculator.string_tokenizer('4+27*243')==[4, '+', 27, '*', 243]
    assert calculator.string_tokenizer('27')==[27]
    assert calculator.string_tokenizer('')==[]
    assert calculator.string_tokenizer('2+3')==[2, '+', 3]

def test_no_operator():
    assert calculator.calculate('35')==35

def test_add_three_numbers():
    assert calculator.calculate('3+4+5')==12

def test_pemdas():
    assert calculator.calculate('5+2*4')==13

if __name__ == '__main__':
    # test_multiply_two_numbers()
    # test_add_two_numbers()
    # test_subtract_two_numbers()
    # test_divide_two_numbers()
    # test_bad_input()
    test_string_tokenizer()
