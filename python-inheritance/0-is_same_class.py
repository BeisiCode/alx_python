def is_same_class(obj, a_class):
    """
    Check if the given object is an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the specified class, False otherwise.
    """
    return type(obj) is a_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__), end=" ")
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__), end=" ")
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__), end=" ")

