class Square:
    def __init__(self, size=0):
        self._size = size  # Private attribute with a single underscore

    def get_size(self):
        return self._size

    def set_size(self, size):
        if size < 0:
            print("Size must be >= 0")
        else:
            self._size = size

my_square = Square(5)
print(my_square.get_size())  # Using the getter method
my_square.set_size(10)       # Using the setter method
print(my_square.get_size())
