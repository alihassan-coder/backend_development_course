"""
===============================
📁 Python File Handling Tutorial
===============================

This file explains:
- What is File Handling
- Reading and Writing Files
- Using "with" statement
- Modes in File Handling
- Methods of File Object
- Examples of each
"""

# 🔹 What is File Handling?
# File handling in Python lets you create, read, update, and delete files.
# Python has built-in functions like open(), read(), write(), and close().

# ==========================================
# 🔸 Opening a File
# ==========================================

# Syntax:
# open(file_name, mode)

# Modes:
# 'r' - Read (default), file must exist
# 'w' - Write, creates new or overwrites existing
# 'a' - Append, adds to the end of file
# 'x' - Create, error if file exists
# 'b' - Binary mode
# 't' - Text mode (default)

# Example: Open a file for writing
f = open("example.txt", "w")
f.write("Hello, this is a test file.\n")
f.write("Second line of text.")
f.close()

# ==========================================
# 🔸 Reading a File
# ==========================================

f = open("example.txt", "r")
content = f.read()  # reads the whole file
print("Reading entire file:")
print(content)
f.close()

# ==========================================
# 🔸 Reading Line by Line
# ==========================================

f = open("example.txt", "r")
print("Reading line by line:")
for line in f:
    print(line.strip())
f.close()

# ==========================================
# 🔸 Using 'with' Statement (Recommended)
# ==========================================

# It automatically closes the file after the block
with open("example.txt", "r") as file:
    print("With statement content:")
    print(file.read())

# ==========================================
# 🔸 Writing to a File
# ==========================================

with open("write_example.txt", "w") as f:
    f.write("This is a new file.\n")
    f.write("Written using 'with'.")

# ==========================================
# 🔸 Appending to a File
# ==========================================

with open("write_example.txt", "a") as f:
    f.write("\nAdding more lines.")
    f.write("\nThis is appended.")

# ==========================================
# 🔸 Reading a File using read(), readline(), readlines()
# ==========================================

with open("write_example.txt", "r") as f:
    print("Using read():")
    print(f.read())

with open("write_example.txt", "r") as f:
    print("\nUsing readline():")
    print(f.readline())  # Reads one line

with open("write_example.txt", "r") as f:
    print("\nUsing readlines():")
    print(f.readlines())  # Returns list of all lines

# ==========================================
# 🔸 File Object Methods
# ==========================================

# Assume we have a file opened as f
# f.read(size)       -> Reads size characters
# f.readline()       -> Reads one line
# f.readlines()      -> Returns list of lines
# f.write(string)    -> Writes string to file
# f.writelines(list) -> Writes list of strings
# f.seek(offset)     -> Moves to byte offset
# f.tell()           -> Returns current position
# f.close()          -> Closes the file
# f.name             -> Name of the file
# f.mode             -> Mode file was opened with
# f.closed           -> True if file is closed

# Example:
with open("example.txt", "r") as f:
    print("\nFile name:", f.name)
    print("File mode:", f.mode)
    print("Is closed?", f.closed)

print("After 'with', is file closed?", f.closed)

# ==========================================
# 🔸 Handling File Not Found / Errors
# ==========================================

try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("\nFile not found!")

# ==========================================
# ✅ Summary:
# ==========================================
# Always use 'with' to handle files safely.
# Choose correct mode: 'r', 'w', 'a'
# Use methods like read(), write(), readline(), seek(), tell(), close()
# Use try-except to handle errors
# ==========================================
# what is means by with explain with in file handling
# it is used to open a file and automatically close it after the block of code is executed, ensuring proper resource management.
