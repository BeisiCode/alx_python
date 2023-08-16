class Square:
    def __init__(self, size):
        self.__size = size

my_square = Square(3)

print(type(my_square), file=open(1, 'w', closefd=False))
print(my_square.__dict__, file=open(1, 'w', closefd=False), sep="\n")

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)