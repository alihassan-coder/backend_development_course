# --------------------------------------------
# 📦 LIST BASICS
# --------------------------------------------

# A list is an ordered, mutable collection
fruits = ["apple", "banana", "cherry"]

print("Original List:", fruits)

# --------------------------------------------
# 🔁 INDEXING & SLICING
# --------------------------------------------

print("\nIndexing & Slicing:")
print("First item:", fruits[0])
print("Last item:", fruits[-1])
print("Slice (0:2):", fruits[0:2])
print("Every 2nd item:", fruits[::2])

# --------------------------------------------
# ➕ ADDING ITEMS
# --------------------------------------------

print("\nAdding Items:")
fruits.append("orange")            # Adds to end
print("After append:", fruits)

fruits.insert(1, "grape")          # Insert at index 1
print("After insert:", fruits)

fruits.extend(["mango", "kiwi"])   # Add multiple items
print("After extend:", fruits)

# --------------------------------------------
# ❌ REMOVING ITEMS
# --------------------------------------------

print("\nRemoving Items:")
fruits.remove("banana")           # Remove by value
print("After remove 'banana':", fruits)

popped_item = fruits.pop()        # Removes last item
print("After pop:", fruits, "| Popped:", popped_item)

del fruits[0]                     # Delete by index
print("After del index 0:", fruits)

fruits.clear()                    # Empty the list
print("After clear:", fruits)

# Refill for further examples
fruits = ["apple", "banana", "cherry", "apple", "banana"]

# --------------------------------------------
# 🔍 FINDING ITEMS
# --------------------------------------------

print("\nFinding Items:")
print("Index of 'cherry':", fruits.index("cherry"))
print("Count of 'banana':", fruits.count("banana"))
print("'apple' in fruits?", "apple" in fruits)

# --------------------------------------------
# 🧼 SORTING & REVERSING
# --------------------------------------------

nums = [5, 2, 9, 1, 5]

print("\nSorting & Reversing:")
nums.sort()                       # Sort ascending
print("Sorted list:", nums)

nums.sort(reverse=True)          # Sort descending
print("Sorted (desc):", nums)

nums.reverse()                   # Reverse current order
print("Reversed list:", nums)

# --------------------------------------------
# 🧭 COPYING LISTS
# --------------------------------------------

print("\nCopying Lists:")
copy1 = nums.copy()
copy2 = list(nums)
copy3 = nums[:]
print("Copy 1:", copy1)
print("Copy 2:", copy2)
print("Copy 3:", copy3)

# --------------------------------------------
# 🔀 LIST COMPREHENSION
# --------------------------------------------

print("\nList Comprehension:")
squares = [x**2 for x in range(5)]
print("Squares:", squares)

even = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", even)

# --------------------------------------------
# 🔧 OTHER USEFUL METHODS
# --------------------------------------------

print("\nOther Useful Methods:")
example = [3, 1, 4, 1, 5, 9]

print("Length:", len(example))
print("Max:", max(example))
print("Min:", min(example))
print("Sum:", sum(example))

example *= 2
print("Repeated list (*2):", example)

# --------------------------------------------
# 🧬 NESTED LISTS
# --------------------------------------------

print("\nNested Lists:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Element at row 2, col 3:", matrix[1][2])  # 6

# --------------------------------------------
# 🧪 enumerate(), zip(), map(), filter() with lists
# --------------------------------------------

print("\nAdvanced:")
names = ["Ali", "Ahmed", "Sara"]
scores = [85, 90, 95]

for index, name in enumerate(names):
    print(f"{index}: {name}")

zipped = list(zip(names, scores))
print("Zipped (name, score):", zipped)

doubled = list(map(lambda x: x * 2, scores))
print("Scores Doubled:", doubled)

filtered = list(filter(lambda x: x > 85, scores))
print("Scores > 85:", filtered)

# --------------------------------------------
# ✅ List unpacking
# --------------------------------------------

print("\nUnpacking:")
items = [1, 2, 3, 4, 5]
a, b, *rest = items
print("a:", a, "b:", b, "rest:", rest)

