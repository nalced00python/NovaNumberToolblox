import random

print("Welcome to Nova Number Guessing Version 3.0")
githubinfo = "Go to my Github Repo called 'Nova-Number-Toolbox' to view future events and updates"
print(githubinfo)

rules = "To guess, type in a number between the given values. The game will tell you if you have gotten it correct, wrong, or if your entered value is invalid."
print(rules)

print("Good Luck!")
input("Press enter to begin playing")

# -------- ROUND 1 --------
low = 1
high = 40
tries = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Round 1 (Easy): Guess a number between {low}-{high}: "))
    tries += 1

    if guess < number:
        print(f"{guess} is too low. Try again!")
    elif guess > number:
        print(f"{guess} is too high. Try again!")
    else:
        print(f"{guess} is correct! Good job!")
        print(f"This round took you {tries} tries!")
        break

# -------- ROUND 2 --------
input("Press Enter for Round 2...")

low = 1
high = 70
tries = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Round 2 (Medium): Guess a number between {low}-{high}: "))
    tries += 1

    if guess < number:
        print(f"{guess} is too low. Try again!")
    elif guess > number:
        print(f"{guess} is too high. Try again!")
    else:
        print(f"{guess} is correct! Good job!")
        print(f"This round took you {tries} tries!")
        break

# -------- ROUND 3 --------
input("Press Enter for Round 3...")

low = 1
high = 100
tries = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Round 3 (Hard): Guess a number between {low}-{high}: "))
    tries += 1

    if guess < number:
        print(f"{guess} is too low. Try again!")
    elif guess > number:
        print(f"{guess} is too high. Try again!")
    else:
        print(f"{guess} is correct! Good job!")
        print(f"This round took you {tries} tries!")
        break

print("Thank you for playing! Check my Github Toolbox for more!")
