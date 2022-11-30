#!/usr/bin/python3
for  x in reversed( range(97, 123)):
    if x % 2 == 0:
        print(chr(x), end='')
    elif x % 2 != 0:
        print(chr(x - (ord('a') - ord('A'))), end='')
        

