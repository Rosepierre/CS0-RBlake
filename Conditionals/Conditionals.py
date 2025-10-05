#Roger Blake
#Calculator that takes 5 inputs and does some basic calculations
import math

def add_func(num1, num2, num3, num4, num5):
    sum_numb = num1 + num2 + num3 + num4 + num5
    return sum_numb

def multiplication_func(num1, num2, num3, num4, num5):
    product = num1 * num2 * num3 * num4 * num5
    return product

def average_func(num1, num2, num3, num4, num5):
    sum_numb = add_func(num1, num2, num3, num4, num5)
    average = sum_numb/5 
    return average

def max_func(num1, num2, num3, num4, num5):
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    if num4 > max_num:
        max_num = num4
    if num5 > max_num:
        max_num = num5
    return max_num

def min_func(num1, num2, num3, num4, num5):
    min_num = num1
    if num2 < min_num:
        min_num = num2
    if num3 < min_num:
        min_num = num3
    if num4 < min_num:
        min_num = num4
    if num5 < min_num:
        min_num = num5
    return min_num

def testcase():
    ans = add_func(4, 2, 6 , 5 , 10)
    expected = 27.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    ans = add_func(1, 3, 5, 7, 9)
    expected = 25.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

    ans = multiplication_func(4, 2, 6, 5, 10)
    expected = 2400.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    ans = multiplication_func(1, 3, 5, 7, 9)
    expected = 945.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

    sum_numb = 50.0
    ans = average_func(sum_numb)
    expected = 10.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    sum_numb = 25.0
    ans = average_func(sum_numb)
    expected = 5.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

    ans = max_func(1, 2, 3, 4, 5)
    expected = 5.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    ans = max_func(3, 6, 4, 90, 100)
    expected = 100.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

    ans = min_func(1, 2, 3, 4, 5,)
    expected = 1.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    ans = min_func(3, 6, 4, 90, 100)
    expected = 3.0
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    print("Test cases passed...")

def main():
    num1, num2, num3, num4, num5 = input("Please enter five numbers seperated by a spaces. ").split()
    num1 = float(num1)
    num2 = float(num2)
    num3 = float(num3)
    num4 = float(num4)
    num5 = float(num5)

    print(f"The sum of the numbers is: {add_func(num1, num2, num3, num4, num5)}")
    print(f"The product of the numbers is: {multiplication_func(num1, num2, num3, num4, num5)}")
    print(f"The average of the numbers is: {average_func(num1, num2, num3, num4, num5)}")
    print(f"The largest value of the numbers is: {max_func(num1, num2, num3, num4, num5)}")
    print(f"The smallest value of the numbers is: {min_func(num1, num2, num3, num4, num5)}")

if __name__ == "__main__":
    testcase()
    main()