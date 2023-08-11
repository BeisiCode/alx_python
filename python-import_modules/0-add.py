# 0-add.py
a = 1
b = 2

# Importing the add function from add_0.py
from add_0 import sum

if __name__ == "__main__":
    # Printing the result using string formatting
    result = add_0.add(a, b)
    print(f"{a} + {b} = {result}")
