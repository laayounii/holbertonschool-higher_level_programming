#!/usr/bin/python3
'''Module for Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructor.'''

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Width of this rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        '''Height of this rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        '''x of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        '''y of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def area(self):
        '''Return the area of the rectangle.'''
        return self.__width * self.__height

    def display(self):
        '''Print the Rectangle instance with the character #.'''
        print('\n' * self.__y, end='')
        for _ in range(self.__height):
            print(' ' * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        '''Return a string representation of the Rectangle.'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        '''Assign arguments to attributes.'''
        attrs = ['id', 'width', 'height', 'x', 'y']
        for i in range(len(args)):
            setattr(self, attrs[i], args[i])
