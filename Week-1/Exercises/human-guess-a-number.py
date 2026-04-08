"""Simple game where the computer chooses a number between 1 and 100, which the user must guess."""

from random import randint

def check_int(s):
    """ Check if string 's' represents an integer. """
    # Convert s to string
    s = str(s) 

    # If first character of the string s is - or +, ignore it when checking
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    
    # Otherwise, check the entire string
    return s.isdigit()

def input_integer(prompt):
    """ Asks user for an integer input. If valid, the string input is returned as an integer. """
    guess = input(prompt) # Ask the user for their guess
    while not check_int(guess): # Repeat until the user inputs a valid integer
        print('Please, enter a n integer number')
        guess = input(prompt)  
    return int(guess)

target = randint(1, 100) # Computer selects a random number between 1 and 100 inclusive
print("I am thinking about a number between 1 and 100. Try to find it!")
guess = input_integer("Your guess (1-100)? ")

while guess != target: # Repeat until the user guesses.
    print("Your guess is too low!") if guess < target else print("Your guess is too high!\n")
    guess = input_integer("New guess? ")

print("You win! The number was indeed " + str(target))