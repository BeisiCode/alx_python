#!/usr/bin/env python3
convert_to_celsius = __import__('2-temperature').convert_to_celsius
def main():
    convert_to_celcius(100)
    convert_to_celcius(-40)
    convert_to_celcius(-459.67)
    convert_to_celcius(32)

    print(convert_to_celsius(100))
    print(convert_to_celsius(-40))
    print(convert_to_celsius(-459.67))
    print(convert_to_celsius(32))


def convert_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5 / 9
    return celcius

main()