# Create a detailed Python file explaining Variables, Scope, and Data Types in Python



    # This file covers:
    # - What are variables
    # - Variable naming rules
    # - Data types (int, float, str, bool, list, tuple, dict, set, None)
    # - Variable scope (local, global, nonlocal)
    # - Dynamic typing
    # - Best practices (pro tips)


# ==========================================
# 🔹 What is a Variable?
# ==========================================
# A variable is a name that refers to a value.
# Python is dynamically typed: you don't need to declare a type.

name = "Ali"
age = 20
is_student = True

# ==========================================
# 🔹 Naming Rules
# ==========================================
# ✅ Allowed: letters, numbers, underscores (but can't start with number)
# ❌ Not Allowed: special characters, spaces
# Examples:
my_name = "Ali"
_myAge = 25
# 2nd_place = "Invalid"  # ❌ Starts with number

# ==========================================
# 🔹 Data Types
# ==========================================

# 🔸 Integer
x = 10
print(type(x))  # <class 'int'>

# 🔸 Float
pi = 3.14
print(type(pi))  # <class 'float'>

# 🔸 String
name = "Python"
print(type(name))  # <class 'str'>

# 🔸 Boolean
is_valid = True
print(type(is_valid))  # <class 'bool'>

# 🔸 List
fruits = ["apple", "banana", "cherry"]
print(type(fruits))  # <class 'list'>

# 🔸 Tuple
coordinates = (10, 20)
print(type(coordinates))  # <class 'tuple'>

# 🔸 Dictionary
student = {"name": "Ali", "age": 21}
print(type(student))  # <class 'dict'>

# 🔸 Set
unique_numbers = {1, 2, 3}
print(type(unique_numbers))  # <class 'set'>

# 🔸 None
nothing = None
print(type(nothing))  # <class 'NoneType'>

# ==========================================
# 🔹 Variable Scope
# ==========================================

# 🔸 Global Variable
x = "global"

def print_global():
    print("Inside function:", x)

print_global()
print("Outside function:", x)

# 🔸 Local Variable
def local_example():
    y = "local"
    print("Inside function:", y)

local_example()
# print(y)  # ❌ Error: y is not defined outside

# 🔸 Global keyword
a = 5

def modify_global():
    global a
    a = 10

modify_global()
print("Modified global a:", a)

# 🔸 nonlocal keyword (for nested functions)
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner"
    inner()
    print("Value after inner():", x)

outer()

# ==========================================
# 🔹 Dynamic Typing
# ==========================================
# Python allows variables to change type

var = 10
print(type(var))  # int
var = "Hello"
print(type(var))  # str

# ==========================================
# 🔹 Pro Tips & Best Practices
# ==========================================

# ✅ Use descriptive names
user_name = "Ali"
price = 100.0

# ✅ Use snake_case for variable names
total_marks = 450

# ✅ Use constants in UPPERCASE
PI = 3.14159

# ✅ Avoid using reserved keywords as variable names
# def = "function"  # ❌ Invalid

# ✅ Check variable types using type()
data = [1, 2, 3]
if type(data) == list:
    print("This is a list")

# ✅ You can use isinstance()
if isinstance(data, list):
    print("Still a list")

# ==========================================
# ✅ Summary:
# ==========================================
# - Variables store data
# - Python has many built-in types
# - Scope determines where variables can be accessed
# - Use global/nonlocal for special scope control
# - Follow naming conventions and best practices



