# --------------------------------------------
# 🔄 Type Casting in Python
# --------------------------------------------

# Convert between types

# int, float, str
a = "10"
b = int(a)
c = float(b)

print("String to int:", b)
print("Int to float:", c)
print("Float to str:", str(c))

# bool
print("bool(0):", bool(0))
print("bool('hello'):", bool("hello"))

# list, tuple, set
s = "abc"
print("String to list:", list(s))
print("String to tuple:", tuple(s))
print("List to set:", set([1, 2, 2, 3]))

# dict from list of tuples
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)
print("List of tuples to dict:", d)

# Using map for batch casting
nums = ["1", "2", "3"]
int_nums = list(map(int, nums))
print("String list to int list:", int_nums)
