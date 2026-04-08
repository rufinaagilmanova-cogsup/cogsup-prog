# Helper function: Ignore
def sprint(s):
    if __name__ == "__main__":
        print(s)

################################################################################
"""
Recommended readings: 
  Chapter on functions: https://automatetheboringstuff.com/3e/chapter4.html
"""
################################################################################

"""
Exercise 5.1

Task:
------
Go back to the code you wrote for exercise 2.7 and turn it into a function called print_triangle_o.
The function should take one argument called 'rows' and print a triangle out of 'o's with n rows.
"""

sprint("Exercise 5.1")

def print_triangle_o(rows):
    """
    Print a centered triangle made of the letter 'o'.
    """

    for i in range(rows):
        print(' ' * (rows - i - 1) + 'o' * (2 * i + 1) + ' ' * (rows - i - 1))

sprint("---")

"""
Exercise 5.2

Task:
------
Go back to the code you wrote for exercise 3.2 and turn it into a function called prod_list_easy.
You can assume that all the elements of the list are numbers.
"""

sprint("Exercise 5.2")

def prod_list_easy(lst):
    """Returns the product of the elements in a number list iteratively."""
    prod = 1
    for element in lst:
        prod *= element
    return prod

sprint("---")

"""
Exercise 5.3

Task:
------
Go back to the code you wrote for exercise 3.2 and turn it into a function called prod_list_rec.
You can assume that all the elements of the list are numbers but you are not allowed to use
loops.

Hint: Can you think of a recursive way to do it?
------
"""

sprint("Exercise 5.3")

def prod_list_rec(lst):
    """Returns the product of the elements in a number list recursively."""
    if not lst:
        return 1
    
    if len(lst) == 1:
        return lst[0]
    
    return lst[0] * prod_list_rec(lst[1:])

sprint("---")

"""
Exercise 5.4

Task:
------
Take the function body you wrote in the previous exercise and modify it so that it stops
executing in case not all of the elements of the list are numbers.
------
"""

sprint("Exercise 5.4")

def prod_list_rec_full(lst):
    """
    Recursively return the product of a list of numbers.

    If the list contains non-numeric elements, a message is printed out
    and the function returns nothing.
    """
    non_numeric = [el for el in lst if not isinstance(el, (int, float))]
    if non_numeric:
        sprint(f"List contains non-numeric element(s): {non_numeric}")
        return

    if not lst:
        return 1

    if len(lst) == 1:
        return lst[0]
    
    return lst[0] * prod_list_rec(lst[1:])

sprint("---")

# --- Run the tests ---
if __name__ == "__main__":
    from testcases import (
        run_tests_ex51,
        run_tests_ex52,
        run_tests_ex53,
        run_tests_ex54,
    )

    run_tests_ex51()
    run_tests_ex52()
    run_tests_ex53()
    run_tests_ex54()