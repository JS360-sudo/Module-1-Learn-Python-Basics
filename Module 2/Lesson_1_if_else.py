# Lesson_1_If_Else.py

print("\n============================")
print("     Lesson 1: If / Else     ")
print("============================\n")

print("""In this lesson you will learn:
- How if/elif/else statements work
- Why they matter
- How to use them in real programs\n""")

# -----------------------------
# EXPLANATION
# -----------------------------

print("IF / ELSE BASICS\n")

print("Python checks conditions from top to bottom:")
print("""
if condition:
    # runs if true
elif another_condition:
    # runs only if above was false
else:
    # runs if nothing else matched
""")

input("\nPress Enter to continue to the exercise.\n")

# -----------------------------
# EXERCISES
# -----------------------------

print("\n============================")
print("      Exercise 2.1          ")
print("============================\n")

print("Create a line code that ask the user for their age and print whether they are an adult or a minor.\n")
input("Press Enter when you are ready to see the solution.\n")

print("""SOLUTION:
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

input("\nPress Enter for the next exercise...\n""")

# -----------------------------------------

print("\n============================")
print("      Exercise 2.2          ")
print("============================\n")

print("Write a program that checks if a number is positive, negative, or zero.\n")
input("Press Enter when you are ready to see the solution.\n")

print("""SOLUTION:
number = float(input("Enter any number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

input("\nPress Enter for the next exercise...\n""")

# -----------------------------------------

print("\n============================")
print("      Exercise 2.3          ")
print("============================\n")

print("Create a simple login check: username = admin, password = password123\n")
input("Press Enter when you are ready to see the solution.\n")

print("""SOLUTION:
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "password123":
    print("Login successful!")
else:
    print("Access denied.")""")

print("\nEnd of Lesson 1.\n")

# -----------------------------
print("Thank you for completing Lesson 1 on If/Else statements!")   
next_lesson = input("Would you like to proceed to Lesson 2 on Boolean Operators? (yes/no): ").strip().lower()
if next_lesson == "yes":
    import Lesson_2_Boolean_Operators   
else:
    print("You can return later to continue your learning. Goodbye!\n") 


