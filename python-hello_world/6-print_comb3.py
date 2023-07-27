for tens in range(10):
    for ones in range(tens + 1, 10):
        print("{:02d}, ".format(tens*10+ones), end="" if ones == 9 else"")
print("\n")
