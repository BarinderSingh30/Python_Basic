#abstrat base class and abstract method : to force a method in a class 

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):

    def __init__(self) -> None:
        self.length=7
        self.breath=8

    def printarea(self):
        return self.length*self.breath


rect1=Rectangle()
print(rect1.printarea())