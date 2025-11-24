# Intro.py

print("\n============================")
print(" Welcome to CyberVets Python ")
print("============================\n")

print("In Module 1, you will learn:")
print("- What Python is and how code works")
print("- Variables")
print("- Data Types")
print("- Basic Input/Output")
print("- Writing simple programs\n")

print("This module is self-paced. Pick where you want to begin.\n")

print("Choose a lesson:")
print("1 - Variables")
print("2 - Data Types")
print("3 - Basic Operations")
print("4 - Mini Projects\n")

choice = input("Enter the number of the lesson you want to start with: ")

if choice == "1":
    import Lesson_1_Variables
elif choice == "2":
    import Lesson_2_Data_Types
elif choice == "3":
    import Lesson_3_Basic_Operations
elif choice == "4":
    import Simple_Programs
else:
    print("Invalid choice. Please run Intro.py again.")
