# exception_handling_demo.py

"""
📘 EXCEPTION HANDLING IN PYTHON
This file explains:
1. Handling exceptions using try-except
2. Raising exceptions using raise
3. Using finally block
4. Creating custom exceptions
"""

# 1️⃣ Handling Exceptions with try-except
def divide_numbers():
    print("\n🔹 Example 1: try-except for dividing numbers")
    try:
        number = int(input("Enter a number to divide 10: "))
        result = 10 / number
        print("✅ Result is:", result)
    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero!")
    except ValueError:
        print("❌ Error: Please enter a valid number (not a letter).")

# 2️⃣ Using finally block
def file_handling_example():
    print("\n🔹 Example 2: finally block demonstration")
    try:
        f = open("sample.txt", "r")
        content = f.read()
        print("✅ File content:", content)
    except FileNotFoundError:
        print("❌ Error: File not found.")
    finally:
        print("🔁 Finally block runs no matter what (e.g., to close file).")

# 3️⃣ Raising Exceptions manually
def check_age():
    print("\n🔹 Example 3: raise statement to trigger custom error")
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("❌ Age cannot be negative!")
        print("✅ Age is valid:", age)
    except ValueError as ve:
        print("❌ Exception raised:", ve)

# 4️⃣ Creating and Using a Custom Exception
class CustomError(Exception):
    """Custom exception for demonstration."""
    pass

def check_unlucky_number(num):
    print("\n🔹 Example 4: Custom exception for unlucky number")
    try:
        if num == 13:
            raise CustomError("😨 13 is considered an unlucky number!")
        print("✅ Number is safe:", num)
    except CustomError as ce:
        print("❌ CustomError raised:", ce)

# 🔄 Run all examples
if __name__ == "__main__":
    divide_numbers()
    file_handling_example()
    check_age()
    check_unlucky_number(13)
