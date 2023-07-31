def reverse_string(string, end=' '):
    reversed_str = " "
    for i in range(len(string) - 1, -1, -1):
        reversed_str += string[i]
    return reversed_str

print(reverse_string("Hello"))         # Output: "olleH"
print(reverse_string(""))              # Output: ""
print(reverse_string("madam"))         # Output: "madam"
print(reverse_string("Hello, World!")) # Output: "!dlroW ,olleH"
