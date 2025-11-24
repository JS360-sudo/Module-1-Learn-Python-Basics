# Lesson_1_Variables.py

print("\n=======================================")
print(" LESSON 1: VARIABLES")
print("=======================================\n")

print("""A variable is a container that stores a value.
Example: x = 5 means x now stores the number 5.\n""")
print("""Here are a few more examples of how a variable can be used. 
name = "Alice"
age = 20
temperature = 98.6""")

print("Variables allow us to store information and use it later in our program.\n")

# ---------------------------
# EXERCISES
# ---------------------------

print("EXERCISE 1: Create a new file and create two variables of your own.")
input("Press Enter to continue...")

x = 10
y = 20
print("Example: x =", x)
print("Example: y =", y)
print("Now run it and hopefully you dont have any errors!\n")

print("EXERCISE 2: Create a variable with your name and print a greeting.")
input("Press Enter to see an example")

print('Example:')
name = "CyberVet"
print("Hello,", name)
print("Now YOU create your own name variable.\n")

print("""EXERCISE 3: Lets create a variable with two numbers.
Once you do that, run a print command adding the two numbers together.""")
input("Press Enter to see an example")

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
    print("You've completed Lesson 1 on Variables.")
    print("Take a break and return when you're ready for Lesson 2.")

