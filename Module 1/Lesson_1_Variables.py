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
input("Press Enter to see an example\n")

print("""Example:
x = 10
y = 20
print("Example: x =", x)
print("Example: y =", y)
Now create your own code and try not to get any errors!\n""")
print("press Enter to continue to the next excersize\n")

print("EXERCISE 2: Create a variable with your name and print a greeting.")
input("Press Enter to see an example\n")

print("""Example:
name = "CyberVet"
print("Hello,", name)
Now YOU create your own name variable.\n""")
print("Press Enter to continue to the next excersize\n")

print("""EXERCISE 3: Lets create a variable with two numbers.
Once you do that, run a print command adding the two numbers together.""")
input("Press Enter to see an example")

print("""Example:
num1 = 5
num2 = 7
print("Total:", num1 + num2)
Now modify the code to take real input using input().\n""")
print("Hint: Use int(input()) to convert input to a number.\n")

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

