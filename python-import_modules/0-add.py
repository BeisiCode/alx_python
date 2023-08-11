
# 0-add.py
a = 1
b = 2

# Importing add function from add_0.py and renaming it as 'add_function'
import add_0 as add_function

if __name__ == "__main__":
    # Printing the result using string formatting with .format()
    result = add_function.add(a, b)
    print("{} + {} = {}".format(a, b, result))
