def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
     print("Inside result: {}".format(result))
    return result

# Test the function
#a = 10
#b = 2
#safe_print_division(a, b)
#result = safe_print_division(a, b)
#print("{:d} / {:d} = {}".format(a, b, result))