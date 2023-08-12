"""a = 1
b = 2


from add_0 import function

if __name__ == "__main__":
    
    result = function.add(a, b)
    print("{} + {} = {}".format(a, b, result))
"""#!/usr/bin/python3

# Assign values to variables
a = 1
b = 2

# Importing the add function from add_0.py
import add_0

# Using the imported add function to calculate the result
result = add_0.add(a, b)

# Printing the result using string formatting
print("{} + {} = {}".format(a, b, result))
