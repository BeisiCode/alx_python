
a = 1
b = 2


from add_0 import add as function

if __name__ == "__main__":
    
    result = function.add(a, b)
    print("{} + {} = {}".format(a, b, result))
