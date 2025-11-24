# Lesson_2_Data_Types.py

print("\n=======================================")
print(" LESSON 2: DATA TYPES")
print("=======================================\n")

print("""Python has several basic data types:
Here are some of the most common ones:
Integers: whole numbers like 5, 20, -3
Floats: decimal numbers like 3.14, 2.5
Strings: text inside quotes 'hello'
Booleans: True or False values\n""")

print("Data types are important so Python knows how to treat information.\n")

# ---------------------------
# EXERCISES
# ---------------------------

print("EXERCISE 1: Identify the data type of a value.")
input("Press Enter to see an example\n")

print("""Example:
x = 10
print(type(x))  # This shows the data type
Now YOU try printing type() on other values.\n""")

print("EXERCISE 2: Convert between data types.")
input("Press Enter to see an example\n")

print("""Example:
num = "5"
num = int(num)   # Convert string to integer
print("Converted:", num)
Now YOU try converting between str, int, and float.\n""")

print("EXERCISE 3: Write a code asking the user for their age and return True/False if they are 18+.")
input("Press Enter to continue...\n")

print("Hint: Use int(input()) and a boolean comparison.\n")

# ---------------------------
# Continue prompt
# ---------------------------

next_step = input("Would you like to go to the next lesson? (yes/no): ").lower()

if next_step == "yes":
    import Lesson_3_Basic_Operations
else:
    print("Great job! Stop here for now, and return when ready.")
