# Module2_Intro.py

print("\n============================")
print("   Welcome to Module 2!     ")
print("   CyberVets Python Course  ")
print("============================\n")

print("In Module 2, you will learn:")
print("- If, Elif, Else statements")
print("- Boolean operators: AND, OR, XOR, NOT")
print("- Control structures and functions")
print("- How to make your programs think and react\n")

print("This module is self-paced. Choose any lesson to begin.\n")

print("Choose a lesson:")
print("1 - If/Else Statements")
print("2 - Boolean Operators (AND, OR, XOR, NOT)")
print("3 - Control Structures & Functions")
print("4 - Practice Exercises (All Topics)\n")

choice = input("Enter the number of the lesson you want to start with: ")

if choice == "1":
    import Lesson_1_if_else
elif choice == "2":
    import Lesson_2_Boolean_Operators
elif choice == "3":
    import Lesson_3_Control_Structures
elif choice == "4":
    import Lesson_4_Simple_Programs
else:
    print("Invalid choice. Please run Module2_Intro.py again.")
print("\nThank you for choosing Module 2! Happy coding!\n")
