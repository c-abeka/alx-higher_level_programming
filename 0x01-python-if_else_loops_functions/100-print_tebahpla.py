#!/usr/bin/python3
i = 0
for  x in reversed( range(97, 123)):
    print(chr(x - i), end='')
    if i == 0:
        i = 32
    else:
        i = 0
