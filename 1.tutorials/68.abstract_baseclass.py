#abstrat base class and abstract method : to force a method in a class 
# you cannot make object of abstract base class

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):

    def __init__(self) -> None:
        self.length=7
        self.breath=8

    def printarea(self):                    # if you don't define this it will give you error
        return self.length*self.breath


rect1=Rectangle()
print(rect1.printarea())