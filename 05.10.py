import argparse
import sys
class Shape:
    __h=0
    __d=0
    def __init__(self, h, d):
        self.width = d
        self.heigth = h



class Triangle(Shape):
    def area(self):
        print(int(1/2*self.heigth*self.width))

class Rectangle(Shape):
    def area(self):
        print(int(self.heigth * self.width))

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-Triangle', nargs='?')
    parser.add_argument('-Rectangle', nargs='?')
    parser.add_argument('width', nargs='?')
    parser.add_argument('height', nargs='?')
    return parser

if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.Triangle:
        triangle_example = Triangle(namespace.height, namespace.width)
        triangle_example.area()
    if namespace.Rectangle:
        rectangle_example = Rectangle(namespace.height, namespace.width)
        rectangle_example.area()
