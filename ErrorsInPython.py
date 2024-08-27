#Errors in Python 

"""
SyntaxError

Cause: This occurs when the Python interpreter encounters code that is not valid Python syntax.
Example:
"""
if x = 10  # Missing colon and using '=' instead of '=='
    print("x is 10")


"""
IndentationError :
Cause: This occurs when the indentation of your code is not consistent. Python relies on indentation to define the structure of the code (e.g., which statements belong to a loop or a function).

"""

def greet():
print("Hello, World!")  # Incorrectly indented


"""
NameError

Cause: This occurs when you try to use a variable or function name that has not been defined.
"""

print(y)   # y is not defined anywhere , or its a local variable # Python raises a NameError


"""
TypeError: Cause: This occurs when an operation is performed on an inappropriate type.
"""

result = "5" + 10  # You cannot add a string ("5") and an integer (10). Python doesn't know how to handle this operation, so it raises a TypeError.


"""
IndexError 
Cause: This occurs when you try to access an index that is out of the range of a list, string, or tuple.
"""
my_list = [1, 2, 3]
print(my_list[3])
# my_list has three elements, but Python uses zero-based indexing, so valid indices are 0, 1, and 2. Attempting to access index 3 results in an IndexError.


"""
KeyError : Cause: This occurs when you try to access a dictionary key that doesn't exist.
"""

my_dict = {"a": 1, "b": 2}
print(my_dict["c"])


"""
ValueError : Cause: This occurs when a function receives an argument of the correct type but an inappropriate value.
"""

int("abc")
#The int() function expects a string that can be converted to an integer, like "123". Since "abc" cannot be converted, Python raises a ValueError.

"""
AttributeError : Cause: This occurs when you try to access an attribute or method that does not exist for a particular object.
"""
my_list = [1, 2, 3]
my_list.push(4)
# Lists in Python do not have a push() method; they have an append() method. Attempting to use push() results in an AttributeError.



"""
ZeroDivisionError : Cause: This occurs when you attempt to divide a number by zero, which is mathematically undefined.
"""
result = 10 / 0

"""
Python raises a ZeroDivisionError.

Handling Errors with try and except

To manage errors and prevent your program from crashing, you can use try and except blocks to catch and handle exceptions.
"""
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

"""
try block: The code that might cause an error is placed inside the try block.
except block: This block catches the specific error and executes code to handle it.
If the user enters something that's not a number, the program will print "Please enter a valid number." instead of crashing with a ValueError.
Similarly, if the user enters 0, it will handle the ZeroDivisionError gracefully.
"""




