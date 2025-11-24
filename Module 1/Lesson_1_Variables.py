# Lesson_1_Variables.py

print("\n=======================================")
print(" LESSON 1: VARIABLES")
print("=======================================\n")

print("A variable is a container that stores a value.")
print("Example: x = 5 means x now stores the number 5.\n")

print("Variables allow us to store information and use it later in our program.\n")

# ---------------------------
# EXERCISES
# ---------------------------

print("EXERCISE 1: Create two variables and print them.")
input("Press Enter to continue...")

x = 10
y = 20
print("Example: x =", x)
print("Example: y =", y)
print("Now YOU try it inside this file and run it!\n")

print("EXERCISE 2: Create a variable with your name and print a greeting.")
input("Press Enter to continue...")

print('Example:')
name = "CyberVet"
print("Hello,", name)
print("Now YOU create your own name variable.\n")

print("EXERCISE 3 (Harder): Ask the user for two numbers and add them.")
input("Press Enter to continue...")

print("Example:")
num1 = 5
num2 = 7
print("Total:", num1 + num2)
print("Now YOU modify the code to take real input using input().\n")

# ---------------------------
# Continue prompt
# ---------------------------

next_step = input("Would you like to go to the next lesson? (yes/no): ").lower()

if next_step == "yes":
    import Lesson_2_Data_Types
else:
    print("Great job! Come back anytime.")
