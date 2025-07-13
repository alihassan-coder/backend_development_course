# --------------------------------------------
# 🔢 Arithmetic Operators
# --------------------------------------------
# Used to perform mathematical operations

a = 10
b = 3

print("Arithmetic Operators:")
print("a + b =", a + b)     # Addition
print("a - b =", a - b)     # Subtraction
print("a * b =", a * b)     # Multiplication
print("a / b =", a / b)     # Division (float)
print("a // b =", a // b)   # Floor Division
print("a % b =", a % b)     # Modulus (remainder)
print("a ** b =", a ** b)   # Exponentiation
print("arithmetic operators are used to perform mathematical operations")

# --------------------------------------------
# 🧠 Bitwise Operators
# --------------------------------------------
# Operate on bits (binary representation)

x = 5       # Binary: 0101
y = 3       # Binary: 0011

print("Bitwise Operators:")
print("x & y =", x & y)     # AND
print("x | y =", x | y)     # OR
print("x ^ y =", x ^ y)     # XOR
print("x << 1 =", x << 1)   # Left Shift (adds a 0 bit)
print("x >> 1 =", x >> 1)   # Right Shift (removes last bit)
print("~x =", ~x)           # NOT (inverts all bits)
print()

# --------------------------------------------
# 🧮 Assignment Operators
# --------------------------------------------
# Used to assign values to variables

c = 5
print("Assignment Operators:")
c += 2      # c = c + 2
print("c += 2:", c)
c -= 1      # c = c - 1
print("c -= 1:", c)
c *= 3      # c = c * 3
print("c *= 3:", c)
c /= 2      # c = c / 2
print("c /= 2:", c)
c //= 2     # c = c // 2
print("c //= 2:", c)
c %= 2      # c = c % 2
print("c %= 2:", c)
c **= 3     # c = c ** 3
print("c **= 3:", c)
print()

# --------------------------------------------
# 🔍 Comparison Operators
# --------------------------------------------
# Compare values and return Boolean result

print("Comparison Operators:")
print("a == b:", a == b)   # Equal
print("a != b:", a != b)   # Not equal
print("a > b:", a > b)     # Greater than
print("a < b:", a < b)     # Less than
print("a >= b:", a >= b)   # Greater than or equal
print("a <= b:", a <= b)   # Less than or equal
print()

# --------------------------------------------
# 🧠 Logical Operators
# --------------------------------------------
# Used with Boolean expressions

p = True
q = False

print("Logical Operators:")
print("p and q:", p and q)   # True if both True
print("p or q:", p or q)     # True if at least one True
print("not p:", not p)       # Inverts the result
print()

# --------------------------------------------
# 🆔 Identity Operators
# --------------------------------------------
# Check if two variables refer to the same object in memory

x = [1, 2]
y = x
z = [1, 2]

print("Identity Operators:")
print("x is y:", x is y)         # True, same object
print("x is z:", x is z)         # False, same value but different objects
print("x is not z:", x is not z) # True
print()

# --------------------------------------------
# 📦 Membership Operators
# --------------------------------------------
# Check if a value is present in a sequence

nums = [1, 2, 3, 4]

print("Membership Operators:")
print("2 in nums:", 2 in nums)         # True
print("5 not in nums:", 5 not in nums) # True
print()
