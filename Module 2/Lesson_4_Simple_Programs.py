# Lesson_4_Simple_Programs.py

print("\n============================")
print(" Lesson 4: Practice Exercises ")
print("============================\n")

print("This lesson combines everything from Module 2.\n")
input("Press Enter to start the challenges...\n")

# --------------- Challenge 1 ---------------

print("\n============================")
print("   Challenge 1: Grade Checker ")
print("============================\n")

print("Write a program that takes a test score (0-100) and prints the corresponding letter grade:\n")
input("Press Enter when you are ready to see the solution.\n")

print("""SOLUTION:
score = float(input("Enter a test score (0-100): "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")""")

input("\nPress Enter for next challenge...\n")

# --------------- Challenge 2 ---------------

print("\n============================")
print("  Challenge 2: Login System  ")
print("============================\n")

print("Create a simple login system that asks for a username and password. Grant access only if both are correct.\n")
input("Press Enter when you are ready to see the solution.\n")  

print("""SOLUTION:
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "cybervets":
    print("Access granted.")
else:
    print("Access denied.")""")

input("\nPress Enter for next challenge...\n")

# --------------- Challenge 3 ---------------

print("\n============================")
print(" Challenge 3: Number Analyzer ")
print("============================\n")

print("Write a program that takes a number and tells if it's even or odd, and whether it's positive, negative, or zero.\n")
input("Press Enter when you are ready to see the solution.\n")

print("""SOLUTION:
num = float(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")""")

input("\nPress Enter for next challenge...\n")

# -------------- Challenge 4 ---------------

print("\n============================")
print(" Challenge 4: Simple Calculator ")   
print("============================\n")

print("Build a simple calculator that can add, subtract, multiply, or divide two numbers based on user input.\n")
input("Press Enter when you are ready to see the solution.\n")  

print("""SOLUTION:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))        
operation = input("Choose operation (+, -, *, /): ")    
if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero.")
else:
    print("Invalid operation.")""")

input("\nPress Enter for next challenge...\n")

# ------------- Challenge 5 ---------------

print("\n============================")
print("  Challenge 5: Age Group Finder  ")      
print("============================\n")

print("Create a program that categorizes a person into an age group (child, teenager, adult, senior) based on their age.\n")
input("Press Enter when you are ready to see the solution.\n")

print("""SOLUTION:
age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")""")

print("\nEnd of Lesson 4. Great work!\n")

# -----------------------------
