#!/usr/bin/env python3
def reverse_string(string):
    reverse_string = string[::-1]
    return reverse_string
result = reverse_string("Hello, World!")
print(result, end='')

print(reverse_string("hello"))  # Output: "olleh"
print(reverse_string("python")) # Output: "nohtyp"
print(reverse_string(""))       # Output: ""
