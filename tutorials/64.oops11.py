#Overridding and super()


class A:
    classv1 = 'I am a class variable in class A'

    def __init__(self):
        self.var1 = 'i am inside class A\'s constructor'
        self.classv1 = 'Instance var in class A'
    
class B(A):
    classv1=' i am class B'
    def __init__(self):
        super().__init__()                              # it will run the constructor of super class and assign the values to instance
        self.var1 = 'i am inside class B\'s constructor' #it will run and change the value of the instance
        self.classv1 = 'Instance var in class B'        # if super called after these assignments then the values of super class will be assigned

        print(super().classv1)






a=A()
b=B()


print(b.var1)


#first it will check instances in its own class then its super class if it didn't find them there then he will serach for variables in its class then its super class
