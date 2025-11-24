# Lesson_3_Basic_Operations.py

print("\n=======================================")
print(" LESSON 3: BASIC OPERATIONS, INPUT, COMMENTS")
print("=======================================\n")

print("""In this lesson, you will learn:
- How to use input()
- Basic math operations (+, -, *, /)
- Writing comments (#)
- Keeping code clean and readable\n""")

# Explanation
print("Comments are lines of text that Python ignores. They help explain your code.")
print("Example: # This is a comment\n")

# ---------------------------
# EXERCISES
# ---------------------------

print("EXERCISE 1: Write a program that asks for your name and prints a greeting.")
input("Press Enter to see an example")

print(""" # Using + operator
greeting = "Hello" + " " + ""nice day today!"

# Using f-strings (preferred)
name = "CyberVet"
message = f"Hello {name}, have a nice day today!\n""")

print("EXERCISE 2: Create a simple calculator.")
input("Press Enter to see an example\n")

print("""Example:
a = 5
b = 3
sum_val = a + b      # Addition: (5 + 3) = 8
diff = a - b         # Subtraction: (5 - 3) = 2
product = a * b      # Multiplication: (5 * 3) = 15
quotient = a / b     # Division: (5 / 3) = 1.666...
remainder = a % b    # Modulus: (5 % 3) = 2
Now YOU write your own calculator using input().\n""")

print("EXERCISE 3: On a new file, write a line a code asking the user for two numbers and show ALL operations (add, subtract, multiply, divide).")
input("Press Enter to continue...\n")

# ---------------------------
# Continue prompt
# ---------------------------

next_step = input("Would you like to continue to the Mini Projects? (yes/no): ").lower()

if next_step == "yes":
    import Simple_Programs
else:
    print("Excellent! You're almost done with Module 1.")
    print("Take a break and return when you're ready for the Mini Projects.")
    print("You've completed Lesson 3 on Basic Operations.")
    