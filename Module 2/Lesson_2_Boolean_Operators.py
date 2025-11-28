# Lesson_2_Boolean_Operators.py

print("\n============================")
print(" Lesson 2: Boolean Operators ")
print("============================\n")

print("""In this lesson you will learn:
- AND, OR, XOR, NOT
- How they work
- When to use them\n""")

# -----------------------------
# EXPLANATION
# -----------------------------

print("Boolean operators help combine conditions.\n")

print("""
AND → True only if BOTH are true
OR  → True if ANY is true
XOR → True if ONLY ONE is true (A != B)
NOT → Reverses the value (not True → False)
""")

input("\nPress Enter to start exercises...\n")

# -----------------------------
# EXERCISES
# -----------------------------

print("\n============================")
print("      Exercise 2.4          ")
print("============================\n")

print("Write a program that checks if two numbers are both positive using AND operator.\n")
input("Press Enter when you are ready to see the solution.\n")

print("""SOLUTION:
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > 0 and b > 0:
    print("Both are positive.")
else:
    print("Condition not met.")""")

input("\nPress Enter for next exercise...\n")

# -----------------------------------------

print("\n============================")
print("      Exercise 2.5          ")
print("============================\n")

print("Create a program that asks the user if they want coffee or tea using XOR operator.\n")
input("Press Enter when you are ready to see the solution.\n")

print("""SOLUTION:
coffee = input("Do you want coffee? (yes/no): ").lower()
tea = input("Do you want tea? (yes/no): ").lower()

coffee_choice = (coffee == "yes")
tea_choice = (tea == "yes")

if coffee_choice != tea_choice:  # XOR
    print("Here you go!")
else:
    print("Invalid choice.")""")

input("\nPress Enter for next exercise...\n")

# -----------------------------------------

print("\n============================")
print("      Exercise 2.6          ")
print("============================\n")

print("Build a password validator that requires at least 8 characters, includes '@' or '#', and has no spaces using AND, OR, NOT operators.\n")
input("Press Enter when you are ready to see the solution.\n")  

print("""SOLUTION:
password = input("Enter a password: ")

if len(password) >= 8 and ("@" in password or "#" in password) and (" " not in password):
    print("Password is valid.")
else:
    print("Password invalid. Requirements not met.")""")

print("\nEnd of Lesson 2.\n")

# -----------------------------
print("Thank you for completing Lesson 2 on Boolean Operators!")
next_lesson = input("Would you like to proceed to Lesson 3 on Control Structures & Functions? (yes/no): ").strip().lower()
if next_lesson == "yes":
    import Lesson_3_Control_Structures  
else:
    print("You can return later to continue your learning. Goodbye!\n")

