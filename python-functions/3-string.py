def reverse_string(string, /n):
    reverse_string = string[:-1]
    return reverse_string

print(reverse_string("Hello"))         # Output: "olleH"
print(reverse_string(""))              # Output: ""
print(reverse_string("madam"))         # Output: "madam"
print(reverse_string("Hello, World!")) # Output: "!dlroW ,olleH"
