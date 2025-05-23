# The lambda function is like a simple first like the parameter 
# and after : write the exprestion 

# add = lambda a, b: a - b
# print(add(2, 3))

# with open("ali.txt" , "w") as ali:
#     ali.write("Hello, World!")
# with open("file.txt", "r") as file:
#     print(file.read())


# import csv
# with open("data.csv", "w", newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Age"])
#     writer.writerow(["John", 30])



# try:
#     x = 1 / 0
# except Exception as e:
#     print("Cannot divide by zero")
# finally:
#     print("This will always execute")



class CustomError(Exception):
    pass
try:
    raise CustomError("An error occurred")
except CustomError as e:
    print(e)


# import numpy as np
# arr = np.array([1, 2, 3])
# print(arr)