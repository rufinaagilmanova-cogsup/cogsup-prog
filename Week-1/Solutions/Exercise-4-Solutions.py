################################################################################
"""
Recommended readings: 
  Chapter on dictionaries: https://automatetheboringstuff.com/3e/chapter7.html 
  Iterating through dictionaries: https://realpython.com/iterate-through-dictionary-python/
"""
################################################################################

"""
Exercise 4.1

Task:
------
Print the sum of all values in the dictionary.
"""

dct = {'a': 3, 'b': 7, 'c': -2, 'd': 10, 'e': 5}

print("Exercise 4.1")

print(sum(dct.values()))

print("---")

"""
Exercise 4.2

Task:
------
Print the key that has the largest value in the dictionary.
"""

print("Exercise 4.2")

# Solution 1
max_value = max(dct.values())
for k, v in dct.items():
    if v == max_value:
        print(k)

# Solution 2
max_value = float("-Inf")

for k, v in dct.items():
    if v > max_value:
        max_value = v
        max_key = k

print(max_key)

print("---")

"""
Exercise 4.3

Task:
------
Create a new dictionary with the squares of all values in the dictionary.
"""

print("Exercise 4.3")

squared = {k: v**2 for k, v in dct.items()}
print(squared)

print("---")

"""
Exercise 4.4

Task:
------
Print only the keys whose values are even numbers.
"""

print("Exercise 4.4")

evens = [k for k, v in dct.items() if v % 2 == 0]
print(evens)

print("---")

"""
Exercise 4.5

Task:
------
Swap keys and values in the dictionary. 

Hint: Assume that all values are unique.
------
"""

print("Exercise 4.5")

swapped = {v: k for k, v in dct.items()}
print(swapped)

print("---")

"""
Exercise 4.6

Task:
------
Count the number of times each letter appears in the string 'ccctcctttttcc'
and print the resulting dictionary.
"""

shapes = {3: "triangle", 4: "square"}       

print("Exercise 4.6")

s = 'ccctcctttttcc'
counts = {}
for ch in s:
    counts[ch] = counts.get(ch, 0) + 1
print(counts)

print("---")

"""
Exercise 4.7

Task:
------
Given the dictionary of responses_mapping = {'j':'jazz', 'p':'pop'},
and the string responses = 'jjjpjjpppppjj',
print the list of corresponding words.
"""

responses_mapping = {'j':'jazz','p':'pop'}
responses = 'jjjpjjpppppjj'

print("Exercise 4.7")

words = [responses_mapping[ch] for ch in responses]
print(words)

print("---")

"""
Exercise 4.8

Task:
------
Merge the following two dictionaries into one:
{'a': 1, 'b': 2} and {'c': 3, 'd': 4}
"""

print("Exercise 4.8")

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

print(d1|d2)

print("---")

"""
Exercise 4.9

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose keys are sorted alphabetically.
"""

print("Exercise 4.9")

animals = {'zebra': 7, 'dolphin': 25, 'alligator': 30, 'monkey': 5, 'pig': 9}
sorted_keys = {k: animals[k] for k in sorted(animals)}
print(sorted_keys)

print("---")

"""
Exercise 4.10

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose values appear in increasing order.
"""

print("Exercise 4.10")

# Solution 1
sorted_values_1 = {k: v for k, v in sorted(animals.items(), key = lambda item: item[1])}
print(sorted_values_1)

# Solution 2
sorted_values_2 = {k: v for v, k in sorted((v, k) for k, v in animals.items())}
print(sorted_values_2)

print("---")