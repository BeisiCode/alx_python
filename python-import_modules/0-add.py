
a = 1
b = 2

# Importing the add function from add_0.py
import add_0

add_function = add_0.add
if __name__ == "__main__":
    # Printing the result using string formatting
       result = add_function(a, b)
       print("{} + {} = {}".format(a, b, result))