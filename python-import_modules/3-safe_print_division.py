def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = a / b
    finally:
        print("Inside result: {}".format(result))
    

# Test the function
