# --------------------------------------------
# 🟢 Sets in Python
# --------------------------------------------
# A set is an unordered, mutable collection of unique elements

s = {1, 2, 3, 2, 1}
print("Set (no duplicates):", s)

# Creating a set
empty_set = set()
s2 = set([3, 4, 5])

# Add, Remove
s.add(4)
print("After add:", s)

s.remove(2)
print("After remove 2:", s)

# discard() doesn't throw an error if element is not found
s.discard(10)

# set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a - b):", a - b)
print("Symmetric Difference:", a ^ b)

# Check membership
print("3 in a?", 3 in a)

# Other methods
print("Is disjoint:", a.isdisjoint(b))
print("Is subset:", {1, 2}.issubset(a))
print("Is superset:", a.issuperset({1}))
