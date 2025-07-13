# --------------------------------------------
# 🔗 Tuples in Python
# --------------------------------------------
# A tuple is an ordered, immutable collection

t = (1, 2, 3)
print("Tuple:", t)
print("First item:", t[0])
print("Length:", len(t))

# Tuple can hold mixed types
t2 = (1, "hello", 3.14)

# Nested tuples
nested = (1, (2, 3), 4)

# Tuple unpacking
a, b, c = t
print("Unpacked:", a, b, c)

# Tuple with one element needs a comma
single = (5,)
print("Single element tuple:", single)

# Tuples are immutable
# t[0] = 10  ❌ (this will throw an error)

# Use case: faster and safe data storage
