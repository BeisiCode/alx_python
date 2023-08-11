
a = 1
b = 2


import add_0 as add_function

if __name__ == "__main__":
    # Printing the result using string formatting with .format()
    result = add_function.add(a, b)
    print("{} + {} = {}".format(a, b, result))
