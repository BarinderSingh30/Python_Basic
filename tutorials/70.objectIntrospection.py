# object introspection : tell about object - from which class, type of the object, storage location

class A:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

barinder=A('Barinder',20)

print(type(barinder))
print(dir(barinder))
print(id(barinder))

# you can also use inspect module to inspect the object
