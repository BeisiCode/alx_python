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
    print({}.format(a, int.__name__))
if is_same_class(a, float):
    print({}.format(a, float.__name__))
if is_same_class(a, object):
    print({}.format(a, object.__name__))

