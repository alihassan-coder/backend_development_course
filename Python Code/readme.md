# Python Course

## Why Use Python?
Python is a versatile and powerful programming language that is easy to learn and use. It is widely used in various fields such as web development, data science, artificial intelligence, and more. Python's simple syntax and readability make it an excellent choice for beginners and experienced programmers alike.

## Course Overview
This course is designed to take you from a beginner to an advanced level in Python programming. Each section will cover specific topics with simple code examples to illustrate the concepts.

## Course Content

### Introduction to Python
- **What is Python?**
- **Installing Python**
- **Writing Your First Python Program**
    ```python
    print("Hello, World!")
    ```

### Python Basics
- **Variables and Data Types**
    ```python
    x = 5
    y = "Hello"
    print(x, y)
    ```
- **Basic Operators**
    ```python
    a = 10
    b = 3
    print(a + b)  # Addition
    print(a - b)  # Subtraction
    print(a * b)  # Multiplication
    print(a / b)  # Division
    ```
- **Input and Output**
    ```python
    name = input("Enter your name: ")
    print("Hello, " + name)
    ```

### Control Flow
- **Conditional Statements**
    ```python
    age = 18
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
    ```
- **Loops**
    - **For Loop**
        ```python
        for i in range(5):
            print(i)
        ```
    - **While Loop**
        ```python
        count = 0
        while count < 5:
            print(count)
            count += 1
        ```

### Data Structures
- **Lists**
    - Creating and Using Lists
        ```python
        fruits = ["apple", "banana", "cherry"]
        print(fruits)
        ```
    - List Methods
        ```python
        fruits.append("orange")
        fruits.remove("banana")
        print(fruits)
        ```
- **Tuples**
    - Definition: Tuples are immutable sequences used to store collections of items.
    - Creating and Using Tuples
        ```python
        my_tuple = ("apple", "banana", "cherry")
        print(my_tuple)
        ```
- **Dictionaries**
    - Creating and Using Dictionaries
        ```python
        person = {"name": "John", "age": 30}
        print(person)
        ```
    - Dictionary Methods
        ```python
        person["age"] = 31
        print(person.keys())
        print(person.values())
        ```
- **Sets**
    - Creating and Using Sets
        ```python
        my_set = {"apple", "banana", "cherry"}
        my_set.add("orange")
        print(my_set)
        ```

### Strings
- **String Operations**
    ```python
    text = "Hello, World!"
    print(text.upper())
    print(text.lower())
    ```
- **String Methods**
    ```python
    print(text.replace("World", "Python"))
    print(text.split(","))
    ```
- **Formatting Strings**
    ```python
    name = "John"
    age = 30
    print(f"My name is {name} and I am {age} years old.")
    ```

### Functions and Modules
- **Defining Functions**
    ```python
    def greet(name):
        return f"Hello, {name}!"
    print(greet("Alice"))
    ```
- **Function Arguments**
    ```python
    def add(a, b):
        return a + b
    print(add(2, 3))
    ```
- **Lambda Functions**
    ```python
    add = lambda a, b: a + b
    print(add(2, 3))
    ```
- **Importing Modules**
    ```python
    import math
    print(math.sqrt(16))
    ```
- **Standard Library Modules**
    ```python
    import datetime
    print(datetime.datetime.now())
    ```

### Object-Oriented Programming
- **Classes and Objects**
    - Defining Classes
        ```python
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
        ```
    - Creating Objects
        ```python
        p1 = Person("John", 30)
        print(p1.name, p1.age)
        ```
    - Instance Variables and Methods
        ```python
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
            
            def greet(self):
                return f"Hello, my name is {self.name}"
        p1 = Person("John", 30)
        print(p1.greet())
        ```
- **Inheritance and Polymorphism**
    - Inheritance
        ```python
        class Student(Person):
            def __init__(self, name, age, student_id):
                super().__init__(name, age)
                self.student_id = student_id
        ```
    - Method Overriding
        ```python
        class Student(Person):
            def greet(self):
                return f"Hello, I am student {self.name}"
        ```
    - Polymorphism
        ```python
        def introduce(person):
            print(person.greet())
        s1 = Student("Alice", 20, "S123")
        introduce(s1)
        ```

### Advanced Topics
- **File Handling**
    - Reading and Writing Files
        ```python
        with open("file.txt", "w") as file:
            file.write("Hello, World!")
        with open("file.txt", "r") as file:
            print(file.read())
        ```
    - Working with CSV Files
        ```python
        import csv
        with open("data.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age"])
            writer.writerow(["John", 30])
        ```
- **Exception Handling**
    - Try, Except, Finally
        ```python
        try:
            x = 1 / 0
        except ZeroDivisionError:
            print("Cannot divide by zero")
        finally:
            print("This will always execute")
        ```
    - Custom Exceptions
        ```python
        class CustomError(Exception):
            pass
        try:
            raise CustomError("An error occurred")
        except CustomError as e:
            print(e)
        ```
- **Working with Libraries**
    - NumPy
        ```python
        import numpy as np
        arr = np.array([1, 2, 3])
        print(arr)
        ```
    - Pandas
        ```python
        import pandas as pd
        df = pd.DataFrame({"Name": ["John", "Alice"], "Age": [30, 25]})
        print(df)
        ```
    - Matplotlib
        ```python
        import matplotlib.pyplot as plt
        plt.plot([1, 2, 3], [4, 5, 6])
        plt.show()
        ```

## Conclusion
By the end of this course, you will have a solid understanding of Python programming and be able to build your own projects. Happy coding!
