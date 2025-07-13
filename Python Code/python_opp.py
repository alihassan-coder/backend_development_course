# Example 1

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print("Available Books:")
        for book in self.books:
            print(book)

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"You have borrowed '{book}'")
        else:
            print("Book not available.")

    def return_book(self, book):
        self.books.append(book)
        print(f"You have returned '{book}'")

# Usage
lib = Library()
lib.add_book("Python Basics")
lib.add_book("DSA in Python")
lib.show_books()
lib.borrow_book("Python Basics")
lib.show_books()
lib.return_book("Python Basics")
lib.show_books()


# example 2
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)

    def show_order(self):
        total = 0
        print("Your Order:")
        for item in self.items:
            print(f"{item.name} - Rs {item.price}")
            total += item.price
        print(f"Total: Rs {total}")

# Usage
burger = MenuItem("Burger", 200)
fries = MenuItem("Fries", 100)

order1 = Order()
order1.add_item(burger)
order1.add_item(fries)
order1.show_order()



# Example 3


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = {}

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def show_report(self):
        print(f"Report Card for {self.name} (Roll No: {self.roll_no})")
        total = 0
        for sub, mark in self.marks.items():
            print(f"{sub}: {mark}")
            total += mark
        average = total / len(self.marks)
        grade = self.get_grade(average)
        print("Grade:", grade)

    def get_grade(self, avg):
        if avg >= 90:
            return 'A+'
        elif avg >= 75:
            return 'A'
        elif avg >= 60:
            return 'B'
        else:
            return 'C'

# Usage
s = Student("Ali", 101)
s.add_mark("Math", 95)
s.add_mark("Science", 88)
s.add_mark("English", 76)
s.show_report()
