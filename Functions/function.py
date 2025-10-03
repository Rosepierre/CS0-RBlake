#Roger Blake
#Basic calculator using multiple functions to do accomplish the task

import math

num1, num2 = input("Please enter two numbers seperated by a space. ").split()
num1 = float(num1)
num2 = float(num2)

def add_func(num1, num2):
    sum_numb = num1 + num2
    return sum_numb

def multiplication_func(num1, num2):
    product = num1 * num2
    return product

def division_func(num1, num2):
    div_quo = num1/num2
    return div_quo

def subtract_func(num1, num2):
    difference = num2 - num1
    return difference

def remainder_func(num1, num2):
    remainder = num1 % num2
    return remainder

def exponent_func(num1, num2):
    power_of = num1 ** num2
    return power_of

def squareroot_func(sqrnum):
    squared = math.sqrt(sqrnum)
    return squared

def test_answer():
    """Test Cases"""
    ans = add_func(5, 7)
    expected = 12.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    ans = add_func(1, 10)
    expected = 11.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

    ans = multiplication_func(5, 7)
    expected = 35.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    ans = multiplication_func(1, 10)
    expected = 10.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

    ans = division_func(5, 7)
    expected = 0.7142857142857143
    assert ans == expected, f"Expected: {expected}, but got:{ans}"
    ans = division_func(1, 10)
    expected = 0.1
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

    ans = remainder_func(5, 7)
    expected = 5.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    ans = remainder_func(1, 10)
    expected = 1.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

    ans = subtract_func(5, 7)
    expected = 2
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    ans = subtract_func(1, 10)
    expected = 9.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

    ans = exponent_func(5, 7)
    expected = 78125.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    ans = exponent_func (1, 10)
    expected = 1.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

    ans = squareroot_func(9)
    expected = 3.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    ans = squareroot_func(5)
    expected = 2.23606797749979
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    print("Test cases have been passed...")

def main():
    add_func(num1, num2)
    print("The sum of your two numbers are", add_func(num1, num2))
    print("The product of your two numbers are", multiplication_func(num1, num2))
    print("The quotient of your two numbers are", division_func(num1, num2), "With a remainder of", remainder_func(num1, num2))
    print("The difference of your two numbers are", subtract_func(num1, num2))
    print(num1, "to the power of", num2, "is equal to", exponent_func(num1, num2))
    square_question = input("Would you like to find the square root of a number? ")
    while square_question.lower() != 'yes' and square_question.lower() != 'no':
        square_question = input("Yes or no please. ")
    if square_question.lower() == 'yes':
        sqrnum = input("Please enter the number.")
        sqrnum = float(sqrnum)
        print(squareroot_func(sqrnum))
    elif square_question.lower() == 'no':
        print("Exiting...")
test_answer()
main()