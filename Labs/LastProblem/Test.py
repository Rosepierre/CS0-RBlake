"""Module to test functions from main.py
"""

import sys
import main

# test function must start with test_ prefix for pytest to recognize it


def test_answer():
    """Test answer function
    """
    ans = main.answer("Alice")
    expected = "Thank you, Alice, and farewell!"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    ans = main.answer("Bob")
    # FIXED 5: fix the expected output
    expected = "Thank you, Bob, and farewell!"  
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    # FIXED 6: add a new test case to test your answer function
    ans = main.answer("Johnathan")
    expected = "Thank you, Johnathan, and farewell!"
    assert ans == expected, f"Expected: {expected} , but got: {ans}"
    # FIXED 7: add a new test case to test your answer function
    ans = main.answer("John Python")
    expected = "Thank you, John Python, and farewell!"
    assert ans == expected, f"Expected: {expected} , but got: {ans}"
    # FIXED 8: add a new test case to test your answer function
    ans = main.answer("Jane Python")
    expected = "Thank you, Jane Python, and farewell!"
    assert ans == expected, f"Expected: {expected} , but got: {ans}"
    # FIXED 9: add a new test case to test your answer function
    ans = main.answer("Jimothy Linux")
    expected = "Thank you, Jimothy Linux, and farewell!"
    assert ans == expected, f"Expected: {expected} , but got: {ans}"
    print("All test cases passed...", file=sys.stderr)


if __name__ == "__main__":
    test_answer()