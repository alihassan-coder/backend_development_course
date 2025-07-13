# --------------------------------------------
# 📌 STRING BASICS
# --------------------------------------------

# Strings are sequences of characters enclosed in '' or ""
s = "Hello, World!"

# Multiline string using triple quotes
multiline = """This is
a multiline
string."""

print("Original String:", s)

# --------------------------------------------
# 🔤 STRING INDEXING & SLICING
# --------------------------------------------

print("First character:", s[0])
print("Last character:", s[-1])
print("Substring (0:5):", s[0:5])  # 'Hello'
print("Every second character:", s[::2])

# --------------------------------------------
# 🧪 COMMON STRING METHODS
# --------------------------------------------

print("\nCommon String Methods:")
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Title case:", s.title())
print("Capitalize:", s.capitalize())
print("Swapcase:", s.swapcase())
print("Is Alphabetic:", "abc".isalpha())
print("Is Digit:", "123".isdigit())
print("Is Alphanumeric:", "abc123".isalnum())
print("Is Lowercase:", "hello".islower())
print("Is Uppercase:", "HELLO".isupper())
print("Is Space:", "   ".isspace())
print("Starts with 'Hello':", s.startswith("Hello"))
print("Ends with '!':", s.endswith("!"))

# --------------------------------------------
# 🔄 STRIPPING & REPLACING
# --------------------------------------------

text = "   Hello Python!   "
print("\nStripping & Replacing:")
print("Original:", repr(text))
print("Stripped:", text.strip())      # Removes whitespace
print("Left strip:", text.lstrip())
print("Right strip:", text.rstrip())
print("Replace 'Python' with 'World':", text.replace("Python", "World"))

# --------------------------------------------
# 🔍 FINDING & COUNTING
# --------------------------------------------

print("\nFinding & Counting:")
print("Find index of 'World':", s.find("World"))
print("Index of 'o':", s.index("o"))          # Like find, but throws error if not found
print("Count of 'l':", s.count("l"))

# --------------------------------------------
# 🧵 JOINING & SPLITTING
# --------------------------------------------

words = ["one", "two", "three"]
sentence = "Join these words"
print("\nJoining & Splitting:")
print("Split sentence into list:", sentence.split())
print("Join list into string:", " - ".join(words))

# --------------------------------------------
# ✂️ STRING JUSTIFICATION & PADDING
# --------------------------------------------

print("\nString Justify:")
print("Left Justify:", "text".ljust(10, "-"))
print("Right Justify:", "text".rjust(10, "-"))
print("Center:", "text".center(10, "*"))

# --------------------------------------------
# 🧠 STRING FORMATTING
# --------------------------------------------

name = "Ali"
age = 22

print("\nString Formatting:")
print("Old style: Hello %s, age %d" % (name, age))
print("str.format(): Hello {}, age {}".format(name, age))
print(f"f-string: Hello {name}, age {age}")

# --------------------------------------------
# 🔐 ENCODING & DECODING
# --------------------------------------------

encoded = s.encode("utf-8")
print("\nEncoding & Decoding:")
print("Encoded:", encoded)
print("Decoded:", encoded.decode("utf-8"))

# --------------------------------------------
# 🔍 ADVANCED (PYTHON 3.9+)
# --------------------------------------------

# Removeprefix and Removesuffix (3.9+)
filename = "image.png"
print("\nPython 3.9+ Features:")
print("Remove prefix:", filename.removeprefix("image"))
print("Remove suffix:", filename.removesuffix(".png"))

# Casefold (better than lower for international strings)
print("Casefold (vs lower):", "Straße".casefold())  # 'strasse'

# --------------------------------------------
# ✅ ISIDENTIFIER, ISDECIMAL, etc.
# --------------------------------------------

print("\nOther Checks:")
print("'variable1'.isidentifier():", "variable1".isidentifier())
print("'12345'.isdecimal():", "12345".isdecimal())

# --------------------------------------------
# 🧪 New Features in Python 3.12+
# --------------------------------------------

print("\nPython 3.12+ additions (example):")
# Not many changes to strings, but f-strings support better debug info
price = 20
print(f"{price=}")  # Python 3.8+: prints 'price=20'

# Unicode character names
import unicodedata
print("Unicode name of '😊':", unicodedata.name("😊", "Unknown"))

# --------------------------------------------
# 🧪 Raw strings and escape characters
# --------------------------------------------

print("\nEscape Characters:")
print("Newline:\nNext Line")
print(r"Raw string: C:\Users\Ali")  # Prevents escape

