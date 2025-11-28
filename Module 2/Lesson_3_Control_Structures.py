# Lesson_3_Control_Structures.py

print("\n============================")
print(" Lesson 3: Control Structures ")
print("============================\n")

print("""In this lesson you will learn:
- Functions
- While loops
- For loops
- Break and continue\n""")

# -----------------------------
# FUNCTIONS
# -----------------------------

print("\nFUNCTIONS\n")
print("""
Functions help organize and reuse code:

def greet(name):
    print("Hello", name)
""")
input("\nPress Enter for exercises.\n")

# -----------------------------
# EXERCISES
# -----------------------------

print("\n============================")
print("      Exercise 2.7          ")
print("============================\n")

print("Create a function that greets the user by their name.\n")
input("Press Enter when you are ready to see the solution.\n")

print("""SOLUTION:
def greet_user(name):
    print("Hello,", name + "!")

name_input = input("Enter your name: ")
greet_user(name_input)""")

input("\nPress Enter for next exercise...\n")

# -----------------------------------------

print("\n============================")
print("      Exercise 2.8          ")
print("============================\n")

print("Write a function that takes a number n and returns the sum of all numbers from 1 to n using a for loop.\n")
input("Press Enter when you are ready to see the solution.\n")

print("""SOLUTION:
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter a number: "))
print("Sum from 1 to", n, "is:", sum_to_n(n))""")

input("\nPress Enter for next exercise...\n")

# -----------------------------------------

print("\n============================")
print("      Exercise 2.9          ")
print("============================\n")

print("Build a simple guessing game where the user has to guess a number between 1 and 20 using a while loop.\n")
input("Press Enter when you are ready to see the solution.\n")

print("""SOLUTION:
import random

def guessing_game():
    number = random.randint(1, 20)
    guess = 0

    print("I am thinking of a number between 1 and 20.")

    while guess != number:
        guess = int(input("Take a guess: "))

        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print("Correct! Well done.")

guessing_game()""")

print("\nEnd of Lesson 3.\n")
# -----------------------------

print("Thank you for completing Lesson 3 on Control Structures & Functions!")
next_lesson = input("Would you like to proceed to Lesson 4 on Practice Exercises? (yes/no): ").strip().lower()
if next_lesson == "yes":
    import Lesson_4_Simple_Programs 
else:
    print("You can return later to continue your learning. Goodbye!\n")

