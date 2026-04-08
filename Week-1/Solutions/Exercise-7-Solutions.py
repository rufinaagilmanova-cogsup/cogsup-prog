"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""

print("I am going to guess your number quickly.")
guessed = False

minimum = 1
maximum = 101 # must be 101, otherwise guess will never equal 100

# Binary search
while not guessed:
    guess = (minimum + maximum) // 2

    feedback = input(f"My current guess is {guess}. Is it correct, high, or low? ").strip().lower()

    while feedback not in ["correct", "high", "low"]:
        print("Please answer one of 'correct', 'high', or 'low', so we can understand each other.")
        feedback = input(f"My current guess is {guess}. Is it correct, high, or low?" ).strip().lower()

    if feedback == "correct":
        guessed = True
    
    elif feedback == "high":
        maximum = guess
    
    elif feedback == "low":
        minimum = guess

print("I won!")