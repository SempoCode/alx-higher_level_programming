#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 123):
            d = ord(str[i]) - 32
        else:
            d = ord(str[i])
        print('{}'.format(chr(d)), end='')
    print('\n', end='')
