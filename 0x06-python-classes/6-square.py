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
            return None

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print('')

        for j in range(1, self.area() + 1):
            if j % self.__size == 1:
                print('{:>{w}}'.format('#', w=self.__position[0] + 1), end='')
            else:
                print('#', end='')

            if j % self.__size == 0 and j > 0:
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value
