# ===============================
# 🔹 MODULES IN PYTHON
# ===============================

# A module is any Python file (with .py extension)
# You can import built-in or user-defined modules

# ---- 1. Importing built-in module ----
import math

# Using a function from the math module
print("Square root of 16 is:", math.sqrt(16))  # Output: 4.0

# ---- 2. Importing specific function ----
from math import pow

print("2^3 is:", pow(2, 3))  # Output: 8.0

# ---- 3. Importing with alias ----
import math as m

print("Cosine of 0:", m.cos(0))  # Output: 1.0

# ---- 4. User-defined module ----
# Assuming we have another file named `calculator.py` in same directory

# calculator.py content:
# def add(a, b):
#     return a + b
# def subtract(a, b):
#     return a - b

# Importing our own module
import calculator

print("Add 5 + 3:", calculator.add(5, 3))        # Output: 8
print("Subtract 5 - 3:", calculator.subtract(5, 3))  # Output: 2

# ===============================
# 🔹 PACKAGES IN PYTHON
# ===============================

# A package is a folder that contains an __init__.py file and modules

# Directory Structure:
# my_package/
# ├── __init__.py
# └── operations.py

# my_package/operations.py content:
# def multiply(a, b):
#     return a * b
# def divide(a, b):
#     return a / b

# Importing from a package
from my_package import operations

print("Multiply 4 * 5:", operations.multiply(4, 5))  # Output: 20
print("Divide 20 / 4:", operations.divide(20, 4))    # Output: 5.0

# ===============================
# 🔚 END OF EXAMPLE
# ===============================
