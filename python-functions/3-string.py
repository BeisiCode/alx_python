#!/usr/bin/env python3
def reverse_string(string, end = ''):
    reverse_string = string[::-1]
    return reverse_string
result = reverse_string("Hello, World!")
print(result)