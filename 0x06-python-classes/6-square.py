#!/usr/bin/python3
''' OOP Classes'''


class Square:
    '''This is a Square object'''
    def __init__(self, size=0, position=(0, 0)):
        '''
        __init__
        instantiates size in the square

        Fields:
        size (int): integer of the square size
        positiion (coord): coordinates of a point
        Raises:
        ValueError: size less than 0
        TypeError: size not integer

        '''
        self.size = size
        self.position = position

    def area(self):
        '''
        area(): returns the area of the square

        '''

        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            if self.__position[0] == 0:
                print('#' * self.__size)
            else:
                print("_" * self.__position[0] + '#' * self.__size)

    
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            if type(value[0]) or type(value[1]) is not int:
                raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

