################################################################################
"""
Recommended readings: 
  Chapter on lists: https://automatetheboringstuff.com/3e/chapter6.html 
  List comprehension: https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
"""
################################################################################

"""
Exercise 3.1

Task:
------
Write code that prints the sum of the elements in the following list.
[1, 4, -6, 7, 2, 3, 9, 11, 6]
"""

lst = [1, 4, -6, 7, 2, 3, 9, 11, 6] # In all exercises in this script, you will work with this list

print("Exercise 3.1")

# Solution 1
cum_sum = 0
for element in lst:
    cum_sum += element

print(f"Sum of {lst} = {cum_sum}")

# Solution 2
print(f"Sum of {lst} = {sum(lst)}")

print("---")

"""
Exercise 3.2

Task:
------
Print the product of the elements in the list.
"""

print("Exercise 3.2")


# Solution 1
cum_prod = 1
for element in lst:
    cum_prod *= element

print(f"Product of {lst} = {cum_prod}")

# Solution 2
import numpy as np
print(f"Product of {lst} = {np.prod(lst)}")

print("---")

"""
Exercise 3.3

Task:
------
Print the sum of the squares of the list.
"""

print("Exercise 3.3")

lst = [1, 4, -6, 7, 2, 3, 9, 11, 6]

# Solution 1
sum_squares = 0
for element in lst:
    sum_squares += element**2

print(f"Sum of squares of {lst} = {sum_squares}")

# Solution 2
sum_squares = sum([i**2 for i in lst])
print(f"Sum of squares of {lst} = {sum_squares}")

print("---")

"""
Exercise 3.4

Task:
------
Print the largest element of the list.
"""

print("Exercise 3.4")

# Solution 1
largest_so_far = float("-Inf")

for element in lst:
    if element > largest_so_far:
        largest_so_far = element

print(f"Largest element of {lst} is {largest_so_far}")

# Solution 2
print(f"Largest element of {lst} is {max(lst)}")

print("---")

"""
Exercise 3.5

Task:
------
Print the largest element of the list.
"""

print("Exercise 3.5")

# Solution 1
print(f"Second largest element of {lst} is {sorted(lst, reverse = True)[1]}")

# Solution 2
lst.sort()
print(f"Second largest element of {lst} is {lst[-2]}")

print("---")