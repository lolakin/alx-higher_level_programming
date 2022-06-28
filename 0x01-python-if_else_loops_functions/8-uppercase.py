#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            num1 = 32
        else:
            num1 = 0
        print("{:c}".format(ord(str[i]) - num1), end="")
    print()
